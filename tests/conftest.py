import pytest
pytest_plugins = 'pytester'


@pytest.fixture
def datapackage(testdir):
    testdir.makefile('.json', datapackage="""
        {
            "name": "children-by-family-type",
            "title": "Children by Family Type",
            "description": "Children by Family Type reports the number and percent of children living in families by child age and by family type.",
            "sources": [{
                "name": "US Census American Community Survey",
                "web": ""
            }],
            "resources": [{
                "path": "data/data.csv",
                "format": "csv",
                "schema": {
                    "fields": [{
                        "name": "Town",
                        "type": "string",
                        "constraints": {
                            "enum": ["Town", "County", "Town/County", "District", "Other"]
                        },
                        "dimension": false
                    }, {
                        "name": "FIPS",
                        "type": "string",
                        "dimension": false
                    }, {
                        "name": "Year",
                        "type": "string",
                        "dimension": false
                    }, {
                        "name": "Grade",
                        "type": "string",
                        "dimension": true,
                        "constraints": {
                            "enum": ["K through 3", "4 through 8", "9 through 12", "All"]
                        }
                    }, {
                        "name": "English Language Learner",
                        "type": "string",
                        "dimension": true,
                        "constraints": {
                            "enum": ["English Language Learner", "All"]
                        }
                    }, {
                        "name": "Students with Disabilities",
                        "type": "string",
                        "dimension": true,
                        "constraints": {
                            "enum": ["With disabilities", "All"]
                        }
                    }, {
                        "name": "Measure Type",
                        "type": "string",
                        "dimension": true
                    }, {
                        "name": "Variable",
                        "type": "string",
                        "dimension": false
                    }, {
                        "name": "Value",
                        "type": "number",
                        "dimension": false
                    }]
                }
            }],
            "ckan_extras": {
                "full_description": {
                    "ckan_name": "Full Description",
                    "value": "Children by Family Type reports the number and percent of children living in families by child age and by family type.",
                    "type": "string"
                },
                "geography": {
                    "ckan_name": "Geography",
                    "value": "Town",
                    "type": "string",
                    "constraints": {
                        "enum": ["Town", "County", "Town/County", "District", "Other"]
                    }
                },
                "domain": {
                    "ckan_name": "Domain",
                    "value": "Demographics",
                    "type": "string"
                },
                "years_in_catalog": {
                    "ckan_name": "Years in Catalog",
                    "value": ["2016", "2015", "2014", "2013"],
                    "type": "array"
                }
            },
            "dimension_groups": [
                ["English Language Learner", "Grade"],
                ["Students with Disabilities"]
            ]
        }
    """)