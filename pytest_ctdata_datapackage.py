# -*- coding: utf-8 -*-

import pytest
import csv
from collections import defaultdict
import itertools
import json

CTDATA_DATASET_DOMAINS = ['Civic Vitality', 'Demographics', 'Economy', 'Education', 'Health', 'Housing', 'Safety']

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


# TODO Write test for pulling spot checks
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