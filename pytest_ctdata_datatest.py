# -*- coding: utf-8 -*-

import pytest
import csv
from collections import defaultdict
import yaml
import os
import itertools

CTDATA_DATASET_DOMAINS = ['Civic Vitality', 'Demographics', 'Economy', 'Education', 'Health', 'Housing', 'Safety']

def nested_dict():
   return defaultdict(nested_dict)

def get_yaml_files():
    for(dirpath, _, filenames) in os.walk('.'):
        for filename in filenames:
            f,e = os.path.splitext(filename)
            if e == 'yml':
                yield os.path.join(dirpath, filename)

@pytest.fixture
def metadata(request):
    """Load the specified metadata yaml file and parse"""
    try:
        yamlfile = getattr(request.module, "METADATA_FILE")
    except AttributeError:
        return dict()
    with open(yamlfile, 'r') as stream:
        metadata = yaml.load(stream)
        return metadata

@pytest.fixture
def years(metadata):
    """Extract years from metadata and convert to list"""
    try:
        return [x for x in metadata['Dataset']['Years in Catalog'][0].split(';')]
    except KeyError:
        return []


@pytest.fixture
def spotchecks(metadata):
    try:
        [(v[0], v[1], v[2], float(v[3])) for k, v in metadata['Dataset']['Spot Checks'].items()]
    except KeyError:
        return []

@pytest.fixture
def dataset(request):
    """Load dataset"""
    try:
        datafile = getattr(request.module, 'TARGET_FILE')
    except AttributeError:
        return []
    with open(datafile, 'r') as file:
        reader = csv.DictReader(file)
        return [x for x in reader]


@pytest.fixture
def _geography(metadata):
    """Extract specified geography from metadata YAML"""
    try:
        return metadata['Dataset']['Geography']
    except KeyError:
        return ''


@pytest.fixture
def geographies(data, _geography):
    """Use metadata file to extract a set of unique towns from data file"""
    return {x[_geography] for x in data}


@pytest.fixture
def domain(metadata):
    return metadata['Dataset']['Domain'] in CTDATA_DATASET_DOMAINS

@pytest.fixture
def dimension_group_list(metadata):
    return metadata['Dataset']['Dimension Groups']

@pytest.fixture
def dimensions(metadata):
    return metadata['Dataset']['Dimensions']

@pytest.fixture
def dimension_combinations(dimension_group_list, dimensions):
    list_of_combinations = []
    for combination in dimension_group_list:
        combos = list(itertools.product(*[dimensions[i] for i in combination]))
        list_of_combinations.append(combos)
    return list_of_combinations