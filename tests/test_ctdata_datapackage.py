# -*- coding: utf-8 -*-


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
                def test_metadata_geography(geography):
                    assert geography == 'Town'
            """)
    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_geography PASSED',
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
        def test_dimension_group_list(dimension_groups):
            assert set(dimension_groups[0].keys()) == {"English Language Learner", "Grade"}
            assert set(dimension_groups[1].keys()) == {"Students with Disabilities"}
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_dimension_group_list PASSED',
    ])

    assert result.ret == 0


def test_dimension_permutations_dataset_one(testdir, datapackage):
    """Confirm that pytest can correctly use fixture to load yaml"""


    testdir.makepyfile("""
        def test_dimension_permutations(dimension_combinations):
            assert len(dimension_combinations) == 10
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_dimension_permutations PASSED',
    ])

    assert result.ret == 0

def test_dimension_permutations_dataset_two(testdir, housing_datapackage):
    """Confirm that pytest can correctly use fixture to load yaml"""


    testdir.makepyfile("""
        def test_dimension_permutations(dimension_combinations):
            assert len(dimension_combinations) == 6
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


def test_spotcheck_lookups(testdir, housing_datapackage, housing_datafile):

    testdir.makepyfile("""
        import pytest

        def test_spotcheck_testing(spotcheck_results):
            for check in spotcheck_results:
                assert check.expected == check.actual
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_spotcheck_testing PASSED',
    ])

    assert result.ret == 0


def test_geoes_are_valid_towns(testdir, housing_datapackage, housing_datafile):

    testdir.makepyfile("""
        import pytest
        import datapackage

        def helper_filter(item, conditions):
            for k,v in conditions:
                if item[k] != v:
                    return False
            return True

        @pytest.fixture
        def towns():
            dp = datapackage.DataPackage(
                'https://raw.githubusercontent.com/CT-Data-Collaborative/ct-town-list/master/datapackage.json')
            return dp.resources[0].data

        def test_geoes_are_valid_towns(towns, geographies):
            assert set(geographies) == set([x['Town'] for x in towns])
   """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_geoes_are_valid_towns PASSED',
    ])

    assert result.ret == 0


def test_row_counts(testdir, housing_datapackage, housing_datafile):

    testdir.makepyfile("""
        def test_dataset_row_counts(rowcount):
            assert rowcount.actual == rowcount.expected
        """)

    result = testdir.runpytest('-v')

    result.stdout.fnmatch_lines([
        '*::test_dataset_row_counts PASSED',
    ])

    assert result.ret == 0


def test_domain(testdir, housing_datapackage):

    testdir.makepyfile("""
        def test_domain(domain):
            assert domain == 'Housing'
        """)

    result = testdir.runpytest('-v')

    result.stdout.fnmatch_lines([
        '*::test_domain PASSED',
    ])

    assert result.ret == 0


def test_subdomain(testdir, housing_datapackage):

    testdir.makepyfile("""
        def test_subdomain(subdomain):
            assert subdomain == 'Housing Characteristics'
        """)

    result = testdir.runpytest('-v')

    result.stdout.fnmatch_lines([
        '*::test_subdomain PASSED',
    ])

    assert result.ret == 0


def test_domain_subdomain_validation(testdir, housing_datapackage):
    testdir.makepyfile("""
        def test_domain_subdomain_validation(domain_map, domain, subdomain):
            assert domain in domain_map
            assert subdomain in domain_map[domain]
    """)

    result = testdir.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_domain_subdomain_validation PASSED',])

    assert result.ret == 0


def test_source_validation(testdir, housing_datapackage):
    testdir.makepyfile("""
        def test_source_validation(source_options, source):
            for s in source:
                assert s['name'] in source_options
    """)

    result = testdir.runpytest('-v')
    result.stdout.fnmatch_lines(['*::test_source_validation PASSED',])

    assert result.ret == 0