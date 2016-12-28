# -*- coding: utf-8 -*-

from pytest_ctdata_datatest import metadata

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


# def test_bar_fixture(testdir):
#     """Make sure that pytest accepts our fixture."""

#     # create a temporary pytest test module
#     testdir.makepyfile("""
#         def test_sth(bar):
#             assert bar == "europython2015"
#     """)

#     # run pytest with the following cmd args
#     result = testdir.runpytest(
#         '--foo=europython2015',
#         '-v'
#     )

#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_sth PASSED',
#     ])

#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0


# def test_help_message(testdir):
#     result = testdir.runpytest(
#         '--help',
#     )
#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         'ctdata_datatest:',
#         '*--foo=DEST_FOO*Set the value for the fixture "bar".',
#     ])


# def test_hello_ini_setting(testdir):
#     testdir.makeini("""
#         [pytest]
#         HELLO = world
#     """)

#     testdir.makepyfile("""
#         import pytest

#         @pytest.fixture
#         def hello(request):
#             return request.config.getini('HELLO')

#         def test_hello_world(hello):
#             assert hello == 'world'
#     """)

#     result = testdir.runpytest('-v')

#     # fnmatch_lines does an assertion internally
#     result.stdout.fnmatch_lines([
#         '*::test_hello_world PASSED',
#     ])

#     # make sure that that we get a '0' exit code for the testsuite
#     assert result.ret == 0
