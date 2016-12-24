# -*- coding: utf-8 -*-

import pytest
import csv
from collections import defaultdict
import yaml
import os

def pytest_addoption(parser):
    group = parser.getgroup('ctdata_datatest')
    group.addoption(
        '--foo',
        action='store',
        dest='dest_foo',
        default='2016',
        help='Set the value for the fixture "bar".'
    )

    parser.addini('HELLO', 'Dummy pytest.ini setting')


@pytest.fixture
def bar(request):
    return request.config.option.dest_foo

def nested_dict():
   return defaultdict(nested_dict)

def get_yaml_files():
    for(dirpath, _, filenames) in os.walk('.'):
        for filename in filenames:
            f,e = os.path.splitext(filename)
            if e == 'yml':
                yield os.path.join(dirpath, filename)

@pytest.fixture
def metadata(session):
    yamls = list(get_yaml_file())
    with open(yamls[0], 'r') as stream:
        metadata = yaml.load(stream)
        return metadata

