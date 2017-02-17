# -*- coding: utf-8 -*-

import csv
import itertools
import json
from collections import namedtuple

import pytest

CTDATA_DATASET_DOMAINS = {
    'Civic Vitality': ['Engagement', 'Public Finance'],
    'Demographics': ['Births', 'Characteristics', 'Family Structure', 'Population'],
    'Economy': ['Commuting', 'Employment', 'Income', 'Poverty', 'Social Assistance'],
    'Education': ['Early Care and Education', 'Educational Attainment', 'Kindergarten Readiness',
                  'Student Behavior', 'Student Demographics', 'Testing and Evaluation'],
    'Health': ['Chronic Disease', 'Early Childhood Development', 'Health Care Access and Insurance',
               'Health Outcomes', 'Mental Health', 'Mortality', 'Substance Abuse'],
    'Housing': ['Household Characteristics', 'Housing Characteristics', 'Residential Mobility'],
    'Safety': ['Child Welfare', 'Public Safety']
}

SOURCES = ["uscensus", "ctsde", "ctdph", "ctopm", "samhsa", "ctdmhas", "municipalities", "ctdss", "ctdol", "ctdecd",
        "ctdcf", "ctocme", "ctoec", "ctdespp", "seda", "ctlib", "cthfa", "ctdot", "ctdoh"]

SPOT_CHECK_CONVERTERS = {
    "float": float,
    "int": int,
    "percent": lambda x: round(x*100,1)
}

Spotcheck = namedtuple("Spotcheck", ['spec', 'expected', 'actual'])
RowCounts = namedtuple("Rowcount", ['expected', 'actual'])

def helper_filter(item, conditions):
    for k,v in conditions:
        if item[k] != v:
            return False
    return True


def _lookerupper(dataset, filter, convertor):
    """Lookup function for spotchecks"""
    filters = [(k, v) for k, v in filter.items()]
    matches = [x for x in dataset if helper_filter(x, filters)]
    try:
        match = matches[0]
    except IndexError:
        return None
    try:
        result = match['Value']
    except KeyError:
        return None
    try:
        final_value = convertor(result)
    except TypeError:
        final_value = None
    return final_value


# Fixtures related to metadata
@pytest.fixture
def metadata(request):
    """Load and parse the datapackage.json"""
    with open('datapackage.json', 'r') as stream:
        metadata = json.load(stream)
        return metadata

@pytest.fixture
def years(metadata):
    """Extract years from metadata and convert to list"""
    try:
        return metadata['ckan_extras']['years_in_catalog']['value']
    except KeyError:
        return []


@pytest.fixture
def dataset(metadata):
    """Load dataset"""
    datafile = metadata['resources'][0]['path']
    with open(datafile, 'r') as file:
        reader = csv.DictReader(file)
        return [x for x in reader]

@pytest.fixture
def geography(metadata):
    """Extract specified geography from datapackage.json"""
    try:
        return metadata['ckan_extras']['geography']['value']
    except KeyError:
        return ''

@pytest.fixture
def geographies(dataset, geography):
    """Use metadata file to extract a set of unique towns from data file"""
    return {x[geography] for x in dataset}

@pytest.fixture
def geography_units_count(metadata):
    return metadata['ckan_extras']['expected_number_of_geographies']['value']

@pytest.fixture
def dimension_groups(metadata):
    return metadata['dimension_groups']

@pytest.fixture
def dimensions(metadata):
    return metadata['resources'][0]['schema']['fields']


@pytest.fixture
def dimension_combinations(dimension_groups):
    list_of_combinations = []
    flat_dimensions = [[val for key,val in i.items()] for i in dimension_groups]

    for combination in flat_dimensions:
        combos = itertools.product(*[i for i in combination])
        for c in combos:
            list_of_combinations.append(c)
    return list_of_combinations


@pytest.fixture
def spotchecks(metadata):
    return metadata['spot_checks']


@pytest.fixture
def spotcheck_results(spotchecks, dataset):
    spotcheck_results = []
    for check in spotchecks:
        final_value_type = check['expected']['number type']
        convertor = SPOT_CHECK_CONVERTERS[final_value_type]

        # Handle parsing the expected value.
        if check['expected']['type'] == '$match':
            expected_final_value = check['expected']['value']
        elif check['expected']['type'] == '$lookup':
            expected_final_value = _lookerupper(dataset, check['expected']['value'], convertor)
        else:
            expected_final_value = -1

        if check['type'] == "$lookup":
            final_value = _lookerupper(dataset, check['filter'], convertor)
        elif check['type'] == '$reduce':
            final_value = sum([_lookerupper(dataset, f, convertor) for f in check['filter']])
        elif check['type'] == '$percent':
            filter = check['filter']
            try:
                numerator = _lookerupper(dataset, filter['numerator'], convertor)
                denominator = _lookerupper(dataset, filter['denominator'], convertor)
            except KeyError:
                final_value = None
            final_value = round(100*(numerator/denominator),1)
        else:
            final_value = None

        check_result = Spotcheck(spec=check, expected=expected_final_value, actual=final_value)
        spotcheck_results.append(check_result)
    return spotcheck_results


# TODO Hard coding the number of geos is bad.
@pytest.fixture
def rowcount(dataset, years, geography_units_count, dimension_combinations):
    expected_row_count = len(years) * geography_units_count * len(dimension_combinations)
    actual_row_count = len(dataset)
    return RowCounts(expected=expected_row_count, actual=actual_row_count)


@pytest.fixture
def domain(metadata):
    return metadata['ckan_extras']['domain']['value']

@pytest.fixture
def subdomain(metadata):
    return metadata['ckan_extras']['subdomain']['value']

@pytest.fixture
def domain_map():
    return CTDATA_DATASET_DOMAINS

@pytest.fixture
def source_options():
    return SOURCES

@pytest.fixture
def source(metadata):
    return metadata['sources']


@pytest.fixture
def schema(metadata):
    return metadata['resources'][0]['schema']['fields']


@pytest.fixture
def schema_test(schema):
    dimensions = [s for s in schema if s['dimension']]
    for d in dimensions:
        if not isinstance(d["constraints"]["enum"], list):
            return False
    return True