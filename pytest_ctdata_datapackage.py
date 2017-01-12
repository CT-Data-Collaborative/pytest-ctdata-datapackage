# -*- coding: utf-8 -*-

import csv
import itertools
import json
from collections import defaultdict, namedtuple

import pytest

CTDATA_DATASET_DOMAINS = ['Civic Vitality', 'Demographics', 'Economy', 'Education', 'Health', 'Housing', 'Safety']


SPOT_CHECK_CONVERTERS = {
    "float": float,
    "int": int,
    "percent": lambda x: round(x*100,1)
}

Spotcheck = namedtuple("Spotcheck", ['spec', 'expected', 'actual'])


def helper_filter(item, conditions):
    for k,v in conditions:
        if item[k] != v:
            return False
    return True


def _lookerupper(dataset, filter):
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
    return result



def nested_dict():
   return defaultdict(nested_dict)

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
def spotchecks(metadata):
    return metadata['spot_checks']

@pytest.fixture
def dataset(metadata):
    """Load dataset"""
    datafile = metadata['resources'][0]['path']
    with open(datafile, 'r') as file:
        reader = csv.DictReader(file)
        return [x for x in reader]

@pytest.fixture
def _geography(metadata):
    """Extract specified geography from datapackage.json"""
    try:
        return metadata['ckan_extras']['geography']['value']
    except KeyError:
        return ''

@pytest.fixture
def geographies(dataset, _geography):
    """Use metadata file to extract a set of unique towns from data file"""
    return {x[_geography] for x in dataset}

@pytest.fixture
def domain(metadata):
    return metadata['ckan_extras']['domain']['value'] in CTDATA_DATASET_DOMAINS

@pytest.fixture
def dimension_group_list(metadata):
    return metadata['dimension_groups']

@pytest.fixture
def dimensions(metadata):
    return metadata['resources'][0]['schema']['fields']

@pytest.fixture
def dimension_combinations(dimension_group_list, dimensions):
    list_of_combinations = []
    dimension_lookup = {d['name']: d for d in dimensions}
    flat_dimensions = [item for sublist in dimension_group_list for item in sublist]
    possible_dimension_values = {d: dimension_lookup[d]['constraints']['enum'] for d in flat_dimensions}

    for combination in dimension_group_list:
        combos = list(itertools.product(*[possible_dimension_values[i] for i in combination]))
        list_of_combinations.append(combos)
    return list_of_combinations

def lookup_wrapper(dataset, filter, convertor):
    lookup = _lookerupper(dataset, filter)
    try:
        final_value = convertor(lookup)
    except TypeError:
        final_value = None
    return final_value

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
            expected_final_value = lookup_wrapper(dataset, check['expected']['value'], convertor)
        else:
            expected_final_value = -1

        if check['type'] == "$lookup":
            final_value = lookup_wrapper(dataset, check['filter'], convertor)
        elif check['type'] == '$reduce':
            final_value = sum([lookup_wrapper(dataset, f, convertor) for f in check['filter']])
        elif check['type'] == '$percent':
            filter = check['filter']
            try:
                numerator = lookup_wrapper(dataset, filter['numerator'], convertor)
                denominator = lookup_wrapper(dataset, filter['denominator'], convertor)
            except KeyError:
                final_value = None
            final_value = round(100*(numerator/denominator),1)
        else:
            final_value = None

        check_result = Spotcheck(spec=check, expected=expected_final_value, actual=final_value)
        spotcheck_results.append(check_result)
    return spotcheck_results
