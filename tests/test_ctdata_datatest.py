# -*- coding: utf-8 -*-

def test_yaml_parse(testdir):
    """Confirm that pytest can correctly use fixture to load yaml"""

    # create a temporary yaml
    testdir.makefile('.yml', test="""
        # Children by Family Type
        ---
        Dataset:
            Name: Children by Family Type
            Description: Children by Family Type reports the number and percent of children living in families by child age and by family type.
            Full Description: Children by Family Type reports the number and percent of children living in families by child age and by family type.
            Source: American Community Survey
        ...
    """)

    testdir.makepyfile("""
        METADATA_FILE='test.yml'


        def test_metadata_fixture(metadata):
            assert metadata['Dataset']['Name'] == 'Children by Family Type'
    """)

    result = testdir.runpytest(
        '-v'
    )
    result.stdout.fnmatch_lines([
        '*::test_metadata_fixture PASSED',
    ])

    assert result.ret == 0


def test_geography_extraction(testdir):
    """Confirm that pytest can correctly use fixture to load yaml"""

    # create a temporary yaml
    testdir.makefile('.yml', test="""
        # Children by Family Type
        ---
        Dataset:
            Name: Children by Family Type
            Description: Children by Family Type reports the number and percent of children living in families by child age and by family type.
            Geography: Town
        ...
    """)

    testdir.makepyfile("""
        METADATA_FILE='test.yml'


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

def test_metadata_domain_extract(testdir):
    """Confirm that pytest can correctly use fixture to load yaml"""

    # create a temporary yaml
    testdir.makefile('.yml', test="""
        # Children by Family Type
        ---
        Dataset:
            Name: Children by Family Type
            Description: Children by Family Type reports the number and percent of children living in families by child age and by family type.
            Geography: Town
            Domain: Demographics
        ...
    """)

    testdir.makepyfile("""
        METADATA_FILE='test.yml'


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

