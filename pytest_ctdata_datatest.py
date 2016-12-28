# -*- coding: utf-8 -*-

import pytest
import csv
from collections import defaultdict
import yaml
import os

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
def expected_years(metadata):
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
    try:
        datafile = getattr(request.module, 'TARGET_FILE')
    except AttributeError:
        return []
    with open(datafile, 'r') as file:
        reader = csv.DictReader(file)
        return [x for x in reader]


@pytest.fixture
def geography(metadata):
    try:
        return metadata['Dataset']['Geography']
    except KeyError:
        return ''


@pytest.fixture
def geographies(data, geography):
    return {x[geography] for x in data}


@pytest.fixture
def domain(metadata):
    return metadata['Dataset']['Domain'] in CTDATA_DATASET_DOMAINS