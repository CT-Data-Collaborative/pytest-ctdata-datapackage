# -*- coding: utf-8 -*-

def helper_filter(item, conditions):
    for k,v in conditions:
        if item[k] != v:
            return False
    return True

def test_datapackagejson_parse(testdir, datapackage):
    """Test loading of datapackage json file"""

    testdir.makepyfile("""
           def test_metadata_fixture(metadata):
               assert metadata['title'] == 'Children by Family Type'
               assert metadata['name'] == 'children-by-family-type'
       """)


    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_fixture PASSED',
    ])


def test_geography_extraction(testdir, datapackage):
    """Test geography extraction fixture"""

    testdir.makepyfile("""
                def test_metadata_geography(_geography):
                    assert _geography == 'Town'
            """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_geography PASSED',
    ])

    assert result.ret == 0


def test_metadata_domain_extract(testdir, datapackage):
    """Test domain extraction fixture"""

    testdir.makepyfile("""
        def test_metadata_domain(domain):
            assert domain
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_domain PASSED',
    ])

    assert result.ret == 0


def test_years_extract(testdir, datapackage):
    """Test years extraction fixture"""

    testdir.makepyfile("""
        def test_metadata_years(years):
            assert years == ["2016", "2015", "2014", "2013"]
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_years PASSED',
    ])

    assert result.ret == 0


def test_dimension_group_list_setup(testdir, datapackage):
    """Test extraction of dimension groups as prerequisite for permutation test"""

    testdir.makepyfile("""
        def test_dimension_group_list(dimension_group_list):
            assert dimension_group_list[0] == ["English Language Learner", "Grade"]
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_dimension_group_list PASSED',
    ])

    assert result.ret == 0


def test_dimension_permutations(testdir, datapackage):
    """Confirm that pytest can correctly use fixture to load yaml"""


    testdir.makepyfile("""
        def test_dimension_permutations(dimension_combinations):
            assert len(dimension_combinations[0]) == 8
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_dimension_permutations PASSED',
    ])

    assert result.ret == 0


def test_spotcheck_fixture(testdir, datapackage):
    """Test extraction of spotchecks from datapackage"""


    testdir.makepyfile("""
        def test_spotcheck_fixture(spotchecks):
            assert len(spotchecks) == 2
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_spotcheck_fixture PASSED',
    ])

    assert result.ret == 0

def test_datafile_load(testdir, datapackage, datafile):

    testdir.makepyfile("""
            def test_datafile_load(dataset):
                assert len(dataset) == 2
        """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_datafile_load PASSED',
    ])

    assert result.ret == 0


def test_spotcheck_lookups(testdir, datapackage, datafile):

    testdir.makepyfile("""
            import pytest

            def helper_filter(item, conditions):
                for k,v in conditions:
                    if item[k] != v:
                        return False
                return True

            def test_spotcheck_testing(spotchecks, dataset):
                for check in spotchecks:
                    v = check['Value']
                    filters = [(k,v) for k,v in check.items() if k != 'Value']
                    matches = list(filter(lambda x: helper_filter(x, filters), dataset))
                    match = matches[0]
                    assert len(matches) == 1
                    assert match['Value'] == str(v)
       """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_spotcheck_testing PASSED',
    ])

    assert result.ret == 0