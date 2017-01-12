import pytest

pytest_plugins = 'pytester'

@pytest.fixture
def datafile(testdir):
    testdir.makefile('.csv', data="""
    Town,FIPS,Year,Grade,English Language Learner,Students with Disabilities,Measure Type,Variable,Value
    Ansonia,"0901",2016,K through 3,English Language Learner,All,Number,Students,10
    Andover,"0902",2015,All,All,With disabilities,Number,Students,1
    """)


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
                "path": "data.csv",
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
                {
                    "English Language Learner": ["English Language Learner", "All"],
                    "Grade": ["K through 3", "4 through 8", "9 through 12", "All"]
                },
                {
                    "Students with Disabilities": ["With disabilities", "All"]
                }
            ],
            "spot_checks": [
              {
                "type": "$lookup",
                "filter": {
                  "Town": "Ansonia",
                  "Year": "2016",
                  "Grade": "K through 3",
                  "English Language Learner": "English Language Learner",
                  "Students with Disabilities": "All",
                  "Measure Type": "Number"
                },
                "expected": {
                  "type": "$match",
                  "number type": "int",
                  "value": 10
                }
              },
              {
                "type": "$lookup",
                "filter": {
                  "Town": "Andover",
                  "Year": "2015",
                  "Grade": "All",
                  "English Language Learner": "All",
                  "Students with Disabilities": "With disabilities",
                  "Measure Type": "Number"
                },
                "expected": {
                  "type": "$match",
                  "number type": "int",
                  "value": 1
                }
              }
            ]
        }
    """)


@pytest.fixture
def housing_datapackage(testdir):
    testdir.makefile('.json', datapackage="""
           {
                "name": "single-housing-units",
                "title": "Single Housing Units",
                "description": "Single Housing Units reports the number and percent of housing units that are single, detached units.",
                "sources": [{
                    "name": "US Census American Community Survey",
                    "web": ""
                }],
                "resources": [{
                    "path": "data.csv",
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
                            "name": "Unit Type",
                            "type": "string",
                            "dimension": true,
                            "constraints": {
                                "enum": ["Total", "Detached"]
                            }
                        }, {
                            "name": "Measure Type",
                            "type": "string",
                            "dimension": true,
                            "constraints": {
                                "enum": ["Number", "Percent"]
                            }
                        }, {
                            "name": "Variable",
                            "type": "string",
                            "dimension": false,
                            "constraints": {
                                "enum": ["Housing Units", "Margins of Error"]
                            }
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
                        "value": "Single Housing Units reports the number and percent of housing units that are single, detached units. A housing unit structure detached from any other house, that is, with open space on all four sides. Data is presented at the town, county, and state level. This data originates from the American Community Survey (ACS), table DP04.",
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
                        "value": ["2011-2015", "2010-2014"],
                        "type": "array"
                    }
                },
                "dimension_groups" : [
                    {
                        "Unit Type": ["Detached"],
                        "Measure Type": ["Number", "Percent"],
                        "Variable": ["Housing Units", "Margins of Error"]
                    },
                    {
                        "Unit Type": ["Total"],
                        "Measure Type": ["Number"],
                        "Variable": ["Housing Units", "Margins of Error"]
                    }
                ],
                "spot_checks": [{
                    "type": "$lookup",
                    "filter": {
                        "Town": "Connecticut",
                        "Year": "2011-2015",
                        "Unit Type": "Detached",
                        "Measure Type": "Percent",
                        "Variable": "Housing Units"
                    },
                    "expected": {
                        "type": "$match",
                        "number type": "float",
                        "value": 59.2
                    }
                }, {
                    "type": "$reduce",
                    "filter": [{
                        "Town": "Hartford",
                        "Year": "2011-2015",
                        "Unit Type": "Detached",
                        "Measure Type": "Number",
                        "Variable": "Housing Units"
                    }, {
                        "Town": "East Hartford",
                        "Year": "2011-2015",
                        "Unit Type": "Detached",
                        "Measure Type": "Number",
                        "Variable": "Housing Units"
                    }],
                    "expected": {
                        "type": "$match",
                        "number type": "int",
                        "value": 19107
                    }
                }, {
                    "type": "$percent",
                    "filter": {
                        "numerator": {
                            "Town": "Connecticut",
                            "Year": "2011-2015",
                            "Unit Type": "Detached",
                            "Measure Type": "Number",
                            "Variable": "Housing Units"
                        },
                        "denominator": {
                            "Town": "Connecticut",
                            "Year": "2011-2015",
                            "Unit Type": "Total",
                            "Measure Type": "Number",
                            "Variable": "Housing Units"
                        }
                    },
                    "expected": {
                        "type": "$lookup",
                        "number type": "float",
                        "value": {
                            "Town": "Connecticut",
                            "Year": "2011-2015",
                            "Unit Type": "Detached",
                            "Measure Type": "Percent",
                            "Variable": "Housing Units"
                        }
                    }
                }, {
                    "type": "$percent",
                    "filter": {
                        "numerator": {
                            "Town": "Connecticut",
                            "Year": "2011-2015",
                            "Unit Type": "Detached",
                            "Measure Type": "Number",
                            "Variable": "Housing Units"
                        },
                        "denominator": {
                            "Town": "Connecticut",
                            "Year": "2011-2015",
                            "Unit Type": "Total",
                            "Measure Type": "Number",
                            "Variable": "Housing Units"
                        }
                    },
                    "expected": {
                        "type": "$match",
                        "number type": "float",
                        "value": 59.2
                    }
                }]
            }
    """)


@pytest.fixture
def housing_datafile(testdir):
    testdir.makefile('.csv', data="""
    Town,FIPS,Year,Unit Type,Measure Type,Variable,Value
    Connecticut,"09",2011-2015,Total,Number,Housing Units,1491786
    Connecticut,"09",2011-2015,Total,Number,Margins of Error,313
    Connecticut,"09",2011-2015,Detached,Number,Housing Units,882941
    Connecticut,"09",2011-2015,Detached,Number,Margins of Error,3457
    Connecticut,"09",2011-2015,Detached,Percent,Housing Units,59.2
    Connecticut,"09",2011-2015,Detached,Percent,Margins of Error,0.2
    Connecticut,"09",2010-2014,Total,Number,Housing Units,1490381
    Connecticut,"09",2010-2014,Total,Number,Margins of Error,481
    Connecticut,"09",2010-2014,Detached,Number,Housing Units,882955
    Connecticut,"09",2010-2014,Detached,Number,Margins of Error,3612
    Connecticut,"09",2010-2014,Detached,Percent,Housing Units,59.2
    Connecticut,"09",2010-2014,Detached,Percent,Margins of Error,0.2
    Bethel,"0900104720",2011-2015,Total,Number,Housing Units,7540
    Bethel,"0900104720",2011-2015,Total,Number,Margins of Error,243
    Bethel,"0900104720",2011-2015,Detached,Number,Housing Units,5236
    Bethel,"0900104720",2011-2015,Detached,Number,Margins of Error,271
    Bethel,"0900104720",2011-2015,Detached,Percent,Housing Units,69.4
    Bethel,"0900104720",2011-2015,Detached,Percent,Margins of Error,3
    Bethel,"0900104720",2010-2014,Total,Number,Housing Units,7388
    Bethel,"0900104720",2010-2014,Total,Number,Margins of Error,248
    Bethel,"0900104720",2010-2014,Detached,Number,Housing Units,5076
    Bethel,"0900104720",2010-2014,Detached,Number,Margins of Error,287
    Bethel,"0900104720",2010-2014,Detached,Percent,Housing Units,68.7
    Bethel,"0900104720",2010-2014,Detached,Percent,Margins of Error,3
    Bridgeport,"0900108070",2011-2015,Total,Number,Housing Units,57889
    Bridgeport,"0900108070",2011-2015,Total,Number,Margins of Error,911
    Bridgeport,"0900108070",2011-2015,Detached,Number,Housing Units,14691
    Bridgeport,"0900108070",2011-2015,Detached,Number,Margins of Error,713
    Bridgeport,"0900108070",2011-2015,Detached,Percent,Housing Units,25.4
    Bridgeport,"0900108070",2011-2015,Detached,Percent,Margins of Error,1.2
    Bridgeport,"0900108070",2010-2014,Total,Number,Housing Units,57709
    Bridgeport,"0900108070",2010-2014,Total,Number,Margins of Error,944
    Bridgeport,"0900108070",2010-2014,Detached,Number,Housing Units,14708
    Bridgeport,"0900108070",2010-2014,Detached,Number,Margins of Error,582
    Bridgeport,"0900108070",2010-2014,Detached,Percent,Housing Units,25.5
    Bridgeport,"0900108070",2010-2014,Detached,Percent,Margins of Error,0.9
    Brookfield,"0900108980",2011-2015,Total,Number,Housing Units,6507
    Brookfield,"0900108980",2011-2015,Total,Number,Margins of Error,284
    Brookfield,"0900108980",2011-2015,Detached,Number,Housing Units,4946
    Brookfield,"0900108980",2011-2015,Detached,Number,Margins of Error,285
    Brookfield,"0900108980",2011-2015,Detached,Percent,Housing Units,76
    Brookfield,"0900108980",2011-2015,Detached,Percent,Margins of Error,2.8
    Brookfield,"0900108980",2010-2014,Total,Number,Housing Units,6553
    Brookfield,"0900108980",2010-2014,Total,Number,Margins of Error,237
    Brookfield,"0900108980",2010-2014,Detached,Number,Housing Units,5049
    Brookfield,"0900108980",2010-2014,Detached,Number,Margins of Error,258
    Brookfield,"0900108980",2010-2014,Detached,Percent,Housing Units,77
    Brookfield,"0900108980",2010-2014,Detached,Percent,Margins of Error,2.8
    Danbury,"0900118500",2011-2015,Total,Number,Housing Units,31716
    Danbury,"0900118500",2011-2015,Total,Number,Margins of Error,728
    Danbury,"0900118500",2011-2015,Detached,Number,Housing Units,13859
    Danbury,"0900118500",2011-2015,Detached,Number,Margins of Error,611
    Danbury,"0900118500",2011-2015,Detached,Percent,Housing Units,43.7
    Danbury,"0900118500",2011-2015,Detached,Percent,Margins of Error,1.7
    Danbury,"0900118500",2010-2014,Total,Number,Housing Units,32036
    Danbury,"0900118500",2010-2014,Total,Number,Margins of Error,693
    Danbury,"0900118500",2010-2014,Detached,Number,Housing Units,14068
    Danbury,"0900118500",2010-2014,Detached,Number,Margins of Error,564
    Danbury,"0900118500",2010-2014,Detached,Percent,Housing Units,43.9
    Danbury,"0900118500",2010-2014,Detached,Percent,Margins of Error,1.4
    Darien,"0900118850",2011-2015,Total,Number,Housing Units,6940
    Darien,"0900118850",2011-2015,Total,Number,Margins of Error,144
    Darien,"0900118850",2011-2015,Detached,Number,Housing Units,6283
    Darien,"0900118850",2011-2015,Detached,Number,Margins of Error,181
    Darien,"0900118850",2011-2015,Detached,Percent,Housing Units,90.5
    Darien,"0900118850",2011-2015,Detached,Percent,Margins of Error,1.7
    Darien,"0900118850",2010-2014,Total,Number,Housing Units,7029
    Darien,"0900118850",2010-2014,Total,Number,Margins of Error,226
    Darien,"0900118850",2010-2014,Detached,Number,Housing Units,6424
    Darien,"0900118850",2010-2014,Detached,Number,Margins of Error,223
    Darien,"0900118850",2010-2014,Detached,Percent,Housing Units,91.4
    Darien,"0900118850",2010-2014,Detached,Percent,Margins of Error,1.6
    Easton,"0900123890",2011-2015,Total,Number,Housing Units,2757
    Easton,"0900123890",2011-2015,Total,Number,Margins of Error,120
    Easton,"0900123890",2011-2015,Detached,Number,Housing Units,2675
    Easton,"0900123890",2011-2015,Detached,Number,Margins of Error,116
    Easton,"0900123890",2011-2015,Detached,Percent,Housing Units,97
    Easton,"0900123890",2011-2015,Detached,Percent,Margins of Error,2.1
    Easton,"0900123890",2010-2014,Total,Number,Housing Units,2718
    Easton,"0900123890",2010-2014,Total,Number,Margins of Error,137
    Easton,"0900123890",2010-2014,Detached,Number,Housing Units,2635
    Easton,"0900123890",2010-2014,Detached,Number,Margins of Error,130
    Easton,"0900123890",2010-2014,Detached,Percent,Housing Units,96.9
    Easton,"0900123890",2010-2014,Detached,Percent,Margins of Error,2
    Fairfield,"0900126620",2011-2015,Total,Number,Housing Units,21359
    Fairfield,"0900126620",2011-2015,Total,Number,Margins of Error,364
    Fairfield,"0900126620",2011-2015,Detached,Number,Housing Units,17089
    Fairfield,"0900126620",2011-2015,Detached,Number,Margins of Error,374
    Fairfield,"0900126620",2011-2015,Detached,Percent,Housing Units,80
    Fairfield,"0900126620",2011-2015,Detached,Percent,Margins of Error,1.2
    Fairfield,"0900126620",2010-2014,Total,Number,Housing Units,21334
    Fairfield,"0900126620",2010-2014,Total,Number,Margins of Error,415
    Fairfield,"0900126620",2010-2014,Detached,Number,Housing Units,16914
    Fairfield,"0900126620",2010-2014,Detached,Number,Margins of Error,425
    Fairfield,"0900126620",2010-2014,Detached,Percent,Housing Units,79.3
    Fairfield,"0900126620",2010-2014,Detached,Percent,Margins of Error,1.4
    Greenwich,"0900133620",2011-2015,Total,Number,Housing Units,24242
    Greenwich,"0900133620",2011-2015,Total,Number,Margins of Error,535
    Greenwich,"0900133620",2011-2015,Detached,Number,Housing Units,15418
    Greenwich,"0900133620",2011-2015,Detached,Number,Margins of Error,462
    Greenwich,"0900133620",2011-2015,Detached,Percent,Housing Units,63.6
    Greenwich,"0900133620",2011-2015,Detached,Percent,Margins of Error,1.5
    Greenwich,"0900133620",2010-2014,Total,Number,Housing Units,24027
    Greenwich,"0900133620",2010-2014,Total,Number,Margins of Error,466
    Greenwich,"0900133620",2010-2014,Detached,Number,Housing Units,15464
    Greenwich,"0900133620",2010-2014,Detached,Number,Margins of Error,466
    Greenwich,"0900133620",2010-2014,Detached,Percent,Housing Units,64.4
    Greenwich,"0900133620",2010-2014,Detached,Percent,Margins of Error,1.5
    Monroe,"0900148620",2011-2015,Total,Number,Housing Units,7047
    Monroe,"0900148620",2011-2015,Total,Number,Margins of Error,246
    Monroe,"0900148620",2011-2015,Detached,Number,Housing Units,5974
    Monroe,"0900148620",2011-2015,Detached,Number,Margins of Error,267
    Monroe,"0900148620",2011-2015,Detached,Percent,Housing Units,84.8
    Monroe,"0900148620",2011-2015,Detached,Percent,Margins of Error,2.7
    Monroe,"0900148620",2010-2014,Total,Number,Housing Units,6890
    Monroe,"0900148620",2010-2014,Total,Number,Margins of Error,250
    Monroe,"0900148620",2010-2014,Detached,Number,Housing Units,5920
    Monroe,"0900148620",2010-2014,Detached,Number,Margins of Error,287
    Monroe,"0900148620",2010-2014,Detached,Percent,Housing Units,85.9
    Monroe,"0900148620",2010-2014,Detached,Percent,Margins of Error,2.4
    New Canaan,"0900150580",2011-2015,Total,Number,Housing Units,7310
    New Canaan,"0900150580",2011-2015,Total,Number,Margins of Error,211
    New Canaan,"0900150580",2011-2015,Detached,Number,Housing Units,5334
    New Canaan,"0900150580",2011-2015,Detached,Number,Margins of Error,248
    New Canaan,"0900150580",2011-2015,Detached,Percent,Housing Units,73
    New Canaan,"0900150580",2011-2015,Detached,Percent,Margins of Error,2.4
    New Canaan,"0900150580",2010-2014,Total,Number,Housing Units,7305
    New Canaan,"0900150580",2010-2014,Total,Number,Margins of Error,233
    New Canaan,"0900150580",2010-2014,Detached,Number,Housing Units,5390
    New Canaan,"0900150580",2010-2014,Detached,Number,Margins of Error,238
    New Canaan,"0900150580",2010-2014,Detached,Percent,Housing Units,73.8
    New Canaan,"0900150580",2010-2014,Detached,Percent,Margins of Error,2.1
    New Fairfield,"0900150860",2011-2015,Total,Number,Housing Units,5863
    New Fairfield,"0900150860",2011-2015,Total,Number,Margins of Error,205
    New Fairfield,"0900150860",2011-2015,Detached,Number,Housing Units,5695
    New Fairfield,"0900150860",2011-2015,Detached,Number,Margins of Error,189
    New Fairfield,"0900150860",2011-2015,Detached,Percent,Housing Units,97.1
    New Fairfield,"0900150860",2011-2015,Detached,Percent,Margins of Error,1
    New Fairfield,"0900150860",2010-2014,Total,Number,Housing Units,5820
    New Fairfield,"0900150860",2010-2014,Total,Number,Margins of Error,215
    New Fairfield,"0900150860",2010-2014,Detached,Number,Housing Units,5597
    New Fairfield,"0900150860",2010-2014,Detached,Number,Margins of Error,207
    New Fairfield,"0900150860",2010-2014,Detached,Percent,Housing Units,96.2
    New Fairfield,"0900150860",2010-2014,Detached,Percent,Margins of Error,1.4
    Newtown,"0900152980",2011-2015,Total,Number,Housing Units,10167
    Newtown,"0900152980",2011-2015,Total,Number,Margins of Error,362
    Newtown,"0900152980",2011-2015,Detached,Number,Housing Units,8839
    Newtown,"0900152980",2011-2015,Detached,Number,Margins of Error,326
    Newtown,"0900152980",2011-2015,Detached,Percent,Housing Units,86.9
    Newtown,"0900152980",2011-2015,Detached,Percent,Margins of Error,2
    Newtown,"0900152980",2010-2014,Total,Number,Housing Units,10163
    Newtown,"0900152980",2010-2014,Total,Number,Margins of Error,328
    Newtown,"0900152980",2010-2014,Detached,Number,Housing Units,9003
    Newtown,"0900152980",2010-2014,Detached,Number,Margins of Error,291
    Newtown,"0900152980",2010-2014,Detached,Percent,Housing Units,88.6
    Newtown,"0900152980",2010-2014,Detached,Percent,Margins of Error,2
    Norwalk,"0900156060",2011-2015,Total,Number,Housing Units,35800
    Norwalk,"0900156060",2011-2015,Total,Number,Margins of Error,682
    Norwalk,"0900156060",2011-2015,Detached,Number,Housing Units,17408
    Norwalk,"0900156060",2011-2015,Detached,Number,Margins of Error,539
    Norwalk,"0900156060",2011-2015,Detached,Percent,Housing Units,48.6
    Norwalk,"0900156060",2011-2015,Detached,Percent,Margins of Error,1.4
    Norwalk,"0900156060",2010-2014,Total,Number,Housing Units,37141
    Norwalk,"0900156060",2010-2014,Total,Number,Margins of Error,787
    Norwalk,"0900156060",2010-2014,Detached,Number,Housing Units,17619
    Norwalk,"0900156060",2010-2014,Detached,Number,Margins of Error,640
    Norwalk,"0900156060",2010-2014,Detached,Percent,Housing Units,47.4
    Norwalk,"0900156060",2010-2014,Detached,Percent,Margins of Error,1.3
    Redding,"0900163480",2011-2015,Total,Number,Housing Units,3963
    Redding,"0900163480",2011-2015,Total,Number,Margins of Error,183
    Redding,"0900163480",2011-2015,Detached,Number,Housing Units,3398
    Redding,"0900163480",2011-2015,Detached,Number,Margins of Error,181
    Redding,"0900163480",2011-2015,Detached,Percent,Housing Units,85.7
    Redding,"0900163480",2011-2015,Detached,Percent,Margins of Error,2.6
    Redding,"0900163480",2010-2014,Total,Number,Housing Units,3932
    Redding,"0900163480",2010-2014,Total,Number,Margins of Error,152
    Redding,"0900163480",2010-2014,Detached,Number,Housing Units,3269
    Redding,"0900163480",2010-2014,Detached,Number,Margins of Error,181
    Redding,"0900163480",2010-2014,Detached,Percent,Housing Units,83.1
    Redding,"0900163480",2010-2014,Detached,Percent,Margins of Error,2.9
    Ridgefield,"0900163970",2011-2015,Total,Number,Housing Units,9460
    Ridgefield,"0900163970",2011-2015,Total,Number,Margins of Error,270
    Ridgefield,"0900163970",2011-2015,Detached,Number,Housing Units,7661
    Ridgefield,"0900163970",2011-2015,Detached,Number,Margins of Error,251
    Ridgefield,"0900163970",2011-2015,Detached,Percent,Housing Units,81
    Ridgefield,"0900163970",2011-2015,Detached,Percent,Margins of Error,1.9
    Ridgefield,"0900163970",2010-2014,Total,Number,Housing Units,9320
    Ridgefield,"0900163970",2010-2014,Total,Number,Margins of Error,241
    Ridgefield,"0900163970",2010-2014,Detached,Number,Housing Units,7599
    Ridgefield,"0900163970",2010-2014,Detached,Number,Margins of Error,262
    Ridgefield,"0900163970",2010-2014,Detached,Percent,Housing Units,81.5
    Ridgefield,"0900163970",2010-2014,Detached,Percent,Margins of Error,1.8
    Shelton,"0900168170",2011-2015,Total,Number,Housing Units,16471
    Shelton,"0900168170",2011-2015,Total,Number,Margins of Error,352
    Shelton,"0900168170",2011-2015,Detached,Number,Housing Units,10890
    Shelton,"0900168170",2011-2015,Detached,Number,Margins of Error,430
    Shelton,"0900168170",2011-2015,Detached,Percent,Housing Units,66.1
    Shelton,"0900168170",2011-2015,Detached,Percent,Margins of Error,2.1
    Shelton,"0900168170",2010-2014,Total,Number,Housing Units,16200
    Shelton,"0900168170",2010-2014,Total,Number,Margins of Error,307
    Shelton,"0900168170",2010-2014,Detached,Number,Housing Units,10614
    Shelton,"0900168170",2010-2014,Detached,Number,Margins of Error,378
    Shelton,"0900168170",2010-2014,Detached,Percent,Housing Units,65.5
    Shelton,"0900168170",2010-2014,Detached,Percent,Margins of Error,1.8
    Sherman,"0900168310",2011-2015,Total,Number,Housing Units,1792
    Sherman,"0900168310",2011-2015,Total,Number,Margins of Error,119
    Sherman,"0900168310",2011-2015,Detached,Number,Housing Units,1747
    Sherman,"0900168310",2011-2015,Detached,Number,Margins of Error,120
    Sherman,"0900168310",2011-2015,Detached,Percent,Housing Units,97.5
    Sherman,"0900168310",2011-2015,Detached,Percent,Margins of Error,1.9
    Sherman,"0900168310",2010-2014,Total,Number,Housing Units,1771
    Sherman,"0900168310",2010-2014,Total,Number,Margins of Error,101
    Sherman,"0900168310",2010-2014,Detached,Number,Housing Units,1722
    Sherman,"0900168310",2010-2014,Detached,Number,Margins of Error,108
    Sherman,"0900168310",2010-2014,Detached,Percent,Housing Units,97.2
    Sherman,"0900168310",2010-2014,Detached,Percent,Margins of Error,2.6
    Stamford,"0900173070",2011-2015,Total,Number,Housing Units,51165
    Stamford,"0900173070",2011-2015,Total,Number,Margins of Error,917
    Stamford,"0900173070",2011-2015,Detached,Number,Housing Units",20116
    Stamford,"0900173070",2011-2015,Detached,Number,Margins of Error,591
    Stamford,"0900173070",2011-2015,Detached,Percent,Housing Units,39.3
    Stamford,"0900173070",2011-2015,Detached,Percent,Margins of Error,0.9
    Stamford,"0900173070",2010-2014,Total,Number,Housing Units,50431
    Stamford,"0900173070",2010-2014,Total,Number,Margins of Error,1022
    Stamford,"0900173070",2010-2014,Detached,Number,Housing Units,19716
    Stamford,"0900173070",2010-2014,Detached,Number,Margins of Error,621
    Stamford,"0900173070",2010-2014,Detached,Percent,Housing Units,39.1
    Stamford,"0900173070",2010-2014,Detached,Percent,Margins of Error,0.9
    Stratford,"0900174190",2011-2015,Total,Number,Housing Units,22264
    Stratford,"0900174190",2011-2015,Total,Number,Margins of Error,455
    Stratford,"0900174190",2011-2015,Detached,Number,Housing Units,14435
    Stratford,"0900174190",2011-2015,Detached,Number,Margins of Error,452
    Stratford,"0900174190",2011-2015,Detached,Percent,Housing Units,64.8
    Stratford,"0900174190",2011-2015,Detached,Percent,Margins of Error,1.7
    Stratford,"0900174190",2010-2014,Total,Number,Housing Units,21736
    Stratford,"0900174190",2010-2014,Total,Number,Margins of Error,365
    Stratford,"0900174190",2010-2014,Detached,Number,Housing Units,14283
    Stratford,"0900174190",2010-2014,Detached,Number,Margins of Error,449
    Stratford,"0900174190",2010-2014,Detached,Percent,Housing Units,65.7
    Stratford,"0900174190",2010-2014,Detached,Percent,Margins of Error,1.6
    Trumbull,"0900177200",2011-2015,Total,Number,Housing Units,12542
    Trumbull,"0900177200",2011-2015,Total,Number,Margins of Error,296
    Trumbull,"0900177200",2011-2015,Detached,Number,Housing Units,10953
    Trumbull,"0900177200",2011-2015,Detached,Number,Margins of Error,303
    Trumbull,"0900177200",2011-2015,Detached,Percent,Housing Units,87.3
    Trumbull,"0900177200",2011-2015,Detached,Percent,Margins of Error,1.4
    Trumbull,"0900177200",2010-2014,Total,Number,Housing Units,12584
    Trumbull,"0900177200",2010-2014,Total,Number,Margins of Error,274
    Trumbull,"0900177200",2010-2014,Detached,Number,Housing Units,11022
    Trumbull,"0900177200",2010-2014,Detached,Number,Margins of Error,305
    Trumbull,"0900177200",2010-2014,Detached,Percent,Housing Units,87.6
    Trumbull,"0900177200",2010-2014,Detached,Percent,Margins of Error,1.4
    Weston,"0900183430",2011-2015,Total,Number,Housing Units,3801
    Weston,"0900183430",2011-2015,Total,Number,Margins of Error,198
    Weston,"0900183430",2011-2015,Detached,Number,Housing Units,3714
    Weston,"0900183430",2011-2015,Detached,Number,Margins of Error,206
    Weston,"0900183430",2011-2015,Detached,Percent,Housing Units,97.7
    Weston,"0900183430",2011-2015,Detached,Percent,Margins of Error,1.2
    Weston,"0900183430",2010-2014,Total,Number,Housing Units,3743
    Weston,"0900183430",2010-2014,Total,Number,Margins of Error,165
    Weston,"0900183430",2010-2014,Detached,Number,Housing Units,3644
    Weston,"0900183430",2010-2014,Detached,Number,Margins of Error,176
    Weston,"0900183430",2010-2014,Detached,Percent,Housing Units,97.4
    Weston,"0900183430",2010-2014,Detached,Percent,Margins of Error,1.4
    Westport,"0900183500",2011-2015,Total,Number,Housing Units,10611
    Westport,"0900183500",2011-2015,Total,Number,Margins of Error,338
    Westport,"0900183500",2011-2015,Detached,Number,Housing Units,9180
    Westport,"0900183500",2011-2015,Detached,Number,Margins of Error,348
    Westport,"0900183500",2011-2015,Detached,Percent,Housing Units,86.5
    Westport,"0900183500",2011-2015,Detached,Percent,Margins of Error,1.7
    Westport,"0900183500",2010-2014,Total,Number,Housing Units,10413
    Westport,"0900183500",2010-2014,Total,Number,Margins of Error,299
    Westport,"0900183500",2010-2014,Detached,Number,Housing Units,9146
    Westport,"0900183500",2010-2014,Detached,Number,Margins of Error,316
    Westport,"0900183500",2010-2014,Detached,Percent,Housing Units,87.8
    Westport,"0900183500",2010-2014,Detached,Percent,Margins of Error,1.6
    Wilton,"0900186370",2011-2015,Total,Number,Housing Units,6350
    Wilton,"0900186370",2011-2015,Total,Number,Margins of Error,198
    Wilton,"0900186370",2011-2015,Detached,Number,Housing Units,5390
    Wilton,"0900186370",2011-2015,Detached,Number,Margins of Error,200
    Wilton,"0900186370",2011-2015,Detached,Percent,Housing Units,84.9
    Wilton,"0900186370",2011-2015,Detached,Percent,Margins of Error,1.9
    Wilton,"0900186370",2010-2014,Total,Number,Housing Units,6373
    Wilton,"0900186370",2010-2014,Total,Number,Margins of Error,199
    Wilton,"0900186370",2010-2014,Detached,Number,Housing Units,5452
    Wilton,"0900186370",2010-2014,Detached,Number,Margins of Error,193
    Wilton,"0900186370",2010-2014,Detached,Percent,Housing Units,85.5
    Wilton,"0900186370",2010-2014,Detached,Percent,Margins of Error,2.3
    Avon,"0900302060",2011-2015,Total,Number,Housing Units,7342
    Avon,"0900302060",2011-2015,Total,Number,Margins of Error,240
    Avon,"0900302060",2011-2015,Detached,Number,Housing Units,5201
    Avon,"0900302060",2011-2015,Detached,Number,Margins of Error,274
    Avon,"0900302060",2011-2015,Detached,Percent,Housing Units,70.8
    Avon,"0900302060",2011-2015,Detached,Percent,Margins of Error,2.7
    Avon,"0900302060",2010-2014,Total,Number,Housing Units,7436
    Avon,"0900302060",2010-2014,Total,Number,Margins of Error,208
    Avon,"0900302060",2010-2014,Detached,Number,Housing Units,5280
    Avon,"0900302060",2010-2014,Detached,Number,Margins of Error,245
    Avon,"0900302060",2010-2014,Detached,Percent,Housing Units,71
    Avon,"0900302060",2010-2014,Detached,Percent,Margins of Error,2.6
    Berlin,"0900304300",2011-2015,Total,Number,Housing Units,8333
    Berlin,"0900304300",2011-2015,Total,Number,Margins of Error,258
    Berlin,"0900304300",2011-2015,Detached,Number,Housing Units,6309
    Berlin,"0900304300",2011-2015,Detached,Number,Margins of Error,367
    Berlin,"0900304300",2011-2015,Detached,Percent,Housing Units,75.7
    Berlin,"0900304300",2011-2015,Detached,Percent,Margins of Error,3.1
    Berlin,"0900304300",2010-2014,Total,Number,Housing Units,8218
    Berlin,"0900304300",2010-2014,Total,Number,Margins of Error,248
    Berlin,"0900304300",2010-2014,Detached,Number,Housing Units,6271
    Berlin,"0900304300",2010-2014,Detached,Number,Margins of Error,301
    Berlin,"0900304300",2010-2014,Detached,Percent,Housing Units,76.3
    Berlin,"0900304300",2010-2014,Detached,Percent,Margins of Error,2.7
    Bloomfield,"0900305910",2011-2015,Total,Number,Housing Units,8823
    Bloomfield,"0900305910",2011-2015,Total,Number,Margins of Error,370
    Bloomfield,"0900305910",2011-2015,Detached,Number,Housing Units,5867
    Bloomfield,"0900305910",2011-2015,Detached,Number,Margins of Error,390
    Bloomfield,"0900305910",2011-2015,Detached,Percent,Housing Units,66.5
    Bloomfield,"0900305910",2011-2015,Detached,Percent,Margins of Error,3.4
    Bloomfield,"0900305910",2010-2014,Total,Number,Housing Units,8746
    Bloomfield,"0900305910",2010-2014,Total,Number,Margins of Error,323
    Bloomfield,"0900305910",2010-2014,Detached,Number,Housing Units,5793
    Bloomfield,"0900305910",2010-2014,Detached,Number,Margins of Error,351
    Bloomfield,"0900305910",2010-2014,Detached,Percent,Housing Units,66.2
    Bloomfield,"0900305910",2010-2014,Detached,Percent,Margins of Error,3.3
    Bristol,"0900308490",2011-2015,Total,Number,Housing Units,26953
    Bristol,"0900308490",2011-2015,Total,Number,Margins of Error,561
    Bristol,"0900308490",2011-2015,Detached,Number,Housing Units,15113
    Bristol,"0900308490",2011-2015,Detached,Number,Margins of Error,529
    Bristol,"0900308490",2011-2015,Detached,Percent,Housing Units,56.1
    Bristol,"0900308490",2011-2015,Detached,Percent,Margins of Error,1.6
    Bristol,"0900308490",2010-2014,Total,Number,Housing Units,27131
    Bristol,"0900308490",2010-2014,Total,Number,Margins of Error,693
    Bristol,"0900308490",2010-2014,Detached,Number,Housing Units,15524
    Bristol,"0900308490",2010-2014,Detached,Number,Margins of Error,507
    Bristol,"0900308490",2010-2014,Detached,Percent,Housing Units,57.2
    Bristol,"0900308490",2010-2014,Detached,Percent,Margins of Error,1.5
    Burlington,"0900310100",2011-2015,Total,Number,Housing Units,3535
    Burlington,"0900310100",2011-2015,Total,Number,Margins of Error,139
    Burlington,"0900310100",2011-2015,Detached,Number,Housing Units,3319
    Burlington,"0900310100",2011-2015,Detached,Number,Margins of Error,164
    Burlington,"0900310100",2011-2015,Detached,Percent,Housing Units,93.9
    Burlington,"0900310100",2011-2015,Detached,Percent,Margins of Error,2.1
    Burlington,"0900310100",2010-2014,Total,Number,Housing Units,3541
    Burlington,"0900310100",2010-2014,Total,Number,Margins of Error,175
    Burlington,"0900310100",2010-2014,Detached,Number,Housing Units,3372
    Burlington,"0900310100",2010-2014,Detached,Number,Margins of Error,177
    Burlington,"0900310100",2010-2014,Detached,Percent,Housing Units,95.2
    Burlington,"0900310100",2010-2014,Detached,Percent,Margins of Error,2
    Canton,"0900312270",2011-2015,Total,Number,Housing Units,4321
    Canton,"0900312270",2011-2015,Total,Number,Margins of Error,189
    Canton,"0900312270",2011-2015,Detached,Number,Housing Units,3104
    Canton,"0900312270",2011-2015,Detached,Number,Margins of Error,208
    Canton,"0900312270",2011-2015,Detached,Percent,Housing Units,71.8
    Canton,"0900312270",2011-2015,Detached,Percent,Margins of Error,4.3
    Canton,"0900312270",2010-2014,Total,Number,Housing Units,4358
    Canton,"0900312270",2010-2014,Total,Number,Margins of Error,165
    Canton,"0900312270",2010-2014,Detached,Number,Housing Units,3216
    Canton,"0900312270",2010-2014,Detached,Number,Margins of Error,218
    Canton,"0900312270",2010-2014,Detached,Percent,Housing Units,73.8
    Canton,"0900312270",2010-2014,Detached,Percent,Margins of Error,4
    East Granby,"0900322070",2011-2015,Total,Number,Housing Units,2198
    East Granby,"0900322070",2011-2015,Total,Number,Margins of Error,98
    East Granby,"0900322070",2011-2015,Detached,Number,Housing Units,1725
    East Granby,"0900322070",2011-2015,Detached,Number,Margins of Error,117
    East Granby,"0900322070",2011-2015,Detached,Percent,Housing Units,78.5
    East Granby,"0900322070",2011-2015,Detached,Percent,Margins of Error,5.2
    East Granby,"0900322070",2010-2014,Total,Number,Housing Units,2179
    East Granby,"0900322070",2010-2014,Total,Number,Margins of Error,99
    East Granby,"0900322070",2010-2014,Detached,Number,Housing Units,1702
    East Granby,"0900322070",2010-2014,Detached,Number,Margins of Error,131
    East Granby,"0900322070",2010-2014,Detached,Percent,Housing Units,78.1
    East Granby,"0900322070",2010-2014,Detached,Percent,Margins of Error,5.8
    East Hartford,"0900322630",2011-2015,Total,Number,Housing Units,22116
    East Hartford,"0900322630",2011-2015,Total,Number,Margins of Error,601
    East Hartford,"0900322630",2011-2015,Detached,Number,Housing Units,11247
    East Hartford,"0900322630",2011-2015,Detached,Number,Margins of Error,457
    East Hartford,"0900322630",2011-2015,Detached,Percent,Housing Units,50.9
    East Hartford,"0900322630",2011-2015,Detached,Percent,Margins of Error,1.6
    East Hartford,"0900322630",2010-2014,Total,Number,Housing Units,21731
    East Hartford,"0900322630",2010-2014,Total,Number,Margins of Error,542
    East Hartford,"0900322630",2010-2014,Detached,Number,Housing Units,11283
    East Hartford,"0900322630",2010-2014,Detached,Number,Margins of Error,428
    East Hartford,"0900322630",2010-2014,Detached,Percent,Housing Units,51.9
    East Hartford,"0900322630",2010-2014,Detached,Percent,Margins of Error,1.5
    East Windsor,"0900324800",2011-2015,Total,Number,Housing Units,4691
    East Windsor,"0900324800",2011-2015,Total,Number,Margins of Error,289
    East Windsor,"0900324800",2011-2015,Detached,Number,Housing Units,2705
    East Windsor,"0900324800",2011-2015,Detached,Number,Margins of Error,262
    East Windsor,"0900324800",2011-2015,Detached,Percent,Housing Units,57.7
    East Windsor,"0900324800",2011-2015,Detached,Percent,Margins of Error,4.3
    East Windsor,"0900324800",2010-2014,Total,Number,Housing Units,4870
    East Windsor,"0900324800",2010-2014,Total,Number,Margins of Error,307
    East Windsor,"0900324800",2010-2014,Detached,Number,Housing Units,2731
    East Windsor,"0900324800",2010-2014,Detached,Number,Margins of Error,248
    East Windsor,"0900324800",2010-2014,Detached,Percent,Housing Units,56.1
    East Windsor,"0900324800",2010-2014,Detached,Percent,Margins of Error,4.4
    Enfield,"0900325990",2011-2015,Total,Number,Housing Units,17446
    Enfield,"0900325990",2011-2015,Total,Number,Margins of Error,474
    Enfield,"0900325990",2011-2015,Detached,Number,Housing Units,12024
    Enfield,"0900325990",2011-2015,Detached,Number,Margins of Error,475
    Enfield,"0900325990",2011-2015,Detached,Percent,Housing Units,68.9
    Enfield,"0900325990",2011-2015,Detached,Percent,Margins of Error,1.6
    Enfield,"0900325990",2010-2014,Total,Number,Housing Units,17302
    Enfield,"0900325990",2010-2014,Total,Number,Margins of Error,469
    Enfield,"0900325990",2010-2014,Detached,Number,Housing Units,11878
    Enfield,"0900325990",2010-2014,Detached,Number,Margins of Error,427
    Enfield,"0900325990",2010-2014,Detached,Percent,Housing Units,68.7
    Enfield,"0900325990",2010-2014,Detached,Percent,Margins of Error,1.7
    Farmington,"0900327600",2011-2015,Total,Number,Housing Units,11052
    Farmington,"0900327600",2011-2015,Total,Number,Margins of Error,226
    Farmington,"0900327600",2011-2015,Detached,Number,Housing Units,6586
    Farmington,"0900327600",2011-2015,Detached,Number,Margins of Error,317
    Farmington,"0900327600",2011-2015,Detached,Percent,Housing Units,59.6
    Farmington,"0900327600",2011-2015,Detached,Percent,Margins of Error,2.3
    Farmington,"0900327600",2010-2014,Total,Number,Housing Units,11072
    Farmington,"0900327600",2010-2014,Total,Number,Margins of Error,284
    Farmington,"0900327600",2010-2014,Detached,Number,Housing Units,6781
    Farmington,"0900327600",2010-2014,Detached,Number,Margins of Error,269
    Farmington,"0900327600",2010-2014,Detached,Percent,Housing Units,61.2
    Farmington,"0900327600",2010-2014,Detached,Percent,Margins of Error,2.1
    Glastonbury,"0900331240",2011-2015,Total,Number,Housing Units,13722
    Glastonbury,"0900331240",2011-2015,Total,Number,Margins of Error,300
    Glastonbury,"0900331240",2011-2015,Detached,Number,Housing Units,10052
    Glastonbury,"0900331240",2011-2015,Detached,Number,Margins of Error,316
    Glastonbury,"0900331240",2011-2015,Detached,Percent,Housing Units,73.3
    Glastonbury,"0900331240",2011-2015,Detached,Percent,Margins of Error,1.8
    Glastonbury,"0900331240",2010-2014,Total,Number,Housing Units,13665
    Glastonbury,"0900331240",2010-2014,Total,Number,Margins of Error,271
    Glastonbury,"0900331240",2010-2014,Detached,Number,Housing Units,10058
    Glastonbury,"0900331240",2010-2014,Detached,Number,Margins of Error,298
    Glastonbury,"0900331240",2010-2014,Detached,Percent,Housing Units,73.6
    Glastonbury,"0900331240",2010-2014,Detached,Percent,Margins of Error,1.9
    Granby,"0900332640",2011-2015,Total,Number,Housing Units,4597
    Granby,"0900332640",2011-2015,Total,Number,Margins of Error,175
    Granby,"0900332640",2011-2015,Detached,Number,Housing Units,4104
    Granby,"0900332640",2011-2015,Detached,Number,Margins of Error,188
    Granby,"0900332640",2011-2015,Detached,Percent,Housing Units,89.3
    Granby,"0900332640",2011-2015,Detached,Percent,Margins of Error,2.6
    Granby,"0900332640",2010-2014,Total,Number,Housing Units,4689
    Granby,"0900332640",2010-2014,Total,Number,Margins of Error,195
    Granby,"0900332640",2010-2014,Detached,Number,Housing Units,4129
    Granby,"0900332640",2010-2014,Detached,Number,Margins of Error,177
    Granby,"0900332640",2010-2014,Detached,Percent,Housing Units,88.1
    Granby,"0900332640",2010-2014,Detached,Percent,Margins of Error,2.7
    Hartford,"0900337070",2011-2015,Total,Number,Housing Units,52737
    Hartford,"0900337070",2011-2015,Total,Number,Margins of Error,845
    Hartford,"0900337070",2011-2015,Detached,Number,Housing Units,7860
    Hartford,"0900337070",2011-2015,Detached,Number,Margins of Error,396
    Hartford,"0900337070",2011-2015,Detached,Percent,Housing Units,14.9
    Hartford,"0900337070",2011-2015,Detached,Percent,Margins of Error,0.7
    Hartford,"0900337070",2010-2014,Total,Number,Housing Units,53644
    Hartford,"0900337070",2010-2014,Total,Number,Margins of Error,1003
    Hartford,"0900337070",2010-2014,Detached,Number,Housing Units,8198
    Hartford,"0900337070",2010-2014,Detached,Number,Margins of Error,452
    Hartford,"0900337070",2010-2014,Detached,Percent,Housing Units,15.3
    Hartford,"0900337070",2010-2014,Detached,Percent,Margins of Error,0.8
    Hartland,"0900337140",2011-2015,Total,Number,Housing Units,832
    Hartland,"0900337140",2011-2015,Total,Number,Margins of Error,49
    Hartland,"0900337140",2011-2015,Detached,Number,Housing Units,798
    Hartland,"0900337140",2011-2015,Detached,Number,Margins of Error,52
    Hartland,"0900337140",2011-2015,Detached,Percent,Housing Units,95.9
    Hartland,"0900337140",2011-2015,Detached,Percent,Margins of Error,2.8
    Hartland,"0900337140",2010-2014,Total,Number,Housing Units,824
    Hartland,"0900337140",2010-2014,Total,Number,Margins of Error,44
    Hartland,"0900337140",2010-2014,Detached,Number,Housing Units,784
    Hartland,"0900337140",2010-2014,Detached,Number,Margins of Error,45
    Hartland,"0900337140",2010-2014,Detached,Percent,Housing Units,95.1
    Hartland,"0900337140",2010-2014,Detached,Percent,Margins of Error,2.6
    Manchester,"0900344700",2011-2015,Total,Number,Housing Units,25456
    Manchester,"0900344700",2011-2015,Total,Number,Margins of Error,588
    Manchester,"0900344700",2011-2015,Detached,Number,Housing Units,11735
    Manchester,"0900344700",2011-2015,Detached,Number,Margins of Error,477
    Manchester,"0900344700",2011-2015,Detached,Percent,Housing Units,46.1
    Manchester,"0900344700",2011-2015,Detached,Percent,Margins of Error,1.6
    Manchester,"0900344700",2010-2014,Total,Number,Housing Units,25260
    Manchester,"0900344700",2010-2014,Total,Number,Margins of Error,493
    Manchester,"0900344700",2010-2014,Detached,Number,Housing Units,11910
    Manchester,"0900344700",2010-2014,Detached,Number,Margins of Error,338
    Manchester,"0900344700",2010-2014,Detached,Percent,Housing Units,47.1
    Manchester,"0900344700",2010-2014,Detached,Percent,Margins of Error,1.2
    Marlborough,"0900345820",2011-2015,Total,Number,Housing Units,2289
    Marlborough,"0900345820",2011-2015,Total,Number,Margins of Error,144
    Marlborough,"0900345820",2011-2015,Detached,Number,Housing Units,2052
    Marlborough,"0900345820",2011-2015,Detached,Number,Margins of Error,129
    Marlborough,"0900345820",2011-2015,Detached,Percent,Housing Units,89.6
    Marlborough,"0900345820",2011-2015,Detached,Percent,Margins of Error,4.3
    Marlborough,"0900345820",2010-2014,Total,Number,Housing Units,2289
    Marlborough,"0900345820",2010-2014,Total,Number,Margins of Error,130
    Marlborough,"0900345820",2010-2014,Detached,Number,Housing Units,2102
    Marlborough,"0900345820",2010-2014,Detached,Number,Margins of Error,154
    Marlborough,"0900345820",2010-2014,Detached,Percent,Housing Units,91.8
    Marlborough,"0900345820",2010-2014,Detached,Percent,Margins of Error,4
    New Britain,"0900350440",2011-2015,Total,Number,Housing Units,31670
    New Britain,"0900350440",2011-2015,Total,Number,Margins of Error,703
    New Britain,"0900350440",2011-2015,Detached,Number,Housing Units,9061
    New Britain,"0900350440",2011-2015,Detached,Number,Margins of Error,478
    New Britain,"0900350440",2011-2015,Detached,Percent,Housing Units,28.6
    New Britain,"0900350440",2011-2015,Detached,Percent,Margins of Error,1.3
    New Britain,"0900350440",2010-2014,Total,Number,Housing Units,31023
    New Britain,"0900350440",2010-2014,Total,Number,Margins of Error,673
    New Britain,"0900350440",2010-2014,Detached,Number,Housing Units,8819
    New Britain,"0900350440",2010-2014,Detached,Number,Margins of Error,454
    New Britain,"0900350440",2010-2014,Detached,Percent,Housing Units,28.4
    New Britain,"0900350440",2010-2014,Detached,Percent,Margins of Error,1.3
    Newington,"0900352140",2011-2015,Total,Number,Housing Units,12990
    Newington,"0900352140",2011-2015,Total,Number,Margins of Error,299
    Newington,"0900352140",2011-2015,Detached,Number,Housing Units,8264
    Newington,"0900352140",2011-2015,Detached,Number,Margins of Error,340
    Newington,"0900352140",2011-2015,Detached,Percent,Housing Units,63.6
    Newington,"0900352140",2011-2015,Detached,Percent,Margins of Error,2
    Newington,"0900352140",2010-2014,Total,Number,Housing Units,13025
    Newington,"0900352140",2010-2014,Total,Number,Margins of Error,336
    Newington,"0900352140",2010-2014,Detached,Number,Housing Units,8390
    Newington,"0900352140",2010-2014,Detached,Number,Margins of Error,311
    Newington,"0900352140",2010-2014,Detached,Percent,Housing Units,64.4
    Newington,"0900352140",2010-2014,Detached,Percent,Margins of Error,1.6
    Plainville,"0900360120",2011-2015,Total,Number,Housing Units,8035
    Plainville,"0900360120",2011-2015,Total,Number,Margins of Error,237
    Plainville,"0900360120",2011-2015,Detached,Number,Housing Units,4792
    Plainville,"0900360120",2011-2015,Detached,Number,Margins of Error,324
    Plainville,"0900360120",2011-2015,Detached,Percent,Housing Units,59.6
    Plainville,"0900360120",2011-2015,Detached,Percent,Margins of Error,3.3
    Plainville,"0900360120",2010-2014,Total,Number,Housing Units,8172
    Plainville,"0900360120",2010-2014,Total,Number,Margins of Error,241
    Plainville,"0900360120",2010-2014,Detached,Number,Housing Units,4920
    Plainville,"0900360120",2010-2014,Detached,Number,Margins of Error,315
    Plainville,"0900360120",2010-2014,Detached,Percent,Housing Units,60.2
    Plainville,"0900360120",2010-2014,Detached,Percent,Margins of Error,3.4
    Rocky Hill,"0900365370",2011-2015,Total,Number,Housing Units,8408
    Rocky Hill,"0900365370",2011-2015,Total,Number,Margins of Error,317
    Rocky Hill,"0900365370",2011-2015,Detached,Number,Housing Units,4028
    Rocky Hill,"0900365370",2011-2015,Detached,Number,Margins of Error,254
    Rocky Hill,"0900365370",2011-2015,Detached,Percent,Housing Units,47.9
    Rocky Hill,"0900365370",2011-2015,Detached,Percent,Margins of Error,2.8
    Rocky Hill,"0900365370",2010-2014,Total,Number,Housing Units,8553
    Rocky Hill,"0900365370",2010-2014,Total,Number,Margins of Error,392
    Rocky Hill,"0900365370",2010-2014,Detached,Number,Housing Units,4089
    Rocky Hill,"0900365370",2010-2014,Detached,Number,Margins of Error,249
    Rocky Hill,"0900365370",2010-2014,Detached,Percent,Housing Units,47.8
    Rocky Hill,"0900365370",2010-2014,Detached,Percent,Margins of Error,2.4
    Simsbury,"0900368940",2011-2015,Total,Number,Housing Units,9248
    Simsbury,"0900368940",2011-2015,Total,Number,Margins of Error,220
    Simsbury,"0900368940",2011-2015,Detached,Number,Housing Units,7428
    Simsbury,"0900368940",2011-2015,Detached,Number,Margins of Error,239
    Simsbury,"0900368940",2011-2015,Detached,Percent,Housing Units,80.3
    Simsbury,"0900368940",2011-2015,Detached,Percent,Margins of Error,1.7
    Simsbury,"0900368940",2010-2014,Total,Number,Housing Units,9154
    Simsbury,"0900368940",2010-2014,Total,Number,Margins of Error,207
    Simsbury,"0900368940",2010-2014,Detached,Number,Housing Units,7404
    Simsbury,"0900368940",2010-2014,Detached,Number,Margins of Error,224
    Simsbury,"0900368940",2010-2014,Detached,Percent,Housing Units,80.9
    Simsbury,"0900368940",2010-2014,Detached,Percent,Margins of Error,1.7
    Southington,"0900370550",2011-2015,Total,Number,Housing Units,18037
    Southington,"0900370550",2011-2015,Total,Number,Margins of Error,389
    Southington,"0900370550",2011-2015,Detached,Number,Housing Units,12779
    Southington,"0900370550",2011-2015,Detached,Number,Margins of Error,445
    Southington,"0900370550",2011-2015,Detached,Percent,Housing Units,70.8
    Southington,"0900370550",2011-2015,Detached,Percent,Margins of Error,2
    Southington,"0900370550",2010-2014,Total,Number,Housing Units,17878
    Southington,"0900370550",2010-2014,Total,Number,Margins of Error,374
    Southington,"0900370550",2010-2014,Detached,Number,Housing Units,12516
    Southington,"0900370550",2010-2014,Detached,Number,Margins of Error,382
    Southington,"0900370550",2010-2014,Detached,Percent,Housing Units,70
    Southington,"0900370550",2010-2014,Detached,Percent,Margins of Error,1.7
    South Windsor,"0900371390",2011-2015,Total,Number,Housing Units,10143
    South Windsor,"0900371390",2011-2015,Total,Number,Margins of Error,313
    South Windsor,"0900371390",2011-2015,Detached,Number,Housing Units,7408
    South Windsor,"0900371390",2011-2015,Detached,Number,Margins of Error,313
    South Windsor,"0900371390",2011-2015,Detached,Percent,Housing Units,73
    South Windsor,"0900371390",2011-2015,Detached,Percent,Margins of Error,2
    South Windsor,"0900371390",2010-2014,Total,Number,Housing Units,10074
    South Windsor,"0900371390",2010-2014,Total,Number,Margins of Error,268
    South Windsor,"0900371390",2010-2014,Detached,Number,Housing Units,7465
    South Windsor,"0900371390",2010-2014,Detached,Number,Margins of Error,258
    South Windsor,"0900371390",2010-2014,Detached,Percent,Housing Units,74.1
    South Windsor,"0900371390",2010-2014,Detached,Percent,Margins of Error,1.8
    Suffield,"0900374540",2011-2015,Total,Number,Housing Units,4977
    Suffield,"0900374540",2011-2015,Total,Number,Margins of Error,248
    Suffield,"0900374540",2011-2015,Detached,Number,Housing Units,4172
    Suffield,"0900374540",2011-2015,Detached,Number,Margins of Error,243
    Suffield,"0900374540",2011-2015,Detached,Percent,Housing Units,83.8
    Suffield,"0900374540",2011-2015,Detached,Percent,Margins of Error,2.7
    Suffield,"0900374540",2010-2014,Total,Number,Housing Units,5098
    Suffield,"0900374540",2010-2014,Total,Number,Margins of Error,243
    Suffield,"0900374540",2010-2014,Detached,Number,Housing Units,4263
    Suffield,"0900374540",2010-2014,Detached,Number,Margins of Error,278
    Suffield,"0900374540",2010-2014,Detached,Percent,Housing Units,83.6
    Suffield,"0900374540",2010-2014,Detached,Percent,Margins of Error,3
    West Hartford,"0900382590",2011-2015,Total,Number,Housing Units,26262
    West Hartford,"0900382590",2011-2015,Total,Number,Margins of Error,436
    West Hartford,"0900382590",2011-2015,Detached,Number,Housing Units,17480
    West Hartford,"0900382590",2011-2015,Detached,Number,Margins of Error,444
    West Hartford,"0900382590",2011-2015,Detached,Percent,Housing Units,66.6
    West Hartford,"0900382590",2011-2015,Detached,Percent,Margins of Error,1.4
    West Hartford,"0900382590",2010-2014,Total,Number,Housing Units,26065
    West Hartford,"0900382590",2010-2014,Total,Number,Margins of Error,373
    West Hartford,"0900382590",2010-2014,Detached,Number,Housing Units,17348
    West Hartford,"0900382590",2010-2014,Detached,Number,Margins of Error,415
    West Hartford,"0900382590",2010-2014,Detached,Percent,Housing Units,66.6
    West Hartford,"0900382590",2010-2014,Detached,Percent,Margins of Error,1.3
    Wethersfield,"0900384900",2011-2015,Total,Number,Housing Units,11274
    Wethersfield,"0900384900",2011-2015,Total,Number,Margins of Error,306
    Wethersfield,"0900384900",2011-2015,Detached,Number,Housing Units,8397
    Wethersfield,"0900384900",2011-2015,Detached,Number,Margins of Error,302
    Wethersfield,"0900384900",2011-2015,Detached,Percent,Housing Units,74.5
    Wethersfield,"0900384900",2011-2015,Detached,Percent,Margins of Error,2.1
    Wethersfield,"0900384900",2010-2014,Total,Number,Housing Units,11291
    Wethersfield,"0900384900",2010-2014,Total,Number,Margins of Error,290
    Wethersfield,"0900384900",2010-2014,Detached,Number,Housing Units,8388
    Wethersfield,"0900384900",2010-2014,Detached,Number,Margins of Error,256
    Wethersfield,"0900384900",2010-2014,Detached,Percent,Housing Units,74.3
    Wethersfield,"0900384900",2010-2014,Detached,Percent,Margins of Error,2
    Windsor,"0900387000",2011-2015,Total,Number,Housing Units,11671
    Windsor,"0900387000",2011-2015,Total,Number,Margins of Error,286
    Windsor,"0900387000",2011-2015,Detached,Number,Housing Units,8972
    Windsor,"0900387000",2011-2015,Detached,Number,Margins of Error,242
    Windsor,"0900387000",2011-2015,Detached,Percent,Housing Units,76.9
    Windsor,"0900387000",2011-2015,Detached,Percent,Margins of Error,1.7
    Windsor,"0900387000",2010-2014,Total,Number,Housing Units,11671
    Windsor,"0900387000",2010-2014,Total,Number,Margins of Error,299
    Windsor,"0900387000",2010-2014,Detached,Number,Housing Units,8944
    Windsor,"0900387000",2010-2014,Detached,Number,Margins of Error,289
    Windsor,"0900387000",2010-2014,Detached,Percent,Housing Units,76.6
    Windsor,"0900387000",2010-2014,Detached,Percent,Margins of Error,1.6
    Windsor Locks,"0900387070",2011-2015,Total,Number,Housing Units,5295
    Windsor Locks,"0900387070",2011-2015,Total,Number,Margins of Error,350
    Windsor Locks,"0900387070",2011-2015,Detached,Number,Housing Units,3777
    Windsor Locks,"0900387070",2011-2015,Detached,Number,Margins of Error,300
    Windsor Locks,"0900387070",2011-2015,Detached,Percent,Housing Units,71.3
    Windsor Locks,"0900387070",2011-2015,Detached,Percent,Margins of Error,3.8
    Windsor Locks,"0900387070",2010-2014,Total,Number,Housing Units,5496
    Windsor Locks,"0900387070",2010-2014,Total,Number,Margins of Error,319
    Windsor Locks,"0900387070",2010-2014,Detached,Number,Housing Units,4031
    Windsor Locks,"0900387070",2010-2014,Detached,Number,Margins of Error,273
    Windsor Locks,"0900387070",2010-2014,Detached,Percent,Housing Units,73.3
    Windsor Locks,"0900387070",2010-2014,Detached,Percent,Margins of Error,3.4
    Barkhamsted,"0900502760",2011-2015,Total,Number,Housing Units,1500
    Barkhamsted,"0900502760",2011-2015,Total,Number,Margins of Error,103
    Barkhamsted,"0900502760",2011-2015,Detached,Number,Housing Units,1404
    Barkhamsted,"0900502760",2011-2015,Detached,Number,Margins of Error,100
    Barkhamsted,"0900502760",2011-2015,Detached,Percent,Housing Units,93.6
    Barkhamsted,"0900502760",2011-2015,Detached,Percent,Margins of Error,3.3
    Barkhamsted,"0900502760",2010-2014,Total,Number,Housing Units,1561
    Barkhamsted,"0900502760",2010-2014,Total,Number,Margins of Error,130
    Barkhamsted,"0900502760",2010-2014,Detached,Number,Housing Units,1412
    Barkhamsted,"0900502760",2010-2014,Detached,Number,Margins of Error,134
    Barkhamsted,"0900502760",2010-2014,Detached,Percent,Housing Units,90.5
    Barkhamsted,"0900502760",2010-2014,Detached,Percent,Margins of Error,4
    Bethlehem,"0900504930",2011-2015,Total,Number,Housing Units,1493
    Bethlehem,"0900504930",2011-2015,Total,Number,Margins of Error,104
    Bethlehem,"0900504930",2011-2015,Detached,Number,Housing Units,1383
    Bethlehem,"0900504930",2011-2015,Detached,Number,Margins of Error,103
    Bethlehem,"0900504930",2011-2015,Detached,Percent,Housing Units,92.6
    Bethlehem,"0900504930",2011-2015,Detached,Percent,Margins of Error,3.6
    Bethlehem,"0900504930",2010-2014,Total,Number,Housing Units,1502
    Bethlehem,"0900504930",2010-2014,Total,Number,Margins of Error,99
    Bethlehem,"0900504930",2010-2014,Detached,Number,Housing Units,1382
    Bethlehem,"0900504930",2010-2014,Detached,Number,Margins of Error,106
    Bethlehem,"0900504930",2010-2014,Detached,Percent,Housing Units,92
    Bethlehem,"0900504930",2010-2014,Detached,Percent,Margins of Error,3.7
    Bridgewater,"0900508210",2011-2015,Total,Number,Housing Units,886
    Bridgewater,"0900508210",2011-2015,Total,Number,Margins of Error,35
    Bridgewater,"0900508210",2011-2015,Detached,Number,Housing Units,846
    Bridgewater,"0900508210",2011-2015,Detached,Number,Margins of Error,40
    Bridgewater,"0900508210",2011-2015,Detached,Percent,Housing Units,95.5
    Bridgewater,"0900508210",2011-2015,Detached,Percent,Margins of Error,2.2
    Bridgewater,"0900508210",2010-2014,Total,Number,Housing Units,896
    Bridgewater,"0900508210",2010-2014,Total,Number,Margins of Error,33
    Bridgewater,"0900508210",2010-2014,Detached,Number,Housing Units,840
    Bridgewater,"0900508210",2010-2014,Detached,Number,Margins of Error,41
    Bridgewater,"0900508210",2010-2014,Detached,Percent,Housing Units,93.8
    Bridgewater,"0900508210",2010-2014,Detached,Percent,Margins of Error,2.6
    Canaan,"0900510940",2011-2015,Total,Number,Housing Units,746
    Canaan,"0900510940",2011-2015,Total,Number,Margins of Error,70
    Canaan,"0900510940",2011-2015,Detached,Number,Housing Units,661
    Canaan,"0900510940",2011-2015,Detached,Number,Margins of Error,68
    Canaan,"0900510940",2011-2015,Detached,Percent,Housing Units,88.6
    Canaan,"0900510940",2011-2015,Detached,Percent,Margins of Error,3.9
    Canaan,"0900510940",2010-2014,Total,Number,Housing Units,772
    Canaan,"0900510940",2010-2014,Total,Number,Margins of Error,64
    Canaan,"0900510940",2010-2014,Detached,Number,Housing Units,659
    Canaan,"0900510940",2010-2014,Detached,Number,Margins of Error,59
    Canaan,"0900510940",2010-2014,Detached,Percent,Housing Units,85.4
    Canaan,"0900510940",2010-2014,Detached,Percent,Margins of Error,4.2
    Colebrook,"0900516050",2011-2015,Total,Number,Housing Units,801
    Colebrook,"0900516050",2011-2015,Total,Number,Margins of Error,37
    Colebrook,"0900516050",2011-2015,Detached,Number,Housing Units,763
    Colebrook,"0900516050",2011-2015,Detached,Number,Margins of Error,42
    Colebrook,"0900516050",2011-2015,Detached,Percent,Housing Units,95.3
    Colebrook,"0900516050",2011-2015,Detached,Percent,Margins of Error,2.2
    Colebrook,"0900516050",2010-2014,Total,Number,Housing Units,773
    Colebrook,"0900516050",2010-2014,Total,Number,Margins of Error,29
    Colebrook,"0900516050",2010-2014,Detached,Number,Housing Units,736
    Colebrook,"0900516050",2010-2014,Detached,Number,Margins of Error,35
    Colebrook,"0900516050",2010-2014,Detached,Percent,Housing Units,95.2
    Colebrook,"0900516050",2010-2014,Detached,Percent,Margins of Error,2.6
    Cornwall,"0900517240",2011-2015,Total,Number,Housing Units,1020
    Cornwall,"0900517240",2011-2015,Total,Number,Margins of Error,33
    Cornwall,"0900517240",2011-2015,Detached,Number,Housing Units,937
    Cornwall,"0900517240",2011-2015,Detached,Number,Margins of Error,40
    Cornwall,"0900517240",2011-2015,Detached,Percent,Housing Units,91.9
    Cornwall,"0900517240",2011-2015,Detached,Percent,Margins of Error,3
    Cornwall,"0900517240",2010-2014,Total,Number,Housing Units,1002
    Cornwall,"0900517240",2010-2014,Total,Number,Margins of Error,31
    Cornwall,"0900517240",2010-2014,Detached,Number,Housing Units,917
    Cornwall,"0900517240",2010-2014,Detached,Number,Margins of Error,47
    Cornwall,"0900517240",2010-2014,Detached,Percent,Housing Units,91.5
    Cornwall,"0900517240",2010-2014,Detached,Percent,Margins of Error,3.5
    Goshen,"0900532290",2011-2015,Total,Number,Housing Units,1633
    Goshen,"0900532290",2011-2015,Total,Number,Margins of Error,142
    Goshen,"0900532290",2011-2015,Detached,Number,Housing Units,1572
    Goshen,"0900532290",2011-2015,Detached,Number,Margins of Error,151
    Goshen,"0900532290",2011-2015,Detached,Percent,Housing Units,96.3
    Goshen,"0900532290",2011-2015,Detached,Percent,Margins of Error,2.5
    Goshen,"0900532290",2010-2014,Total,Number,Housing Units,1694
    Goshen,"0900532290",2010-2014,Total,Number,Margins of Error,138
    Goshen,"0900532290",2010-2014,Detached,Number,Housing Units,1628
    Goshen,"0900532290",2010-2014,Detached,Number,Margins of Error,137
    Goshen,"0900532290",2010-2014,Detached,Percent,Housing Units,96.1
    Goshen,"0900532290",2010-2014,Detached,Percent,Margins of Error,3
    Harwinton,"0900537280",2011-2015,Total,Number,Housing Units,2259
    Harwinton,"0900537280",2011-2015,Total,Number,Margins of Error,125
    Harwinton,"0900537280",2011-2015,Detached,Number,Housing Units,2183
    Harwinton,"0900537280",2011-2015,Detached,Number,Margins of Error,123
    Harwinton,"0900537280",2011-2015,Detached,Percent,Housing Units,96.6
    Harwinton,"0900537280",2011-2015,Detached,Percent,Margins of Error,1.4
    Harwinton,"0900537280",2010-2014,Total,Number,Housing Units,2259
    Harwinton,"0900537280",2010-2014,Total,Number,Margins of Error,135
    Harwinton,"0900537280",2010-2014,Detached,Number,Housing Units,2196
    Harwinton,"0900537280",2010-2014,Detached,Number,Margins of Error,132
    Harwinton,"0900537280",2010-2014,Detached,Percent,Housing Units,97.2
    Harwinton,"0900537280",2010-2014,Detached,Percent,Margins of Error,1.4
    Kent,"0900540290",2011-2015,Total,Number,Housing Units,1508
    Kent,"0900540290",2011-2015,Total,Number,Margins of Error,165
    Kent,"0900540290",2011-2015,Detached,Number,Housing Units,1127
    Kent,"0900540290",2011-2015,Detached,Number,Margins of Error,174
    Kent,"0900540290",2011-2015,Detached,Percent,Housing Units,74.7
    Kent,"0900540290",2011-2015,Detached,Percent,Margins of Error,7.1
    Kent,"0900540290",2010-2014,Total,Number,Housing Units,1574
    Kent,"0900540290",2010-2014,Total,Number,Margins of Error,154
    Kent,"0900540290",2010-2014,Detached,Number,Housing Units,1113
    Kent,"0900540290",2010-2014,Detached,Number,Margins of Error,165
    Kent,"0900540290",2010-2014,Detached,Percent,Housing Units,70.7
    Kent,"0900540290",2010-2014,Detached,Percent,Margins of Error,6.7
    Litchfield,"0900543370",2011-2015,Total,Number,Housing Units,4151
    Litchfield,"0900543370",2011-2015,Total,Number,Margins of Error,271
    Litchfield,"0900543370",2011-2015,Detached,Number,Housing Units,3203
    Litchfield,"0900543370",2011-2015,Detached,Number,Margins of Error,234
    Litchfield,"0900543370",2011-2015,Detached,Percent,Housing Units,77.2
    Litchfield,"0900543370",2011-2015,Detached,Percent,Margins of Error,3.2
    Litchfield,"0900543370",2010-2014,Total,Number,Housing Units,4166
    Litchfield,"0900543370",2010-2014,Total,Number,Margins of Error,240
    Litchfield,"0900543370",2010-2014,Detached,Number,Housing Units,3187
    Litchfield,"0900543370",2010-2014,Detached,Number,Margins of Error,203
    Litchfield,"0900543370",2010-2014,Detached,Percent,Housing Units,76.5
    Litchfield,"0900543370",2010-2014,Detached,Percent,Margins of Error,2.8
    Morris,"0900549460",2011-2015,Total,Number,Housing Units,1292
    Morris,"0900549460",2011-2015,Total,Number,Margins of Error,59
    Morris,"0900549460",2011-2015,Detached,Number,Housing Units,1147
    Morris,"0900549460",2011-2015,Detached,Number,Margins of Error,70
    Morris,"0900549460",2011-2015,Detached,Percent,Housing Units,88.8
    Morris,"0900549460",2011-2015,Detached,Percent,Margins of Error,3.5
    Morris,"0900549460",2010-2014,Total,Number,Housing Units,1294
    Morris,"0900549460",2010-2014,Total,Number,Margins of Error,49
    Morris,"0900549460",2010-2014,Detached,Number,Housing Units,1149
    Morris,"0900549460",2010-2014,Detached,Number,Margins of Error,54
    Morris,"0900549460",2010-2014,Detached,Percent,Housing Units,88.8
    Morris,"0900549460",2010-2014,Detached,Percent,Margins of Error,3.5
    New Hartford,"0900551350",2011-2015,Total,Number,Housing Units,2906
    New Hartford,"0900551350",2011-2015,Total,Number,Margins of Error,228
    New Hartford,"0900551350",2011-2015,Detached,Number,Housing Units,2658
    New Hartford,"0900551350",2011-2015,Detached,Number,Margins of Error,235
    New Hartford,"0900551350",2011-2015,Detached,Percent,Housing Units,91.5
    New Hartford,"0900551350",2011-2015,Detached,Percent,Margins of Error,4.4
    New Hartford,"0900551350",2010-2014,Total,Number,Housing Units,2984
    New Hartford,"0900551350",2010-2014,Total,Number,Margins of Error,196
    New Hartford,"0900551350",2010-2014,Detached,Number,Housing Units,2785
    New Hartford,"0900551350",2010-2014,Detached,Number,Margins of Error,231
    New Hartford,"0900551350",2010-2014,Detached,Percent,Housing Units,93.3
    New Hartford,"0900551350",2010-2014,Detached,Percent,Margins of Error,3.5
    New Milford,"0900552630",2011-2015,Total,Number,Housing Units,11592
    New Milford,"0900552630",2011-2015,Total,Number,Margins of Error,314
    New Milford,"0900552630",2011-2015,Detached,Number,Housing Units,8625
    New Milford,"0900552630",2011-2015,Detached,Number,Margins of Error,339
    New Milford,"0900552630",2011-2015,Detached,Percent,Housing Units,74.4
    New Milford,"0900552630",2011-2015,Detached,Percent,Margins of Error,2.1
    New Milford,"0900552630",2010-2014,Total,Number,Housing Units,11700
    New Milford,"0900552630",2010-2014,Total,Number,Margins of Error,354
    New Milford,"0900552630",2010-2014,Detached,Number,Housing Units,8664
    New Milford,"0900552630",2010-2014,Detached,Number,Margins of Error,358
    New Milford,"0900552630",2010-2014,Detached,Percent,Housing Units,74.1
    New Milford,"0900552630",2010-2014,Detached,Percent,Margins of Error,2.1
    Norfolk,"0900553470",2011-2015,Total,Number,Housing Units,940
    Norfolk,"0900553470",2011-2015,Total,Number,Margins of Error,63
    Norfolk,"0900553470",2011-2015,Detached,Number,Housing Units,716
    Norfolk,"0900553470",2011-2015,Detached,Number,Margins of Error,58
    Norfolk,"0900553470",2011-2015,Detached,Percent,Housing Units,76.2
    Norfolk,"0900553470",2011-2015,Detached,Percent,Margins of Error,4.7
    Norfolk,"0900553470",2010-2014,Total,Number,Housing Units,912
    Norfolk,"0900553470",2010-2014,Total,Number,Margins of Error,60
    Norfolk,"0900553470",2010-2014,Detached,Number,Housing Units,723
    Norfolk,"0900553470",2010-2014,Detached,Number,Margins of Error,66
    Norfolk,"0900553470",2010-2014,Detached,Percent,Housing Units,79.3
    Norfolk,"0900553470",2010-2014,Detached,Percent,Margins of Error,5.3
    North Canaan,"0900554030",2011-2015,Total,Number,Housing Units,1558
    North Canaan,"0900554030",2011-2015,Total,Number,Margins of Error,117
    North Canaan,"0900554030",2011-2015,Detached,Number,Housing Units,1254
    North Canaan,"0900554030",2011-2015,Detached,Number,Margins of Error,141
    North Canaan,"0900554030",2011-2015,Detached,Percent,Housing Units,80.5
    North Canaan,"0900554030",2011-2015,Detached,Percent,Margins of Error,5.8
    North Canaan,"0900554030",2010-2014,Total,Number,Housing Units,1596
    North Canaan,"0900554030",2010-2014,Total,Number,Margins of Error,126
    North Canaan,"0900554030",2010-2014,Detached,Number,Housing Units,1318
    North Canaan,"0900554030",2010-2014,Detached,Number,Margins of Error,150
    North Canaan,"0900554030",2010-2014,Detached,Percent,Housing Units,82.6
    North Canaan,"0900554030",2010-2014,Detached,Percent,Margins of Error,6.6
    Plymouth,"0900560750",2011-2015,Total,Number,Housing Units,5127
    Plymouth,"0900560750",2011-2015,Total,Number,Margins of Error,172
    Plymouth,"0900560750",2011-2015,Detached,Number,Housing Units,3931
    Plymouth,"0900560750",2011-2015,Detached,Number,Margins of Error,209
    Plymouth,"0900560750",2011-2015,Detached,Percent,Housing Units,76.7
    Plymouth,"0900560750",2011-2015,Detached,Percent,Margins of Error,2.8
    Plymouth,"0900560750",2010-2014,Total,Number,Housing Units,5124
    Plymouth,"0900560750",2010-2014,Total,Number,Margins of Error,197
    Plymouth,"0900560750",2010-2014,Detached,Number,Housing Units,3815
    Plymouth,"0900560750",2010-2014,Detached,Number,Margins of Error,204
    Plymouth,"0900560750",2010-2014,Detached,Percent,Housing Units,74.5
    Plymouth,"0900560750",2010-2014,Detached,Percent,Margins of Error,3
    Roxbury,"0900565930",2011-2015,Total,Number,Housing Units,1209
    Roxbury,"0900565930",2011-2015,Total,Number,Margins of Error,35
    Roxbury,"0900565930",2011-2015,Detached,Number,Housing Units,1165
    Roxbury,"0900565930",2011-2015,Detached,Number,Margins of Error,43
    Roxbury,"0900565930",2011-2015,Detached,Percent,Housing Units,96.4
    Roxbury,"0900565930",2011-2015,Detached,Percent,Margins of Error,2.4
    Roxbury,"0900565930",2010-2014,Total,Number,Housing Units,1197
    Roxbury,"0900565930",2010-2014,Total,Number,Margins of Error,44
    Roxbury,"0900565930",2010-2014,Detached,Number,Housing Units,1162
    Roxbury,"0900565930",2010-2014,Detached,Number,Margins of Error,49
    Roxbury,"0900565930",2010-2014,Detached,Percent,Housing Units,97.1
    Roxbury,"0900565930",2010-2014,Detached,Percent,Margins of Error,1.9
    Salisbury,"0900566420",2011-2015,Total,Number,Housing Units,2439
    Salisbury,"0900566420",2011-2015,Total,Number,Margins of Error,185
    Salisbury,"0900566420",2011-2015,Detached,Number,Housing Units",2016
    Salisbury,"0900566420",2011-2015,Detached,Number,Margins of Error,222
    Salisbury,"0900566420",2011-2015,Detached,Percent,Housing Units,82.7
    Salisbury,"0900566420",2011-2015,Detached,Percent,Margins of Error,6.2
    Salisbury,"0900566420",2010-2014,Total,Number,Housing Units,2478
    Salisbury,"0900566420",2010-2014,Total,Number,Margins of Error,187
    Salisbury,"0900566420",2010-2014,Detached,Number,Housing Units,2114
    Salisbury,"0900566420",2010-2014,Detached,Number,Margins of Error,225
    Salisbury,"0900566420",2010-2014,Detached,Percent,Housing Units,85.3
    Salisbury,"0900566420",2010-2014,Detached,Percent,Margins of Error,5.1
    Sharon,"0900567960",2011-2015,Total,Number,Housing Units,1943
    Sharon,"0900567960",2011-2015,Total,Number,Margins of Error,143
    Sharon,"0900567960",2011-2015,Detached,Number,Housing Units,1779
    Sharon,"0900567960",2011-2015,Detached,Number,Margins of Error,154
    Sharon,"0900567960",2011-2015,Detached,Percent,Housing Units,91.6
    Sharon,"0900567960",2011-2015,Detached,Percent,Margins of Error,4.2
    Sharon,"0900567960",2010-2014,Total,Number,Housing Units,1816
    Sharon,"0900567960",2010-2014,Total,Number,Margins of Error,135
    Sharon,"0900567960",2010-2014,Detached,Number,Housing Units,1617
    Sharon,"0900567960",2010-2014,Detached,Number,Margins of Error,178
    Sharon,"0900567960",2010-2014,Detached,Percent,Housing Units,89
    Sharon,"0900567960",2010-2014,Detached,Percent,Margins of Error,6.5
    Thomaston,"0900575730",2011-2015,Total,Number,Housing Units,3104
    Thomaston,"0900575730",2011-2015,Total,Number,Margins of Error,170
    Thomaston,"0900575730",2011-2015,Detached,Number,Housing Units,2227
    Thomaston,"0900575730",2011-2015,Detached,Number,Margins of Error,152
    Thomaston,"0900575730",2011-2015,Detached,Percent,Housing Units,71.7
    Thomaston,"0900575730",2011-2015,Detached,Percent,Margins of Error,4.3
    Thomaston,"0900575730",2010-2014,Total,Number,Housing Units,3110
    Thomaston,"0900575730",2010-2014,Total,Number,Margins of Error,128
    Thomaston,"0900575730",2010-2014,Detached,Number,Housing Units,2229
    Thomaston,"0900575730",2010-2014,Detached,Number,Margins of Error,124
    Thomaston,"0900575730",2010-2014,Detached,Percent,Housing Units,71.7
    Thomaston,"0900575730",2010-2014,Detached,Percent,Margins of Error,4.4
    Torrington,"0900576570",2011-2015,Total,Number,Housing Units,17195
    Torrington,"0900576570",2011-2015,Total,Number,Margins of Error,423
    Torrington,"0900576570",2011-2015,Detached,Number,Housing Units,9308
    Torrington,"0900576570",2011-2015,Detached,Number,Margins of Error,372
    Torrington,"0900576570",2011-2015,Detached,Percent,Housing Units,54.1
    Torrington,"0900576570",2011-2015,Detached,Percent,Margins of Error,1.7
    Torrington,"0900576570",2010-2014,Total,Number,Housing Units,16812
    Torrington,"0900576570",2010-2014,Total,Number,Margins of Error,376
    Torrington,"0900576570",2010-2014,Detached,Number,Housing Units,9249
    Torrington,"0900576570",2010-2014,Detached,Number,Margins of Error,393
    Torrington,"0900576570",2010-2014,Detached,Percent,Housing Units,55
    Torrington,"0900576570",2010-2014,Detached,Percent,Margins of Error,2.1
    Warren,"0900579510",2011-2015,Total,Number,Housing Units,826
    Warren,"0900579510",2011-2015,Total,Number,Margins of Error,33
    Warren,"0900579510",2011-2015,Detached,Number,Housing Units,805
    Warren,"0900579510",2011-2015,Detached,Number,Margins of Error,38
    Warren,"0900579510",2011-2015,Detached,Percent,Housing Units,97.5
    Warren,"0900579510",2011-2015,Detached,Percent,Margins of Error,2.3
    Warren,"0900579510",2010-2014,Total,Number,Housing Units,819
    Warren,"0900579510",2010-2014,Total,Number,Margins of Error,27
    Warren,"0900579510",2010-2014,Detached,Number,Housing Units,786
    Warren,"0900579510",2010-2014,Detached,Number,Margins of Error,40
    Warren,"0900579510",2010-2014,Detached,Percent,Housing Units,96
    Warren,"0900579510",2010-2014,Detached,Percent,Margins of Error,2.9
    Washington,"0900579720",2011-2015,Total,Number,Housing Units,2200
    Washington,"0900579720",2011-2015,Total,Number,Margins of Error,158
    Washington,"0900579720",2011-2015,Detached,Number,Housing Units,2033
    Washington,"0900579720",2011-2015,Detached,Number,Margins of Error,170
    Washington,"0900579720",2011-2015,Detached,Percent,Housing Units,92.4
    Washington,"0900579720",2011-2015,Detached,Percent,Margins of Error,2.8
    Washington,"0900579720",2010-2014,Total,Number,Housing Units,2195
    Washington,"0900579720",2010-2014,Total,Number,Margins of Error,185
    Washington,"0900579720",2010-2014,Detached,Number,Housing Units",2016
    Washington,"0900579720",2010-2014,Detached,Number,Margins of Error,187
    Washington,"0900579720",2010-2014,Detached,Percent,Housing Units,91.8
    Washington,"0900579720",2010-2014,Detached,Percent,Margins of Error,2.6
    Watertown,"0900580490",2011-2015,Total,Number,Housing Units,8835
    Watertown,"0900580490",2011-2015,Total,Number,Margins of Error,326
    Watertown,"0900580490",2011-2015,Detached,Number,Housing Units,6992
    Watertown,"0900580490",2011-2015,Detached,Number,Margins of Error,378
    Watertown,"0900580490",2011-2015,Detached,Percent,Housing Units,79.1
    Watertown,"0900580490",2011-2015,Detached,Percent,Margins of Error,2.8
    Watertown,"0900580490",2010-2014,Total,Number,Housing Units,9098
    Watertown,"0900580490",2010-2014,Total,Number,Margins of Error,271
    Watertown,"0900580490",2010-2014,Detached,Number,Housing Units,7072
    Watertown,"0900580490",2010-2014,Detached,Number,Margins of Error,327
    Watertown,"0900580490",2010-2014,Detached,Percent,Housing Units,77.7
    Watertown,"0900580490",2010-2014,Detached,Percent,Margins of Error,2.5
    Winchester,"0900586440",2011-2015,Total,Number,Housing Units,5822
    Winchester,"0900586440",2011-2015,Total,Number,Margins of Error,299
    Winchester,"0900586440",2011-2015,Detached,Number,Housing Units,3308
    Winchester,"0900586440",2011-2015,Detached,Number,Margins of Error,292
    Winchester,"0900586440",2011-2015,Detached,Percent,Housing Units,56.8
    Winchester,"0900586440",2011-2015,Detached,Percent,Margins of Error,4.4
    Winchester,"0900586440",2010-2014,Total,Number,Housing Units,5661
    Winchester,"0900586440",2010-2014,Total,Number,Margins of Error,321
    Winchester,"0900586440",2010-2014,Detached,Number,Housing Units,3244
    Winchester,"0900586440",2010-2014,Detached,Number,Margins of Error,328
    Winchester,"0900586440",2010-2014,Detached,Percent,Housing Units,57.3
    Winchester,"0900586440",2010-2014,Detached,Percent,Margins of Error,4.6
    Woodbury,"0900587910",2011-2015,Total,Number,Housing Units,4462
    Woodbury,"0900587910",2011-2015,Total,Number,Margins of Error,203
    Woodbury,"0900587910",2011-2015,Detached,Number,Housing Units,3031
    Woodbury,"0900587910",2011-2015,Detached,Number,Margins of Error,219
    Woodbury,"0900587910",2011-2015,Detached,Percent,Housing Units,67.9
    Woodbury,"0900587910",2011-2015,Detached,Percent,Margins of Error,4
    Woodbury,"0900587910",2010-2014,Total,Number,Housing Units,4495
    Woodbury,"0900587910",2010-2014,Total,Number,Margins of Error,238
    Woodbury,"0900587910",2010-2014,Detached,Number,Housing Units,3109
    Woodbury,"0900587910",2010-2014,Detached,Number,Margins of Error,208
    Woodbury,"0900587910",2010-2014,Detached,Percent,Housing Units,69.2
    Woodbury,"0900587910",2010-2014,Detached,Percent,Margins of Error,3.6
    Chester,"0900714300",2011-2015,Total,Number,Housing Units,2091
    Chester,"0900714300",2011-2015,Total,Number,Margins of Error,134
    Chester,"0900714300",2011-2015,Detached,Number,Housing Units,1576
    Chester,"0900714300",2011-2015,Detached,Number,Margins of Error,140
    Chester,"0900714300",2011-2015,Detached,Percent,Housing Units,75.4
    Chester,"0900714300",2011-2015,Detached,Percent,Margins of Error,4.3
    Chester,"0900714300",2010-2014,Total,Number,Housing Units,2096
    Chester,"0900714300",2010-2014,Total,Number,Margins of Error,126
    Chester,"0900714300",2010-2014,Detached,Number,Housing Units,1538
    Chester,"0900714300",2010-2014,Detached,Number,Margins of Error,128
    Chester,"0900714300",2010-2014,Detached,Percent,Housing Units,73.4
    Chester,"0900714300",2010-2014,Detached,Percent,Margins of Error,4.6
    Clinton,"0900715350",2011-2015,Total,Number,Housing Units,6157
    Clinton,"0900715350",2011-2015,Total,Number,Margins of Error,236
    Clinton,"0900715350",2011-2015,Detached,Number,Housing Units,4964
    Clinton,"0900715350",2011-2015,Detached,Number,Margins of Error,226
    Clinton,"0900715350",2011-2015,Detached,Percent,Housing Units,80.6
    Clinton,"0900715350",2011-2015,Detached,Percent,Margins of Error,2.3
    Clinton,"0900715350",2010-2014,Total,Number,Housing Units,6001
    Clinton,"0900715350",2010-2014,Total,Number,Margins of Error,235
    Clinton,"0900715350",2010-2014,Detached,Number,Housing Units,4791
    Clinton,"0900715350",2010-2014,Detached,Number,Margins of Error,236
    Clinton,"0900715350",2010-2014,Detached,Percent,Housing Units,79.8
    Clinton,"0900715350",2010-2014,Detached,Percent,Margins of Error,2.7
    Cromwell,"0900718080",2011-2015,Total,Number,Housing Units,5846
    Cromwell,"0900718080",2011-2015,Total,Number,Margins of Error,258
    Cromwell,"0900718080",2011-2015,Detached,Number,Housing Units,3395
    Cromwell,"0900718080",2011-2015,Detached,Number,Margins of Error,203
    Cromwell,"0900718080",2011-2015,Detached,Percent,Housing Units,58.1
    Cromwell,"0900718080",2011-2015,Detached,Percent,Margins of Error,2.9
    Cromwell,"0900718080",2010-2014,Total,Number,Housing Units,5823
    Cromwell,"0900718080",2010-2014,Total,Number,Margins of Error,291
    Cromwell,"0900718080",2010-2014,Detached,Number,Housing Units,3331
    Cromwell,"0900718080",2010-2014,Detached,Number,Margins of Error,247
    Cromwell,"0900718080",2010-2014,Detached,Percent,Housing Units,57.2
    Cromwell,"0900718080",2010-2014,Detached,Percent,Margins of Error,3.3
    Deep River,"0900719130",2011-2015,Total,Number,Housing Units,2169
    Deep River,"0900719130",2011-2015,Total,Number,Margins of Error,127
    Deep River,"0900719130",2011-2015,Detached,Number,Housing Units,1641
    Deep River,"0900719130",2011-2015,Detached,Number,Margins of Error,127
    Deep River,"0900719130",2011-2015,Detached,Percent,Housing Units,75.7
    Deep River,"0900719130",2011-2015,Detached,Percent,Margins of Error,4.7
    Deep River,"0900719130",2010-2014,Total,Number,Housing Units,2178
    Deep River,"0900719130",2010-2014,Total,Number,Margins of Error,152
    Deep River,"0900719130",2010-2014,Detached,Number,Housing Units,1615
    Deep River,"0900719130",2010-2014,Detached,Number,Margins of Error,182
    Deep River,"0900719130",2010-2014,Detached,Percent,Housing Units,74.2
    Deep River,"0900719130",2010-2014,Detached,Percent,Margins of Error,6
    Durham,"0900720810",2011-2015,Total,Number,Housing Units,2692
    Durham,"0900720810",2011-2015,Total,Number,Margins of Error,197
    Durham,"0900720810",2011-2015,Detached,Number,Housing Units,2437
    Durham,"0900720810",2011-2015,Detached,Number,Margins of Error,194
    Durham,"0900720810",2011-2015,Detached,Percent,Housing Units,90.5
    Durham,"0900720810",2011-2015,Detached,Percent,Margins of Error,4.6
    Durham,"0900720810",2010-2014,Total,Number,Housing Units,2685
    Durham,"0900720810",2010-2014,Total,Number,Margins of Error,173
    Durham,"0900720810",2010-2014,Detached,Number,Housing Units,2424
    Durham,"0900720810",2010-2014,Detached,Number,Margins of Error,194
    Durham,"0900720810",2010-2014,Detached,Percent,Housing Units,90.3
    Durham,"0900720810",2010-2014,Detached,Percent,Margins of Error,4.7
    East Haddam,"0900722280",2011-2015,Total,Number,Housing Units,4538
    East Haddam,"0900722280",2011-2015,Total,Number,Margins of Error,221
    East Haddam,"0900722280",2011-2015,Detached,Number,Housing Units,4127
    East Haddam,"0900722280",2011-2015,Detached,Number,Margins of Error,297
    East Haddam,"0900722280",2011-2015,Detached,Percent,Housing Units,90.9
    East Haddam,"0900722280",2011-2015,Detached,Percent,Margins of Error,3.4
    East Haddam,"0900722280",2010-2014,Total,Number,Housing Units,4540
    East Haddam,"0900722280",2010-2014,Total,Number,Margins of Error,254
    East Haddam,"0900722280",2010-2014,Detached,Number,Housing Units,4191
    East Haddam,"0900722280",2010-2014,Detached,Number,Margins of Error,286
    East Haddam,"0900722280",2010-2014,Detached,Percent,Housing Units,92.3
    East Haddam,"0900722280",2010-2014,Detached,Percent,Margins of Error,3.1
    East Hampton,"0900722490",2011-2015,Total,Number,Housing Units,5570
    East Hampton,"0900722490",2011-2015,Total,Number,Margins of Error,224
    East Hampton,"0900722490",2011-2015,Detached,Number,Housing Units,4632
    East Hampton,"0900722490",2011-2015,Detached,Number,Margins of Error,234
    East Hampton,"0900722490",2011-2015,Detached,Percent,Housing Units,83.2
    East Hampton,"0900722490",2011-2015,Detached,Percent,Margins of Error,3.1
    East Hampton,"0900722490",2010-2014,Total,Number,Housing Units,5547
    East Hampton,"0900722490",2010-2014,Total,Number,Margins of Error,235
    East Hampton,"0900722490",2010-2014,Detached,Number,Housing Units,4623
    East Hampton,"0900722490",2010-2014,Detached,Number,Margins of Error,210
    East Hampton,"0900722490",2010-2014,Detached,Percent,Housing Units,83.3
    East Hampton,"0900722490",2010-2014,Detached,Percent,Margins of Error,3.3
    Essex,"0900726270",2011-2015,Total,Number,Housing Units,3263
    Essex,"0900726270",2011-2015,Total,Number,Margins of Error,197
    Essex,"0900726270",2011-2015,Detached,Number,Housing Units,2455
    Essex,"0900726270",2011-2015,Detached,Number,Margins of Error,218
    Essex,"0900726270",2011-2015,Detached,Percent,Housing Units,75.2
    Essex,"0900726270",2011-2015,Detached,Percent,Margins of Error,5.5
    Essex,"0900726270",2010-2014,Total,Number,Housing Units,3195
    Essex,"0900726270",2010-2014,Total,Number,Margins of Error,159
    Essex,"0900726270",2010-2014,Detached,Number,Housing Units,2457
    Essex,"0900726270",2010-2014,Detached,Number,Margins of Error,155
    Essex,"0900726270",2010-2014,Detached,Percent,Housing Units,76.9
    Essex,"0900726270",2010-2014,Detached,Percent,Margins of Error,4.4
    Haddam,"0900735230",2011-2015,Total,Number,Housing Units,3552
    Haddam,"0900735230",2011-2015,Total,Number,Margins of Error,196
    Haddam,"0900735230",2011-2015,Detached,Number,Housing Units,3327
    Haddam,"0900735230",2011-2015,Detached,Number,Margins of Error,224
    Haddam,"0900735230",2011-2015,Detached,Percent,Housing Units,93.7
    Haddam,"0900735230",2011-2015,Detached,Percent,Margins of Error,3.4
    Haddam,"0900735230",2010-2014,Total,Number,Housing Units,3481
    Haddam,"0900735230",2010-2014,Total,Number,Margins of Error,220
    Haddam,"0900735230",2010-2014,Detached,Number,Housing Units,3226
    Haddam,"0900735230",2010-2014,Detached,Number,Margins of Error,217
    Haddam,"0900735230",2010-2014,Detached,Percent,Housing Units,92.7
    Haddam,"0900735230",2010-2014,Detached,Percent,Margins of Error,3.2
    Killingworth,"0900740710",2011-2015,Total,Number,Housing Units,2709
    Killingworth,"0900740710",2011-2015,Total,Number,Margins of Error,128
    Killingworth,"0900740710",2011-2015,Detached,Number,Housing Units,2333
    Killingworth,"0900740710",2011-2015,Detached,Number,Margins of Error,152
    Killingworth,"0900740710",2011-2015,Detached,Percent,Housing Units,86.1
    Killingworth,"0900740710",2011-2015,Detached,Percent,Margins of Error,3.8
    Killingworth,"0900740710",2010-2014,Total,Number,Housing Units,2800
    Killingworth,"0900740710",2010-2014,Total,Number,Margins of Error,140
    Killingworth,"0900740710",2010-2014,Detached,Number,Housing Units,2449
    Killingworth,"0900740710",2010-2014,Detached,Number,Margins of Error,163
    Killingworth,"0900740710",2010-2014,Detached,Percent,Housing Units,87.5
    Killingworth,"0900740710",2010-2014,Detached,Percent,Margins of Error,3.2
    Middlefield,"0900747080",2011-2015,Total,Number,Housing Units,1822
    Middlefield,"0900747080",2011-2015,Total,Number,Margins of Error,119
    Middlefield,"0900747080",2011-2015,Detached,Number,Housing Units,1671
    Middlefield,"0900747080",2011-2015,Detached,Number,Margins of Error,115
    Middlefield,"0900747080",2011-2015,Detached,Percent,Housing Units,91.7
    Middlefield,"0900747080",2011-2015,Detached,Percent,Margins of Error,3.2
    Middlefield,"0900747080",2010-2014,Total,Number,Housing Units,1805
    Middlefield,"0900747080",2010-2014,Total,Number,Margins of Error,103
    Middlefield,"0900747080",2010-2014,Detached,Number,Housing Units,1619
    Middlefield,"0900747080",2010-2014,Detached,Number,Margins of Error,119
    Middlefield,"0900747080",2010-2014,Detached,Percent,Housing Units,89.7
    Middlefield,"0900747080",2010-2014,Detached,Percent,Margins of Error,3.8
    Middletown,"0900747360",2011-2015,Total,Number,Housing Units,21081
    Middletown,"0900747360",2011-2015,Total,Number,Margins of Error,543
    Middletown,"0900747360",2011-2015,Detached,Number,Housing Units,9332
    Middletown,"0900747360",2011-2015,Detached,Number,Margins of Error,378
    Middletown,"0900747360",2011-2015,Detached,Percent,Housing Units,44.3
    Middletown,"0900747360",2011-2015,Detached,Percent,Margins of Error,1.7
    Middletown,"0900747360",2010-2014,Total,Number,Housing Units,21170
    Middletown,"0900747360",2010-2014,Total,Number,Margins of Error,535
    Middletown,"0900747360",2010-2014,Detached,Number,Housing Units,9627
    Middletown,"0900747360",2010-2014,Detached,Number,Margins of Error,397
    Middletown,"0900747360",2010-2014,Detached,Percent,Housing Units,45.5
    Middletown,"0900747360",2010-2014,Detached,Percent,Margins of Error,1.7
    Old Saybrook,"0900757320",2011-2015,Total,Number,Housing Units,5723
    Old Saybrook,"0900757320",2011-2015,Total,Number,Margins of Error,252
    Old Saybrook,"0900757320",2011-2015,Detached,Number,Housing Units,5256
    Old Saybrook,"0900757320",2011-2015,Detached,Number,Margins of Error,251
    Old Saybrook,"0900757320",2011-2015,Detached,Percent,Housing Units,91.8
    Old Saybrook,"0900757320",2011-2015,Detached,Percent,Margins of Error,2.3
    Old Saybrook,"0900757320",2010-2014,Total,Number,Housing Units,5814
    Old Saybrook,"0900757320",2010-2014,Total,Number,Margins of Error,234
    Old Saybrook,"0900757320",2010-2014,Detached,Number,Housing Units,5460
    Old Saybrook,"0900757320",2010-2014,Detached,Number,Margins of Error,233
    Old Saybrook,"0900757320",2010-2014,Detached,Percent,Housing Units,93.9
    Old Saybrook,"0900757320",2010-2014,Detached,Percent,Margins of Error,1.9
    Portland,"0900761800",2011-2015,Total,Number,Housing Units,4308
    Portland,"0900761800",2011-2015,Total,Number,Margins of Error,208
    Portland,"0900761800",2011-2015,Detached,Number,Housing Units,3592
    Portland,"0900761800",2011-2015,Detached,Number,Margins of Error,218
    Portland,"0900761800",2011-2015,Detached,Percent,Housing Units,83.4
    Portland,"0900761800",2011-2015,Detached,Percent,Margins of Error,3.3
    Portland,"0900761800",2010-2014,Total,Number,Housing Units,4404
    Portland,"0900761800",2010-2014,Total,Number,Margins of Error,195
    Portland,"0900761800",2010-2014,Detached,Number,Housing Units,3590
    Portland,"0900761800",2010-2014,Detached,Number,Margins of Error,218
    Portland,"0900761800",2010-2014,Detached,Percent,Housing Units,81.5
    Portland,"0900761800",2010-2014,Detached,Percent,Margins of Error,3.2
    Westbrook,"0900781680",2011-2015,Total,Number,Housing Units,3641
    Westbrook,"0900781680",2011-2015,Total,Number,Margins of Error,216
    Westbrook,"0900781680",2011-2015,Detached,Number,Housing Units,2851
    Westbrook,"0900781680",2011-2015,Detached,Number,Margins of Error,262
    Westbrook,"0900781680",2011-2015,Detached,Percent,Housing Units,78.3
    Westbrook,"0900781680",2011-2015,Detached,Percent,Margins of Error,5.3
    Westbrook,"0900781680",2010-2014,Total,Number,Housing Units,3542
    Westbrook,"0900781680",2010-2014,Total,Number,Margins of Error,215
    Westbrook,"0900781680",2010-2014,Detached,Number,Housing Units,2828
    Westbrook,"0900781680",2010-2014,Detached,Number,Margins of Error,242
    Westbrook,"0900781680",2010-2014,Detached,Percent,Housing Units,79.8
    Westbrook,"0900781680",2010-2014,Detached,Percent,Margins of Error,4.8
    Ansonia,"0900901220",2011-2015,Total,Number,Housing Units,7408
    Ansonia,"0900901220",2011-2015,Total,Number,Margins of Error,395
    Ansonia,"0900901220",2011-2015,Detached,Number,Housing Units,3422
    Ansonia,"0900901220",2011-2015,Detached,Number,Margins of Error,262
    Ansonia,"0900901220",2011-2015,Detached,Percent,Housing Units,46.2
    Ansonia,"0900901220",2011-2015,Detached,Percent,Margins of Error,3.3
    Ansonia,"0900901220",2010-2014,Total,Number,Housing Units,7711
    Ansonia,"0900901220",2010-2014,Total,Number,Margins of Error,419
    Ansonia,"0900901220",2010-2014,Detached,Number,Housing Units,3428
    Ansonia,"0900901220",2010-2014,Detached,Number,Margins of Error,275
    Ansonia,"0900901220",2010-2014,Detached,Percent,Housing Units,44.5
    Ansonia,"0900901220",2010-2014,Detached,Percent,Margins of Error,3.1
    Beacon Falls,"0900903250",2011-2015,Total,Number,Housing Units,2623
    Beacon Falls,"0900903250",2011-2015,Total,Number,Margins of Error,167
    Beacon Falls,"0900903250",2011-2015,Detached,Number,Housing Units,1537
    Beacon Falls,"0900903250",2011-2015,Detached,Number,Margins of Error,175
    Beacon Falls,"0900903250",2011-2015,Detached,Percent,Housing Units,58.6
    Beacon Falls,"0900903250",2011-2015,Detached,Percent,Margins of Error,5.8
    Beacon Falls,"0900903250",2010-2014,Total,Number,Housing Units,2579
    Beacon Falls,"0900903250",2010-2014,Total,Number,Margins of Error,156
    Beacon Falls,"0900903250",2010-2014,Detached,Number,Housing Units,1632
    Beacon Falls,"0900903250",2010-2014,Detached,Number,Margins of Error,138
    Beacon Falls,"0900903250",2010-2014,Detached,Percent,Housing Units,63.3
    Beacon Falls,"0900903250",2010-2014,Detached,Percent,Margins of Error,5.2
    Bethany,"0900904580",2011-2015,Total,Number,Housing Units,2060
    Bethany,"0900904580",2011-2015,Total,Number,Margins of Error,114
    Bethany,"0900904580",2011-2015,Detached,Number,Housing Units,1927
    Bethany,"0900904580",2011-2015,Detached,Number,Margins of Error,119
    Bethany,"0900904580",2011-2015,Detached,Percent,Housing Units,93.5
    Bethany,"0900904580",2011-2015,Detached,Percent,Margins of Error,2.9
    Bethany,"0900904580",2010-2014,Total,Number,Housing Units,2105
    Bethany,"0900904580",2010-2014,Total,Number,Margins of Error,115
    Bethany,"0900904580",2010-2014,Detached,Number,Housing Units,1960
    Bethany,"0900904580",2010-2014,Detached,Number,Margins of Error,102
    Bethany,"0900904580",2010-2014,Detached,Percent,Housing Units,93.1
    Bethany,"0900904580",2010-2014,Detached,Percent,Margins of Error,2.8
    Branford,"0900907310",2011-2015,Total,Number,Housing Units,13967
    Branford,"0900907310",2011-2015,Total,Number,Margins of Error,446
    Branford,"0900907310",2011-2015,Detached,Number,Housing Units,7146
    Branford,"0900907310",2011-2015,Detached,Number,Margins of Error,369
    Branford,"0900907310",2011-2015,Detached,Percent,Housing Units,51.2
    Branford,"0900907310",2011-2015,Detached,Percent,Margins of Error,2.1
    Branford,"0900907310",2010-2014,Total,Number,Housing Units,13747
    Branford,"0900907310",2010-2014,Total,Number,Margins of Error,379
    Branford,"0900907310",2010-2014,Detached,Number,Housing Units,7032
    Branford,"0900907310",2010-2014,Detached,Number,Margins of Error,349
    Branford,"0900907310",2010-2014,Detached,Percent,Housing Units,51.2
    Branford,"0900907310",2010-2014,Detached,Percent,Margins of Error,2.1
    Cheshire,"0900914160",2011-2015,Total,Number,Housing Units,10413
    Cheshire,"0900914160",2011-2015,Total,Number,Margins of Error,296
    Cheshire,"0900914160",2011-2015,Detached,Number,Housing Units,8157
    Cheshire,"0900914160",2011-2015,Detached,Number,Margins of Error,324
    Cheshire,"0900914160",2011-2015,Detached,Percent,Housing Units,78.3
    Cheshire,"0900914160",2011-2015,Detached,Percent,Margins of Error,2.3
    Cheshire,"0900914160",2010-2014,Total,Number,Housing Units,10209
    Cheshire,"0900914160",2010-2014,Total,Number,Margins of Error,359
    Cheshire,"0900914160",2010-2014,Detached,Number,Housing Units,8055
    Cheshire,"0900914160",2010-2014,Detached,Number,Margins of Error,342
    Cheshire,"0900914160",2010-2014,Detached,Percent,Housing Units,78.9
    Cheshire,"0900914160",2010-2014,Detached,Percent,Margins of Error,2.1
    Derby,"0900919550",2011-2015,Total,Number,Housing Units,5429
    Derby,"0900919550",2011-2015,Total,Number,Margins of Error,379
    Derby,"0900919550",2011-2015,Detached,Number,Housing Units,1870
    Derby,"0900919550",2011-2015,Detached,Number,Margins of Error,223
    Derby,"0900919550",2011-2015,Detached,Percent,Housing Units,34.4
    Derby,"0900919550",2011-2015,Detached,Percent,Margins of Error,3.6
    Derby,"0900919550",2010-2014,Total,Number,Housing Units,5505
    Derby,"0900919550",2010-2014,Total,Number,Margins of Error,359
    Derby,"0900919550",2010-2014,Detached,Number,Housing Units,1959
    Derby,"0900919550",2010-2014,Detached,Number,Margins of Error,264
    Derby,"0900919550",2010-2014,Detached,Percent,Housing Units,35.6
    Derby,"0900919550",2010-2014,Detached,Percent,Margins of Error,4.4
    East Haven,"0900922910",2011-2015,Total,Number,Housing Units,12456
    East Haven,"0900922910",2011-2015,Total,Number,Margins of Error,360
    East Haven,"0900922910",2011-2015,Detached,Number,Housing Units,7847
    East Haven,"0900922910",2011-2015,Detached,Number,Margins of Error,380
    East Haven,"0900922910",2011-2015,Detached,Percent,Housing Units,63
    East Haven,"0900922910",2011-2015,Detached,Percent,Margins of Error,2.7
    East Haven,"0900922910",2010-2014,Total,Number,Housing Units,12356
    East Haven,"0900922910",2010-2014,Total,Number,Margins of Error,365
    East Haven,"0900922910",2010-2014,Detached,Number,Housing Units,7654
    East Haven,"0900922910",2010-2014,Detached,Number,Margins of Error,468
    East Haven,"0900922910",2010-2014,Detached,Percent,Housing Units,61.9
    East Haven,"0900922910",2010-2014,Detached,Percent,Margins of Error,2.8
    Guilford,"0900934950",2011-2015,Total,Number,Housing Units,9578
    Guilford,"0900934950",2011-2015,Total,Number,Margins of Error,263
    Guilford,"0900934950",2011-2015,Detached,Number,Housing Units,8127
    Guilford,"0900934950",2011-2015,Detached,Number,Margins of Error,310
    Guilford,"0900934950",2011-2015,Detached,Percent,Housing Units,84.9
    Guilford,"0900934950",2011-2015,Detached,Percent,Margins of Error,2
    Guilford,"0900934950",2010-2014,Total,Number,Housing Units,9725
    Guilford,"0900934950",2010-2014,Total,Number,Margins of Error,234
    Guilford,"0900934950",2010-2014,Detached,Number,Housing Units,8208
    Guilford,"0900934950",2010-2014,Detached,Number,Margins of Error,308
    Guilford,"0900934950",2010-2014,Detached,Percent,Housing Units,84.4
    Guilford,"0900934950",2010-2014,Detached,Percent,Margins of Error,2
    Hamden,"0900935650",2011-2015,Total,Number,Housing Units,25227
    Hamden,"0900935650",2011-2015,Total,Number,Margins of Error,579
    Hamden,"0900935650",2011-2015,Detached,Number,Housing Units,14377
    Hamden,"0900935650",2011-2015,Detached,Number,Margins of Error,481
    Hamden,"0900935650",2011-2015,Detached,Percent,Housing Units,57
    Hamden,"0900935650",2011-2015,Detached,Percent,Margins of Error,1.5
    Hamden,"0900935650",2010-2014,Total,Number,Housing Units,25465
    Hamden,"0900935650",2010-2014,Total,Number,Margins of Error,795
    Hamden,"0900935650",2010-2014,Detached,Number,Housing Units,14357
    Hamden,"0900935650",2010-2014,Detached,Number,Margins of Error,540
    Hamden,"0900935650",2010-2014,Detached,Percent,Housing Units,56.4
    Hamden,"0900935650",2010-2014,Detached,Percent,Margins of Error,1.4
    Madison,"0900944560",2011-2015,Total,Number,Housing Units,7968
    Madison,"0900944560",2011-2015,Total,Number,Margins of Error,295
    Madison,"0900944560",2011-2015,Detached,Number,Housing Units,7201
    Madison,"0900944560",2011-2015,Detached,Number,Margins of Error,297
    Madison,"0900944560",2011-2015,Detached,Percent,Housing Units,90.4
    Madison,"0900944560",2011-2015,Detached,Percent,Margins of Error,1.7
    Madison,"0900944560",2010-2014,Total,Number,Housing Units,7935
    Madison,"0900944560",2010-2014,Total,Number,Margins of Error,304
    Madison,"0900944560",2010-2014,Detached,Number,Housing Units,7175
    Madison,"0900944560",2010-2014,Detached,Number,Margins of Error,316
    Madison,"0900944560",2010-2014,Detached,Percent,Housing Units,90.4
    Madison,"0900944560",2010-2014,Detached,Percent,Margins of Error,2.3
    Meriden,"0900946520",2011-2015,Total,Number,Housing Units,28704
    Meriden,"0900946520",2011-2015,Total,Number,Margins of Error,777
    Meriden,"0900946520",2011-2015,Detached,Number,Housing Units,13988
    Meriden,"0900946520",2011-2015,Detached,Number,Margins of Error,545
    Meriden,"0900946520",2011-2015,Detached,Percent,Housing Units,48.7
    Meriden,"0900946520",2011-2015,Detached,Percent,Margins of Error,1.5
    Meriden,"0900946520",2010-2014,Total,Number,Housing Units,27611
    Meriden,"0900946520",2010-2014,Total,Number,Margins of Error,625
    Meriden,"0900946520",2010-2014,Detached,Number,Housing Units,13250
    Meriden,"0900946520",2010-2014,Detached,Number,Margins of Error,565
    Meriden,"0900946520",2010-2014,Detached,Percent,Housing Units,48
    Meriden,"0900946520",2010-2014,Detached,Percent,Margins of Error,1.6
    Middlebury,"0900946940",2011-2015,Total,Number,Housing Units,2870
    Middlebury,"0900946940",2011-2015,Total,Number,Margins of Error,103
    Middlebury,"0900946940",2011-2015,Detached,Number,Housing Units,2595
    Middlebury,"0900946940",2011-2015,Detached,Number,Margins of Error,110
    Middlebury,"0900946940",2011-2015,Detached,Percent,Housing Units,90.4
    Middlebury,"0900946940",2011-2015,Detached,Percent,Margins of Error,2.4
    Middlebury,"0900946940",2010-2014,Total,Number,Housing Units,2924
    Middlebury,"0900946940",2010-2014,Total,Number,Margins of Error,102
    Middlebury,"0900946940",2010-2014,Detached,Number,Housing Units,2584
    Middlebury,"0900946940",2010-2014,Detached,Number,Margins of Error,122
    Middlebury,"0900946940",2010-2014,Detached,Percent,Housing Units,88.4
    Middlebury,"0900946940",2010-2014,Detached,Percent,Margins of Error,3.5
    Milford,"0900947535",2011-2015,Total,Number,Housing Units,23092
    Milford,"0900947535",2011-2015,Total,Number,Margins of Error,434
    Milford,"0900947535",2011-2015,Detached,Number,Housing Units,16030
    Milford,"0900947535",2011-2015,Detached,Number,Margins of Error,454
    Milford,"0900947535",2011-2015,Detached,Percent,Housing Units,69.4
    Milford,"0900947535",2011-2015,Detached,Percent,Margins of Error,1.6
    Milford,"0900947535",2010-2014,Total,Number,Housing Units,22838
    Milford,"0900947535",2010-2014,Total,Number,Margins of Error,477
    Milford,"0900947535",2010-2014,Detached,Number,Housing Units,15956
    Milford,"0900947535",2010-2014,Detached,Number,Margins of Error,489
    Milford,"0900947535",2010-2014,Detached,Percent,Housing Units,69.9
    Milford,"0900947535",2010-2014,Detached,Percent,Margins of Error,1.5
    Naugatuck,"0900949950",2011-2015,Total,Number,Housing Units,12930
    Naugatuck,"0900949950",2011-2015,Total,Number,Margins of Error,454
    Naugatuck,"0900949950",2011-2015,Detached,Number,Housing Units,7479
    Naugatuck,"0900949950",2011-2015,Detached,Number,Margins of Error,457
    Naugatuck,"0900949950",2011-2015,Detached,Percent,Housing Units,57.8
    Naugatuck,"0900949950",2011-2015,Detached,Percent,Margins of Error,2.5
    Naugatuck,"0900949950",2010-2014,Total,Number,Housing Units,13103
    Naugatuck,"0900949950",2010-2014,Total,Number,Margins of Error,453
    Naugatuck,"0900949950",2010-2014,Detached,Number,Housing Units,7708
    Naugatuck,"0900949950",2010-2014,Detached,Number,Margins of Error,433
    Naugatuck,"0900949950",2010-2014,Detached,Percent,Housing Units,58.8
    Naugatuck,"0900949950",2010-2014,Detached,Percent,Margins of Error,3
    New Haven,"0900952070",2011-2015,Total,Number,Housing Units,56673
    New Haven,"0900952070",2011-2015,Total,Number,Margins of Error,1004
    New Haven,"0900952070",2011-2015,Detached,Number,Housing Units,11141
    New Haven,"0900952070",2011-2015,Detached,Number,Margins of Error,518
    New Haven,"0900952070",2011-2015,Detached,Percent,Housing Units,19.7
    New Haven,"0900952070",2011-2015,Detached,Percent,Margins of Error,0.9
    New Haven,"0900952070",2010-2014,Total,Number,Housing Units,57190
    New Haven,"0900952070",2010-2014,Total,Number,Margins of Error,1006
    New Haven,"0900952070",2010-2014,Detached,Number,Housing Units,11141
    New Haven,"0900952070",2010-2014,Detached,Number,Margins of Error,545
    New Haven,"0900952070",2010-2014,Detached,Percent,Housing Units,19.5
    New Haven,"0900952070",2010-2014,Detached,Percent,Margins of Error,0.9
    North Branford,"0900953890",2011-2015,Total,Number,Housing Units,5629
    North Branford,"0900953890",2011-2015,Total,Number,Margins of Error,177
    North Branford,"0900953890",2011-2015,Detached,Number,Housing Units,4571
    North Branford,"0900953890",2011-2015,Detached,Number,Margins of Error,244
    North Branford,"0900953890",2011-2015,Detached,Percent,Housing Units,81.2
    North Branford,"0900953890",2011-2015,Detached,Percent,Margins of Error,3.2
    North Branford,"0900953890",2010-2014,Total,Number,Housing Units,5775
    North Branford,"0900953890",2010-2014,Total,Number,Margins of Error,162
    North Branford,"0900953890",2010-2014,Detached,Number,Housing Units,4624
    North Branford,"0900953890",2010-2014,Detached,Number,Margins of Error,214
    North Branford,"0900953890",2010-2014,Detached,Percent,Housing Units,80.1
    North Branford,"0900953890",2010-2014,Detached,Percent,Margins of Error,2.9
    North Haven,"0900954870",2011-2015,Total,Number,Housing Units,9015
    North Haven,"0900954870",2011-2015,Total,Number,Margins of Error,332
    North Haven,"0900954870",2011-2015,Detached,Number,Housing Units,7439
    North Haven,"0900954870",2011-2015,Detached,Number,Margins of Error,373
    North Haven,"0900954870",2011-2015,Detached,Percent,Housing Units,82.5
    North Haven,"0900954870",2011-2015,Detached,Percent,Margins of Error,2.3
    North Haven,"0900954870",2010-2014,Total,Number,Housing Units,9054
    North Haven,"0900954870",2010-2014,Total,Number,Margins of Error,257
    North Haven,"0900954870",2010-2014,Detached,Number,Housing Units,7499
    North Haven,"0900954870",2010-2014,Detached,Number,Margins of Error,316
    North Haven,"0900954870",2010-2014,Detached,Percent,Housing Units,82.8
    North Haven,"0900954870",2010-2014,Detached,Percent,Margins of Error,2.4
    Orange,"0900957600",2011-2015,Total,Number,Housing Units,5031
    Orange,"0900957600",2011-2015,Total,Number,Margins of Error,165
    Orange,"0900957600",2011-2015,Detached,Number,Housing Units,4500
    Orange,"0900957600",2011-2015,Detached,Number,Margins of Error,174
    Orange,"0900957600",2011-2015,Detached,Percent,Housing Units,89.4
    Orange,"0900957600",2011-2015,Detached,Percent,Margins of Error,1.7
    Orange,"0900957600",2010-2014,Total,Number,Housing Units,5082
    Orange,"0900957600",2010-2014,Total,Number,Margins of Error,160
    Orange,"0900957600",2010-2014,Detached,Number,Housing Units,4519
    Orange,"0900957600",2010-2014,Detached,Number,Margins of Error,177
    Orange,"0900957600",2010-2014,Detached,Percent,Housing Units,88.9
    Orange,"0900957600",2010-2014,Detached,Percent,Margins of Error,2.2
    Oxford,"0900958300",2011-2015,Total,Number,Housing Units,4690
    Oxford,"0900958300",2011-2015,Total,Number,Margins of Error,209
    Oxford,"0900958300",2011-2015,Detached,Number,Housing Units,4409
    Oxford,"0900958300",2011-2015,Detached,Number,Margins of Error,234
    Oxford,"0900958300",2011-2015,Detached,Percent,Housing Units,94
    Oxford,"0900958300",2011-2015,Detached,Percent,Margins of Error,2.2
    Oxford,"0900958300",2010-2014,Total,Number,Housing Units,4681
    Oxford,"0900958300",2010-2014,Total,Number,Margins of Error,173
    Oxford,"0900958300",2010-2014,Detached,Number,Housing Units,4359
    Oxford,"0900958300",2010-2014,Detached,Number,Margins of Error,200
    Oxford,"0900958300",2010-2014,Detached,Percent,Housing Units,93.1
    Oxford,"0900958300",2010-2014,Detached,Percent,Margins of Error,2.1
    Prospect,"0900962290",2011-2015,Total,Number,Housing Units,3311
    Prospect,"0900962290",2011-2015,Total,Number,Margins of Error,139
    Prospect,"0900962290",2011-2015,Detached,Number,Housing Units,2753
    Prospect,"0900962290",2011-2015,Detached,Number,Margins of Error,147
    Prospect,"0900962290",2011-2015,Detached,Percent,Housing Units,83.1
    Prospect,"0900962290",2011-2015,Detached,Percent,Margins of Error,3.3
    Prospect,"0900962290",2010-2014,Total,Number,Housing Units,3293
    Prospect,"0900962290",2010-2014,Total,Number,Margins of Error,142
    Prospect,"0900962290",2010-2014,Detached,Number,Housing Units,2757
    Prospect,"0900962290",2010-2014,Detached,Number,Margins of Error,154
    Prospect,"0900962290",2010-2014,Detached,Percent,Housing Units,83.7
    Prospect,"0900962290",2010-2014,Detached,Percent,Margins of Error,3
    Seymour,"0900967610",2011-2015,Total,Number,Housing Units,6649
    Seymour,"0900967610",2011-2015,Total,Number,Margins of Error,315
    Seymour,"0900967610",2011-2015,Detached,Number,Housing Units,4507
    Seymour,"0900967610",2011-2015,Detached,Number,Margins of Error,301
    Seymour,"0900967610",2011-2015,Detached,Percent,Housing Units,67.8
    Seymour,"0900967610",2011-2015,Detached,Percent,Margins of Error,3
    Seymour,"0900967610",2010-2014,Total,Number,Housing Units,6590
    Seymour,"0900967610",2010-2014,Total,Number,Margins of Error,290
    Seymour,"0900967610",2010-2014,Detached,Number,Housing Units,4576
    Seymour,"0900967610",2010-2014,Detached,Number,Margins of Error,324
    Seymour,"0900967610",2010-2014,Detached,Percent,Housing Units,69.4
    Seymour,"0900967610",2010-2014,Detached,Percent,Margins of Error,4.1
    Southbury,"0900969640",2011-2015,Total,Number,Housing Units,8435
    Southbury,"0900969640",2011-2015,Total,Number,Margins of Error,285
    Southbury,"0900969640",2011-2015,Detached,Number,Housing Units,4931
    Southbury,"0900969640",2011-2015,Detached,Number,Margins of Error,254
    Southbury,"0900969640",2011-2015,Detached,Percent,Housing Units,58.5
    Southbury,"0900969640",2011-2015,Detached,Percent,Margins of Error,2.5
    Southbury,"0900969640",2010-2014,Total,Number,Housing Units,8565
    Southbury,"0900969640",2010-2014,Total,Number,Margins of Error,304
    Southbury,"0900969640",2010-2014,Detached,Number,Housing Units,5080
    Southbury,"0900969640",2010-2014,Detached,Number,Margins of Error,243
    Southbury,"0900969640",2010-2014,Detached,Percent,Housing Units,59.3
    Southbury,"0900969640",2010-2014,Detached,Percent,Margins of Error,2.2
    Wallingford,"0900978740",2011-2015,Total,Number,Housing Units,19280
    Wallingford,"0900978740",2011-2015,Total,Number,Margins of Error,384
    Wallingford,"0900978740",2011-2015,Detached,Number,Housing Units,11706
    Wallingford,"0900978740",2011-2015,Detached,Number,Margins of Error,350
    Wallingford,"0900978740",2011-2015,Detached,Percent,Housing Units,60.7
    Wallingford,"0900978740",2011-2015,Detached,Percent,Margins of Error,1.6
    Wallingford,"0900978740",2010-2014,Total,Number,Housing Units,18570
    Wallingford,"0900978740",2010-2014,Total,Number,Margins of Error,416
    Wallingford,"0900978740",2010-2014,Detached,Number,Housing Units,11362
    Wallingford,"0900978740",2010-2014,Detached,Number,Margins of Error,376
    Wallingford,"0900978740",2010-2014,Detached,Percent,Housing Units,61.2
    Wallingford,"0900978740",2010-2014,Detached,Percent,Margins of Error,1.7
    Waterbury,"0900980070",2011-2015,Total,Number,Housing Units,47356
    Waterbury,"0900980070",2011-2015,Total,Number,Margins of Error,807
    Waterbury,"0900980070",2011-2015,Detached,Number,Housing Units,17524
    Waterbury,"0900980070",2011-2015,Detached,Number,Margins of Error,686
    Waterbury,"0900980070",2011-2015,Detached,Percent,Housing Units,37
    Waterbury,"0900980070",2011-2015,Detached,Percent,Margins of Error,1.3
    Waterbury,"0900980070",2010-2014,Total,Number,Housing Units,47983
    Waterbury,"0900980070",2010-2014,Total,Number,Margins of Error,824
    Waterbury,"0900980070",2010-2014,Detached,Number,Housing Units,17250
    Waterbury,"0900980070",2010-2014,Detached,Number,Margins of Error,760
    Waterbury,"0900980070",2010-2014,Detached,Percent,Housing Units,36
    Waterbury,"0900980070",2010-2014,Detached,Percent,Margins of Error,1.5
    West Haven,"0900982870",2011-2015,Total,Number,Housing Units,22290
    West Haven,"0900982870",2011-2015,Total,Number,Margins of Error,674
    West Haven,"0900982870",2011-2015,Detached,Number,Housing Units,10516
    West Haven,"0900982870",2011-2015,Detached,Number,Margins of Error,548
    West Haven,"0900982870",2011-2015,Detached,Percent,Housing Units,47.2
    West Haven,"0900982870",2011-2015,Detached,Percent,Margins of Error,2.1
    West Haven,"0900982870",2010-2014,Total,Number,Housing Units,22245
    West Haven,"0900982870",2010-2014,Total,Number,Margins of Error,612
    West Haven,"0900982870",2010-2014,Detached,Number,Housing Units,10323
    West Haven,"0900982870",2010-2014,Detached,Number,Margins of Error,525
    West Haven,"0900982870",2010-2014,Detached,Percent,Housing Units,46.4
    West Haven,"0900982870",2010-2014,Detached,Percent,Margins of Error,2
    Wolcott,"0900987560",2011-2015,Total,Number,Housing Units,6043
    Wolcott,"0900987560",2011-2015,Total,Number,Margins of Error,265
    Wolcott,"0900987560",2011-2015,Detached,Number,Housing Units,5144
    Wolcott,"0900987560",2011-2015,Detached,Number,Margins of Error,291
    Wolcott,"0900987560",2011-2015,Detached,Percent,Housing Units,85.1
    Wolcott,"0900987560",2011-2015,Detached,Percent,Margins of Error,2.8
    Wolcott,"0900987560",2010-2014,Total,Number,Housing Units,6139
    Wolcott,"0900987560",2010-2014,Total,Number,Margins of Error,269
    Wolcott,"0900987560",2010-2014,Detached,Number,Housing Units,5213
    Wolcott,"0900987560",2010-2014,Detached,Number,Margins of Error,294
    Wolcott,"0900987560",2010-2014,Detached,Percent,Housing Units,84.9
    Wolcott,"0900987560",2010-2014,Detached,Percent,Margins of Error,3
    Woodbridge,"0900987700",2011-2015,Total,Number,Housing Units,3224
    Woodbridge,"0900987700",2011-2015,Total,Number,Margins of Error,172
    Woodbridge,"0900987700",2011-2015,Detached,Number,Housing Units,2946
    Woodbridge,"0900987700",2011-2015,Detached,Number,Margins of Error,164
    Woodbridge,"0900987700",2011-2015,Detached,Percent,Housing Units,91.4
    Woodbridge,"0900987700",2011-2015,Detached,Percent,Margins of Error,3
    Woodbridge,"0900987700",2010-2014,Total,Number,Housing Units,3222
    Woodbridge,"0900987700",2010-2014,Total,Number,Margins of Error,189
    Woodbridge,"0900987700",2010-2014,Detached,Number,Housing Units,2943
    Woodbridge,"0900987700",2010-2014,Detached,Number,Margins of Error,189
    Woodbridge,"0900987700",2010-2014,Detached,Percent,Housing Units,91.3
    Woodbridge,"0900987700",2010-2014,Detached,Percent,Margins of Error,3.5
    Bozrah,"0901106820",2011-2015,Total,Number,Housing Units,1087
    Bozrah,"0901106820",2011-2015,Total,Number,Margins of Error,73
    Bozrah,"0901106820",2011-2015,Detached,Number,Housing Units,1010
    Bozrah,"0901106820",2011-2015,Detached,Number,Margins of Error,69
    Bozrah,"0901106820",2011-2015,Detached,Percent,Housing Units,92.9
    Bozrah,"0901106820",2011-2015,Detached,Percent,Margins of Error,2.8
    Bozrah,"0901106820",2010-2014,Total,Number,Housing Units,1109
    Bozrah,"0901106820",2010-2014,Total,Number,Margins of Error,76
    Bozrah,"0901106820",2010-2014,Detached,Number,Housing Units,1013
    Bozrah,"0901106820",2010-2014,Detached,Number,Margins of Error,76
    Bozrah,"0901106820",2010-2014,Detached,Percent,Housing Units,91.3
    Bozrah,"0901106820",2010-2014,Detached,Percent,Margins of Error,3.1
    Colchester,"0901115910",2011-2015,Total,Number,Housing Units,6209
    Colchester,"0901115910",2011-2015,Total,Number,Margins of Error,209
    Colchester,"0901115910",2011-2015,Detached,Number,Housing Units,4734
    Colchester,"0901115910",2011-2015,Detached,Number,Margins of Error,247
    Colchester,"0901115910",2011-2015,Detached,Percent,Housing Units,76.2
    Colchester,"0901115910",2011-2015,Detached,Percent,Margins of Error,2.9
    Colchester,"0901115910",2010-2014,Total,Number,Housing Units,6268
    Colchester,"0901115910",2010-2014,Total,Number,Margins of Error,244
    Colchester,"0901115910",2010-2014,Detached,Number,Housing Units,4751
    Colchester,"0901115910",2010-2014,Detached,Number,Margins of Error,243
    Colchester,"0901115910",2010-2014,Detached,Percent,Housing Units,75.8
    Colchester,"0901115910",2010-2014,Detached,Percent,Margins of Error,3.1
    East Lyme,"0901123400",2011-2015,Total,Number,Housing Units,8226
    East Lyme,"0901123400",2011-2015,Total,Number,Margins of Error,255
    East Lyme,"0901123400",2011-2015,Detached,Number,Housing Units,6846
    East Lyme,"0901123400",2011-2015,Detached,Number,Margins of Error,304
    East Lyme,"0901123400",2011-2015,Detached,Percent,Housing Units,83.2
    East Lyme,"0901123400",2011-2015,Detached,Percent,Margins of Error,2.3
    East Lyme,"0901123400",2010-2014,Total,Number,Housing Units,8303
    East Lyme,"0901123400",2010-2014,Total,Number,Margins of Error,219
    East Lyme,"0901123400",2010-2014,Detached,Number,Housing Units,6949
    East Lyme,"0901123400",2010-2014,Detached,Number,Margins of Error,269
    East Lyme,"0901123400",2010-2014,Detached,Percent,Housing Units,83.7
    East Lyme,"0901123400",2010-2014,Detached,Percent,Margins of Error,1.9
    Franklin,"0901129910",2011-2015,Total,Number,Housing Units,772
    Franklin,"0901129910",2011-2015,Total,Number,Margins of Error,37
    Franklin,"0901129910",2011-2015,Detached,Number,Housing Units,723
    Franklin,"0901129910",2011-2015,Detached,Number,Margins of Error,37
    Franklin,"0901129910",2011-2015,Detached,Percent,Housing Units,93.7
    Franklin,"0901129910",2011-2015,Detached,Percent,Margins of Error,2.5
    Franklin,"0901129910",2010-2014,Total,Number,Housing Units,782
    Franklin,"0901129910",2010-2014,Total,Number,Margins of Error,39
    Franklin,"0901129910",2010-2014,Detached,Number,Housing Units,726
    Franklin,"0901129910",2010-2014,Detached,Number,Margins of Error,41
    Franklin,"0901129910",2010-2014,Detached,Percent,Housing Units,92.8
    Franklin,"0901129910",2010-2014,Detached,Percent,Margins of Error,2.9
    Griswold,"0901133900",2011-2015,Total,Number,Housing Units,4936
    Griswold,"0901133900",2011-2015,Total,Number,Margins of Error,305
    Griswold,"0901133900",2011-2015,Detached,Number,Housing Units,3165
    Griswold,"0901133900",2011-2015,Detached,Number,Margins of Error,270
    Griswold,"0901133900",2011-2015,Detached,Percent,Housing Units,64.1
    Griswold,"0901133900",2011-2015,Detached,Percent,Margins of Error,4.6
    Griswold,"0901133900",2010-2014,Total,Number,Housing Units,4929
    Griswold,"0901133900",2010-2014,Total,Number,Margins of Error,282
    Griswold,"0901133900",2010-2014,Detached,Number,Housing Units,3261
    Griswold,"0901133900",2010-2014,Detached,Number,Margins of Error,286
    Griswold,"0901133900",2010-2014,Detached,Percent,Housing Units,66.2
    Griswold,"0901133900",2010-2014,Detached,Percent,Margins of Error,4.9
    Groton,"0901134250",2011-2015,Total,Number,Housing Units,18506
    Groton,"0901134250",2011-2015,Total,Number,Margins of Error,526
    Groton,"0901134250",2011-2015,Detached,Number,Housing Units,8568
    Groton,"0901134250",2011-2015,Detached,Number,Margins of Error,418
    Groton,"0901134250",2011-2015,Detached,Percent,Housing Units,46.3
    Groton,"0901134250",2011-2015,Detached,Percent,Margins of Error,1.7
    Groton,"0901134250",2010-2014,Total,Number,Housing Units,18348
    Groton,"0901134250",2010-2014,Total,Number,Margins of Error,475
    Groton,"0901134250",2010-2014,Detached,Number,Housing Units,8442
    Groton,"0901134250",2010-2014,Detached,Number,Margins of Error,361
    Groton,"0901134250",2010-2014,Detached,Percent,Housing Units,46
    Groton,"0901134250",2010-2014,Detached,Percent,Margins of Error,1.6
    Lebanon,"0901142390",2011-2015,Total,Number,Housing Units,3097
    Lebanon,"0901142390",2011-2015,Total,Number,Margins of Error,172
    Lebanon,"0901142390",2011-2015,Detached,Number,Housing Units,2898
    Lebanon,"0901142390",2011-2015,Detached,Number,Margins of Error,222
    Lebanon,"0901142390",2011-2015,Detached,Percent,Housing Units,93.6
    Lebanon,"0901142390",2011-2015,Detached,Percent,Margins of Error,3.6
    Lebanon,"0901142390",2010-2014,Total,Number,Housing Units,3151
    Lebanon,"0901142390",2010-2014,Total,Number,Margins of Error,161
    Lebanon,"0901142390",2010-2014,Detached,Number,Housing Units,2938
    Lebanon,"0901142390",2010-2014,Detached,Number,Margins of Error,192
    Lebanon,"0901142390",2010-2014,Detached,Percent,Housing Units,93.2
    Lebanon,"0901142390",2010-2014,Detached,Percent,Margins of Error,3.4
    Ledyard,"0901142600",2011-2015,Total,Number,Housing Units,6160
    Ledyard,"0901142600",2011-2015,Total,Number,Margins of Error,220
    Ledyard,"0901142600",2011-2015,Detached,Number,Housing Units,5273
    Ledyard,"0901142600",2011-2015,Detached,Number,Margins of Error,236
    Ledyard,"0901142600",2011-2015,Detached,Percent,Housing Units,85.6
    Ledyard,"0901142600",2011-2015,Detached,Percent,Margins of Error,3.1
    Ledyard,"0901142600",2010-2014,Total,Number,Housing Units,6124
    Ledyard,"0901142600",2010-2014,Total,Number,Margins of Error,228
    Ledyard,"0901142600",2010-2014,Detached,Number,Housing Units,5389
    Ledyard,"0901142600",2010-2014,Detached,Number,Margins of Error,272
    Ledyard,"0901142600",2010-2014,Detached,Percent,Housing Units,88
    Ledyard,"0901142600",2010-2014,Detached,Percent,Margins of Error,3.2
    Lisbon,"0901143230",2011-2015,Total,Number,Housing Units,1640
    Lisbon,"0901143230",2011-2015,Total,Number,Margins of Error,95
    Lisbon,"0901143230",2011-2015,Detached,Number,Housing Units,1436
    Lisbon,"0901143230",2011-2015,Detached,Number,Margins of Error,100
    Lisbon,"0901143230",2011-2015,Detached,Percent,Housing Units,87.6
    Lisbon,"0901143230",2011-2015,Detached,Percent,Margins of Error,4.1
    Lisbon,"0901143230",2010-2014,Total,Number,Housing Units,1724
    Lisbon,"0901143230",2010-2014,Total,Number,Margins of Error,122
    Lisbon,"0901143230",2010-2014,Detached,Number,Housing Units,1529
    Lisbon,"0901143230",2010-2014,Detached,Number,Margins of Error,132
    Lisbon,"0901143230",2010-2014,Detached,Percent,Housing Units,88.7
    Lisbon,"0901143230",2010-2014,Detached,Percent,Margins of Error,3.8
    Lyme,"0901144210",2011-2015,Total,Number,Housing Units,1203
    Lyme,"0901144210",2011-2015,Total,Number,Margins of Error,55
    Lyme,"0901144210",2011-2015,Detached,Number,Housing Units,1169
    Lyme,"0901144210",2011-2015,Detached,Number,Margins of Error,62
    Lyme,"0901144210",2011-2015,Detached,Percent,Housing Units,97.2
    Lyme,"0901144210",2011-2015,Detached,Percent,Margins of Error,2.5
    Lyme,"0901144210",2010-2014,Total,Number,Housing Units,1227
    Lyme,"0901144210",2010-2014,Total,Number,Margins of Error,60
    Lyme,"0901144210",2010-2014,Detached,Number,Housing Units,1193
    Lyme,"0901144210",2010-2014,Detached,Number,Margins of Error,61
    Lyme,"0901144210",2010-2014,Detached,Percent,Housing Units,97.2
    Lyme,"0901144210",2010-2014,Detached,Percent,Margins of Error,2
    Montville,"0901148900",2011-2015,Total,Number,Housing Units,7589
    Montville,"0901148900",2011-2015,Total,Number,Margins of Error,350
    Montville,"0901148900",2011-2015,Detached,Number,Housing Units,5929
    Montville,"0901148900",2011-2015,Detached,Number,Margins of Error,341
    Montville,"0901148900",2011-2015,Detached,Percent,Housing Units,78.1
    Montville,"0901148900",2011-2015,Detached,Percent,Margins of Error,3.2
    Montville,"0901148900",2010-2014,Total,Number,Housing Units,7459
    Montville,"0901148900",2010-2014,Total,Number,Margins of Error,325
    Montville,"0901148900",2010-2014,Detached,Number,Housing Units,5793
    Montville,"0901148900",2010-2014,Detached,Number,Margins of Error,317
    Montville,"0901148900",2010-2014,Detached,Percent,Housing Units,77.7
    Montville,"0901148900",2010-2014,Detached,Percent,Margins of Error,3
    New London,"0901152350",2011-2015,Total,Number,Housing Units,12254
    New London,"0901152350",2011-2015,Total,Number,Margins of Error,559
    New London,"0901152350",2011-2015,Detached,Number,Housing Units,3855
    New London,"0901152350",2011-2015,Detached,Number,Margins of Error,367
    New London,"0901152350",2011-2015,Detached,Percent,Housing Units,31.5
    New London,"0901152350",2011-2015,Detached,Percent,Margins of Error,2.9
    New London,"0901152350",2010-2014,Total,Number,Housing Units,11582
    New London,"0901152350",2010-2014,Total,Number,Margins of Error,490
    New London,"0901152350",2010-2014,Detached,Number,Housing Units,3665
    New London,"0901152350",2010-2014,Detached,Number,Margins of Error,358
    New London,"0901152350",2010-2014,Detached,Percent,Housing Units,31.6
    New London,"0901152350",2010-2014,Detached,Percent,Margins of Error,2.6
    North Stonington,"0901155500",2011-2015,Total,Number,Housing Units,2222
    North Stonington,"0901155500",2011-2015,Total,Number,Margins of Error,176
    North Stonington,"0901155500",2011-2015,Detached,Number,Housing Units,2045
    North Stonington,"0901155500",2011-2015,Detached,Number,Margins of Error,209
    North Stonington,"0901155500",2011-2015,Detached,Percent,Housing Units,92
    North Stonington,"0901155500",2011-2015,Detached,Percent,Margins of Error,4.1
    North Stonington,"0901155500",2010-2014,Total,Number,Housing Units,2256
    North Stonington,"0901155500",2010-2014,Total,Number,Margins of Error,114
    North Stonington,"0901155500",2010-2014,Detached,Number,Housing Units,2081
    North Stonington,"0901155500",2010-2014,Detached,Number,Margins of Error,169
    North Stonington,"0901155500",2010-2014,Detached,Percent,Housing Units,92.2
    North Stonington,"0901155500",2010-2014,Detached,Percent,Margins of Error,4.7
    Norwich,"0901156270",2011-2015,Total,Number,Housing Units,18310
    Norwich,"0901156270",2011-2015,Total,Number,Margins of Error,620
    Norwich,"0901156270",2011-2015,Detached,Number,Housing Units,7678
    Norwich,"0901156270",2011-2015,Detached,Number,Margins of Error,507
    Norwich,"0901156270",2011-2015,Detached,Percent,Housing Units,41.9
    Norwich,"0901156270",2011-2015,Detached,Percent,Margins of Error,2.4
    Norwich,"0901156270",2010-2014,Total,Number,Housing Units,18241
    Norwich,"0901156270",2010-2014,Total,Number,Margins of Error,532
    Norwich,"0901156270",2010-2014,Detached,Number,Housing Units,7793
    Norwich,"0901156270",2010-2014,Detached,Number,Margins of Error,442
    Norwich,"0901156270",2010-2014,Detached,Percent,Housing Units,42.7
    Norwich,"0901156270",2010-2014,Detached,Percent,Margins of Error,2
    Old Lyme,"0901157040",2011-2015,Total,Number,Housing Units,4953
    Old Lyme,"0901157040",2011-2015,Total,Number,Margins of Error,214
    Old Lyme,"0901157040",2011-2015,Detached,Number,Housing Units,4491
    Old Lyme,"0901157040",2011-2015,Detached,Number,Margins of Error,236
    Old Lyme,"0901157040",2011-2015,Detached,Percent,Housing Units,90.7
    Old Lyme,"0901157040",2011-2015,Detached,Percent,Margins of Error,3.2
    Old Lyme,"0901157040",2010-2014,Total,Number,Housing Units,5003
    Old Lyme,"0901157040",2010-2014,Total,Number,Margins of Error,207
    Old Lyme,"0901157040",2010-2014,Detached,Number,Housing Units,4481
    Old Lyme,"0901157040",2010-2014,Detached,Number,Margins of Error,210
    Old Lyme,"0901157040",2010-2014,Detached,Percent,Housing Units,89.6
    Old Lyme,"0901157040",2010-2014,Detached,Percent,Margins of Error,3.4
    Preston,"0901162150",2011-2015,Total,Number,Housing Units,2042
    Preston,"0901162150",2011-2015,Total,Number,Margins of Error,117
    Preston,"0901162150",2011-2015,Detached,Number,Housing Units,1908
    Preston,"0901162150",2011-2015,Detached,Number,Margins of Error,129
    Preston,"0901162150",2011-2015,Detached,Percent,Housing Units,93.4
    Preston,"0901162150",2011-2015,Detached,Percent,Margins of Error,3
    Preston,"0901162150",2010-2014,Total,Number,Housing Units,2086
    Preston,"0901162150",2010-2014,Total,Number,Margins of Error,129
    Preston,"0901162150",2010-2014,Detached,Number,Housing Units,1942
    Preston,"0901162150",2010-2014,Detached,Number,Margins of Error,151
    Preston,"0901162150",2010-2014,Detached,Percent,Housing Units,93.1
    Preston,"0901162150",2010-2014,Detached,Percent,Margins of Error,3.5
    Salem,"0901166210",2011-2015,Total,Number,Housing Units,1672
    Salem,"0901166210",2011-2015,Total,Number,Margins of Error,99
    Salem,"0901166210",2011-2015,Detached,Number,Housing Units,1565
    Salem,"0901166210",2011-2015,Detached,Number,Margins of Error,100
    Salem,"0901166210",2011-2015,Detached,Percent,Housing Units,93.6
    Salem,"0901166210",2011-2015,Detached,Percent,Margins of Error,3.2
    Salem,"0901166210",2010-2014,Total,Number,Housing Units,1693
    Salem,"0901166210",2010-2014,Total,Number,Margins of Error,95
    Salem,"0901166210",2010-2014,Detached,Number,Housing Units,1567
    Salem,"0901166210",2010-2014,Detached,Number,Margins of Error,99
    Salem,"0901166210",2010-2014,Detached,Percent,Housing Units,92.6
    Salem,"0901166210",2010-2014,Detached,Percent,Margins of Error,4.2
    Sprague,"0901171670",2011-2015,Total,Number,Housing Units,1294
    Sprague,"0901171670",2011-2015,Total,Number,Margins of Error,93
    Sprague,"0901171670",2011-2015,Detached,Number,Housing Units,770
    Sprague,"0901171670",2011-2015,Detached,Number,Margins of Error,95
    Sprague,"0901171670",2011-2015,Detached,Percent,Housing Units,59.5
    Sprague,"0901171670",2011-2015,Detached,Percent,Margins of Error,5.4
    Sprague,"0901171670",2010-2014,Total,Number,Housing Units,1357
    Sprague,"0901171670",2010-2014,Total,Number,Margins of Error,92
    Sprague,"0901171670",2010-2014,Detached,Number,Housing Units,799
    Sprague,"0901171670",2010-2014,Detached,Number,Margins of Error,95
    Sprague,"0901171670",2010-2014,Detached,Percent,Housing Units,58.9
    Sprague,"0901171670",2010-2014,Detached,Percent,Margins of Error,6.3
    Stonington,"0901173770",2011-2015,Total,Number,Housing Units,9281
    Stonington,"0901173770",2011-2015,Total,Number,Margins of Error,317
    Stonington,"0901173770",2011-2015,Detached,Number,Housing Units,6349
    Stonington,"0901173770",2011-2015,Detached,Number,Margins of Error,283
    Stonington,"0901173770",2011-2015,Detached,Percent,Housing Units,68.4
    Stonington,"0901173770",2011-2015,Detached,Percent,Margins of Error,2.3
    Stonington,"0901173770",2010-2014,Total,Number,Housing Units,9477
    Stonington,"0901173770",2010-2014,Total,Number,Margins of Error,244
    Stonington,"0901173770",2010-2014,Detached,Number,Housing Units,6488
    Stonington,"0901173770",2010-2014,Detached,Number,Margins of Error,255
    Stonington,"0901173770",2010-2014,Detached,Percent,Housing Units,68.5
    Stonington,"0901173770",2010-2014,Detached,Percent,Margins of Error,2.4
    Voluntown,"0901178600",2011-2015,Total,Number,Housing Units,1077
    Voluntown,"0901178600",2011-2015,Total,Number,Margins of Error,74
    Voluntown,"0901178600",2011-2015,Detached,Number,Housing Units,997
    Voluntown,"0901178600",2011-2015,Detached,Number,Margins of Error,72
    Voluntown,"0901178600",2011-2015,Detached,Percent,Housing Units,92.6
    Voluntown,"0901178600",2011-2015,Detached,Percent,Margins of Error,2.6
    Voluntown,"0901178600",2010-2014,Total,Number,Housing Units,1123
    Voluntown,"0901178600",2010-2014,Total,Number,Margins of Error,71
    Voluntown,"0901178600",2010-2014,Detached,Number,Housing Units,1022
    Voluntown,"0901178600",2010-2014,Detached,Number,Margins of Error,70
    Voluntown,"0901178600",2010-2014,Detached,Percent,Housing Units,91
    Voluntown,"0901178600",2010-2014,Detached,Percent,Margins of Error,3.5
    Waterford,"0901180280",2011-2015,Total,Number,Housing Units,8728
    Waterford,"0901180280",2011-2015,Total,Number,Margins of Error,252
    Waterford,"0901180280",2011-2015,Detached,Number,Housing Units,7612
    Waterford,"0901180280",2011-2015,Detached,Number,Margins of Error,247
    Waterford,"0901180280",2011-2015,Detached,Percent,Housing Units,87.2
    Waterford,"0901180280",2011-2015,Detached,Percent,Margins of Error,1.8
    Waterford,"0901180280",2010-2014,Total,Number,Housing Units,8854
    Waterford,"0901180280",2010-2014,Total,Number,Margins of Error,255
    Waterford,"0901180280",2010-2014,Detached,Number,Housing Units,7594
    Waterford,"0901180280",2010-2014,Detached,Number,Margins of Error,281
    Waterford,"0901180280",2010-2014,Detached,Percent,Housing Units,85.8
    Waterford,"0901180280",2010-2014,Detached,Percent,Margins of Error,2.2
    Andover,"0901301080",2011-2015,Total,Number,Housing Units,1234
    Andover,"0901301080",2011-2015,Total,Number,Margins of Error,92
    Andover,"0901301080",2011-2015,Detached,Number,Housing Units,1138
    Andover,"0901301080",2011-2015,Detached,Number,Margins of Error,92
    Andover,"0901301080",2011-2015,Detached,Percent,Housing Units,92.2
    Andover,"0901301080",2011-2015,Detached,Percent,Margins of Error,3.4
    Andover,"0901301080",2010-2014,Total,Number,Housing Units,1195
    Andover,"0901301080",2010-2014,Total,Number,Margins of Error,78
    Andover,"0901301080",2010-2014,Detached,Number,Housing Units,1095
    Andover,"0901301080",2010-2014,Detached,Number,Margins of Error,83
    Andover,"0901301080",2010-2014,Detached,Percent,Housing Units,91.6
    Andover,"0901301080",2010-2014,Detached,Percent,Margins of Error,3.4
    Bolton,"0901306260",2011-2015,Total,Number,Housing Units,2131
    Bolton,"0901306260",2011-2015,Total,Number,Margins of Error,102
    Bolton,"0901306260",2011-2015,Detached,Number,Housing Units,1914
    Bolton,"0901306260",2011-2015,Detached,Number,Margins of Error,104
    Bolton,"0901306260",2011-2015,Detached,Percent,Housing Units,89.8
    Bolton,"0901306260",2011-2015,Detached,Percent,Margins of Error,3.4
    Bolton,"0901306260",2010-2014,Total,Number,Housing Units,2141
    Bolton,"0901306260",2010-2014,Total,Number,Margins of Error,121
    Bolton,"0901306260",2010-2014,Detached,Number,Housing Units,1857
    Bolton,"0901306260",2010-2014,Detached,Number,Margins of Error,125
    Bolton,"0901306260",2010-2014,Detached,Percent,Housing Units,86.7
    Bolton,"0901306260",2010-2014,Detached,Percent,Margins of Error,4.1
    Columbia,"0901316400",2011-2015,Total,Number,Housing Units,2159
    Columbia,"0901316400",2011-2015,Total,Number,Margins of Error,152
    Columbia,"0901316400",2011-2015,Detached,Number,Housing Units,1888
    Columbia,"0901316400",2011-2015,Detached,Number,Margins of Error,151
    Columbia,"0901316400",2011-2015,Detached,Percent,Housing Units,87.4
    Columbia,"0901316400",2011-2015,Detached,Percent,Margins of Error,4.1
    Columbia,"0901316400",2010-2014,Total,Number,Housing Units,2210
    Columbia,"0901316400",2010-2014,Total,Number,Margins of Error,141
    Columbia,"0901316400",2010-2014,Detached,Number,Housing Units,1991
    Columbia,"0901316400",2010-2014,Detached,Number,Margins of Error,141
    Columbia,"0901316400",2010-2014,Detached,Percent,Housing Units,90.1
    Columbia,"0901316400",2010-2014,Detached,Percent,Margins of Error,3.8
    Coventry,"0901317800",2011-2015,Total,Number,Housing Units,4965
    Coventry,"0901317800",2011-2015,Total,Number,Margins of Error,211
    Coventry,"0901317800",2011-2015,Detached,Number,Housing Units,4528
    Coventry,"0901317800",2011-2015,Detached,Number,Margins of Error,229
    Coventry,"0901317800",2011-2015,Detached,Percent,Housing Units,91.2
    Coventry,"0901317800",2011-2015,Detached,Percent,Margins of Error,2.7
    Coventry,"0901317800",2010-2014,Total,Number,Housing Units,5112
    Coventry,"0901317800",2010-2014,Total,Number,Margins of Error,188
    Coventry,"0901317800",2010-2014,Detached,Number,Housing Units,4604
    Coventry,"0901317800",2010-2014,Detached,Number,Margins of Error,223
    Coventry,"0901317800",2010-2014,Detached,Percent,Housing Units,90.1
    Coventry,"0901317800",2010-2014,Detached,Percent,Margins of Error,2.5
    Ellington,"0901325360",2011-2015,Total,Number,Housing Units,6669
    Ellington,"0901325360",2011-2015,Total,Number,Margins of Error,281
    Ellington,"0901325360",2011-2015,Detached,Number,Housing Units,4255
    Ellington,"0901325360",2011-2015,Detached,Number,Margins of Error,251
    Ellington,"0901325360",2011-2015,Detached,Percent,Housing Units,63.8
    Ellington,"0901325360",2011-2015,Detached,Percent,Margins of Error,3.2
    Ellington,"0901325360",2010-2014,Total,Number,Housing Units,6573
    Ellington,"0901325360",2010-2014,Total,Number,Margins of Error,244
    Ellington,"0901325360",2010-2014,Detached,Number,Housing Units,4297
    Ellington,"0901325360",2010-2014,Detached,Number,Margins of Error,301
    Ellington,"0901325360",2010-2014,Detached,Percent,Housing Units,65.4
    Ellington,"0901325360",2010-2014,Detached,Percent,Margins of Error,3.5
    Hebron,"0901337910",2011-2015,Total,Number,Housing Units,3622
    Hebron,"0901337910",2011-2015,Total,Number,Margins of Error,165
    Hebron,"0901337910",2011-2015,Detached,Number,Housing Units,3310
    Hebron,"0901337910",2011-2015,Detached,Number,Margins of Error,182
    Hebron,"0901337910",2011-2015,Detached,Percent,Housing Units,91.4
    Hebron,"0901337910",2011-2015,Detached,Percent,Margins of Error,3.1
    Hebron,"0901337910",2010-2014,Total,Number,Housing Units,3564
    Hebron,"0901337910",2010-2014,Total,Number,Margins of Error,171
    Hebron,"0901337910",2010-2014,Detached,Number,Housing Units,3273
    Hebron,"0901337910",2010-2014,Detached,Number,Margins of Error,196
    Hebron,"0901337910",2010-2014,Detached,Percent,Housing Units,91.8
    Hebron,"0901337910",2010-2014,Detached,Percent,Margins of Error,2.8
    Mansfield,"0901344910",2011-2015,Total,Number,Housing Units,6119
    Mansfield,"0901344910",2011-2015,Total,Number,Margins of Error,561
    Mansfield,"0901344910",2011-2015,Detached,Number,Housing Units,3466
    Mansfield,"0901344910",2011-2015,Detached,Number,Margins of Error,325
    Mansfield,"0901344910",2011-2015,Detached,Percent,Housing Units,56.6
    Mansfield,"0901344910",2011-2015,Detached,Percent,Margins of Error,3.2
    Mansfield,"0901344910",2010-2014,Total,Number,Housing Units,6199
    Mansfield,"0901344910",2010-2014,Total,Number,Margins of Error,536
    Mansfield,"0901344910",2010-2014,Detached,Number,Housing Units,3791
    Mansfield,"0901344910",2010-2014,Detached,Number,Margins of Error,387
    Mansfield,"0901344910",2010-2014,Detached,Percent,Housing Units,61.2
    Mansfield,"0901344910",2010-2014,Detached,Percent,Margins of Error,3.5
    Somers,"0901369220",2011-2015,Total,Number,Housing Units,3597
    Somers,"0901369220",2011-2015,Total,Number,Margins of Error,163
    Somers,"0901369220",2011-2015,Detached,Number,Housing Units,3175
    Somers,"0901369220",2011-2015,Detached,Number,Margins of Error,144
    Somers,"0901369220",2011-2015,Detached,Percent,Housing Units,88.3
    Somers,"0901369220",2011-2015,Detached,Percent,Margins of Error,2.5
    Somers,"0901369220",2010-2014,Total,Number,Housing Units,3546
    Somers,"0901369220",2010-2014,Total,Number,Margins of Error,192
    Somers,"0901369220",2010-2014,Detached,Number,Housing Units,3176
    Somers,"0901369220",2010-2014,Detached,Number,Margins of Error,181
    Somers,"0901369220",2010-2014,Detached,Percent,Housing Units,89.6
    Somers,"0901369220",2010-2014,Detached,Percent,Margins of Error,2.6
    Stafford,"0901372090",2011-2015,Total,Number,Housing Units,5428
    Stafford,"0901372090",2011-2015,Total,Number,Margins of Error,243
    Stafford,"0901372090",2011-2015,Detached,Number,Housing Units,3886
    Stafford,"0901372090",2011-2015,Detached,Number,Margins of Error,256
    Stafford,"0901372090",2011-2015,Detached,Percent,Housing Units,71.6
    Stafford,"0901372090",2011-2015,Detached,Percent,Margins of Error,3.2
    Stafford,"0901372090",2010-2014,Total,Number,Housing Units,5286
    Stafford,"0901372090",2010-2014,Total,Number,Margins of Error,225
    Stafford,"0901372090",2010-2014,Detached,Number,Housing Units,3792
    Stafford,"0901372090",2010-2014,Detached,Number,Margins of Error,256
    Stafford,"0901372090",2010-2014,Detached,Percent,Housing Units,71.7
    Stafford,"0901372090",2010-2014,Detached,Percent,Margins of Error,3.3
    Tolland,"0901376290",2011-2015,Total,Number,Housing Units,5439
    Tolland,"0901376290",2011-2015,Total,Number,Margins of Error,185
    Tolland,"0901376290",2011-2015,Detached,Number,Housing Units,5150
    Tolland,"0901376290",2011-2015,Detached,Number,Margins of Error",201
    Tolland,"0901376290",2011-2015,Detached,Percent,Housing Units,94.7
    Tolland,"0901376290",2011-2015,Detached,Percent,Margins of Error,1.9
    Tolland,"0901376290",2010-2014,Total,Number,Housing Units,5545
    Tolland,"0901376290",2010-2014,Total,Number,Margins of Error,196
    Tolland,"0901376290",2010-2014,Detached,Number,Housing Units,5197
    Tolland,"0901376290",2010-2014,Detached,Number,Margins of Error,214
    Tolland,"0901376290",2010-2014,Detached,Percent,Housing Units,93.7
    Tolland,"0901376290",2010-2014,Detached,Percent,Margins of Error,1.9
    Union,"0901377830",2011-2015,Total,Number,Housing Units,370
    Union,"0901377830",2011-2015,Total,Number,Margins of Error,44
    Union,"0901377830",2011-2015,Detached,Number,Housing Units,363
    Union,"0901377830",2011-2015,Detached,Number,Margins of Error,44
    Union,"0901377830",2011-2015,Detached,Percent,Housing Units,98.1
    Union,"0901377830",2011-2015,Detached,Percent,Margins of Error,2.3
    Union,"0901377830",2010-2014,Total,Number,Housing Units,375
    Union,"0901377830",2010-2014,Total,Number,Margins of Error,58
    Union,"0901377830",2010-2014,Detached,Number,Housing Units,361
    Union,"0901377830",2010-2014,Detached,Number,Margins of Error,56
    Union,"0901377830",2010-2014,Detached,Percent,Housing Units,96.3
    Union,"0901377830",2010-2014,Detached,Percent,Margins of Error,3.3
    Vernon,"0901378250",2011-2015,Total,Number,Housing Units,14124
    Vernon,"0901378250",2011-2015,Total,Number,Margins of Error,342
    Vernon,"0901378250",2011-2015,Detached,Number,Housing Units,6412
    Vernon,"0901378250",2011-2015,Detached,Number,Margins of Error,341
    Vernon,"0901378250",2011-2015,Detached,Percent,Housing Units,45.4
    Vernon,"0901378250",2011-2015,Detached,Percent,Margins of Error,2.2
    Vernon,"0901378250",2010-2014,Total,Number,Housing Units,14076
    Vernon,"0901378250",2010-2014,Total,Number,Margins of Error,373
    Vernon,"0901378250",2010-2014,Detached,Number,Housing Units,6383
    Vernon,"0901378250",2010-2014,Detached,Number,Margins of Error,317
    Vernon,"0901378250",2010-2014,Detached,Percent,Housing Units,45.3
    Vernon,"0901378250",2010-2014,Detached,Percent,Margins of Error,2.1
    Willington,"0901385950",2011-2015,Total,Number,Housing Units,2526
    Willington,"0901385950",2011-2015,Total,Number,Margins of Error,190
    Willington,"0901385950",2011-2015,Detached,Number,Housing Units,1661
    Willington,"0901385950",2011-2015,Detached,Number,Margins of Error,226
    Willington,"0901385950",2011-2015,Detached,Percent,Housing Units,65.8
    Willington,"0901385950",2011-2015,Detached,Percent,Margins of Error,7
    Willington,"0901385950",2010-2014,Total,Number,Housing Units,2457
    Willington,"0901385950",2010-2014,Total,Number,Margins of Error,200
    Willington,"0901385950",2010-2014,Detached,Number,Housing Units,1625
    Willington,"0901385950",2010-2014,Detached,Number,Margins of Error,203
    Willington,"0901385950",2010-2014,Detached,Percent,Housing Units,66.1
    Willington,"0901385950",2010-2014,Detached,Percent,Margins of Error,6.7
    Ashford,"0901501430",2011-2015,Total,Number,Housing Units,1898
    Ashford,"0901501430",2011-2015,Total,Number,Margins of Error,114
    Ashford,"0901501430",2011-2015,Detached,Number,Housing Units,1595
    Ashford,"0901501430",2011-2015,Detached,Number,Margins of Error,126
    Ashford,"0901501430",2011-2015,Detached,Percent,Housing Units,84
    Ashford,"0901501430",2011-2015,Detached,Percent,Margins of Error,3.6
    Ashford,"0901501430",2010-2014,Total,Number,Housing Units,1883
    Ashford,"0901501430",2010-2014,Total,Number,Margins of Error,109
    Ashford,"0901501430",2010-2014,Detached,Number,Housing Units,1554
    Ashford,"0901501430",2010-2014,Detached,Number,Margins of Error,125
    Ashford,"0901501430",2010-2014,Detached,Percent,Housing Units,82.5
    Ashford,"0901501430",2010-2014,Detached,Percent,Margins of Error,4.1
    Brooklyn,"0901509190",2011-2015,Total,Number,Housing Units,3160
    Brooklyn,"0901509190",2011-2015,Total,Number,Margins of Error,216
    Brooklyn,"0901509190",2011-2015,Detached,Number,Housing Units,2353
    Brooklyn,"0901509190",2011-2015,Detached,Number,Margins of Error,254
    Brooklyn,"0901509190",2011-2015,Detached,Percent,Housing Units,74.5
    Brooklyn,"0901509190",2011-2015,Detached,Percent,Margins of Error,5.7
    Brooklyn,"0901509190",2010-2014,Total,Number,Housing Units,3188
    Brooklyn,"0901509190",2010-2014,Total,Number,Margins of Error,209
    Brooklyn,"0901509190",2010-2014,Detached,Number,Housing Units,2341
    Brooklyn,"0901509190",2010-2014,Detached,Number,Margins of Error,227
    Brooklyn,"0901509190",2010-2014,Detached,Percent,Housing Units,73.4
    Brooklyn,"0901509190",2010-2014,Detached,Percent,Margins of Error,5.6
    Canterbury,"0901512130",2011-2015,Total,Number,Housing Units,2026
    Canterbury,"0901512130",2011-2015,Total,Number,Margins of Error,102
    Canterbury,"0901512130",2011-2015,Detached,Number,Housing Units,1868
    Canterbury,"0901512130",2011-2015,Detached,Number,Margins of Error,109
    Canterbury,"0901512130",2011-2015,Detached,Percent,Housing Units,92.2
    Canterbury,"0901512130",2011-2015,Detached,Percent,Margins of Error,3
    Canterbury,"0901512130",2010-2014,Total,Number,Housing Units,2031
    Canterbury,"0901512130",2010-2014,Total,Number,Margins of Error,109
    Canterbury,"0901512130",2010-2014,Detached,Number,Housing Units,1844
    Canterbury,"0901512130",2010-2014,Detached,Number,Margins of Error,109
    Canterbury,"0901512130",2010-2014,Detached,Percent,Housing Units,90.8
    Canterbury,"0901512130",2010-2014,Detached,Percent,Margins of Error,3.6
    Chaplin,"0901513810",2011-2015,Total,Number,Housing Units,938
    Chaplin,"0901513810",2011-2015,Total,Number,Margins of Error,39
    Chaplin,"0901513810",2011-2015,Detached,Number,Housing Units,749
    Chaplin,"0901513810",2011-2015,Detached,Number,Margins of Error,62
    Chaplin,"0901513810",2011-2015,Detached,Percent,Housing Units,79.9
    Chaplin,"0901513810",2011-2015,Detached,Percent,Margins of Error,5.8
    Chaplin,"0901513810",2010-2014,Total,Number,Housing Units,958
    Chaplin,"0901513810",2010-2014,Total,Number,Margins of Error,40
    Chaplin,"0901513810",2010-2014,Detached,Number,Housing Units,804
    Chaplin,"0901513810",2010-2014,Detached,Number,Margins of Error,61
    Chaplin,"0901513810",2010-2014,Detached,Percent,Housing Units,83.9
    Chaplin,"0901513810",2010-2014,Detached,Percent,Margins of Error,5.5
    Eastford,"0901521860",2011-2015,Total,Number,Housing Units,783
    Eastford,"0901521860",2011-2015,Total,Number,Margins of Error,41
    Eastford,"0901521860",2011-2015,Detached,Number,Housing Units,679
    Eastford,"0901521860",2011-2015,Detached,Number,Margins of Error,48
    Eastford,"0901521860",2011-2015,Detached,Percent,Housing Units,86.7
    Eastford,"0901521860",2011-2015,Detached,Percent,Margins of Error,5.1
    Eastford,"0901521860",2010-2014,Total,Number,Housing Units,791
    Eastford,"0901521860",2010-2014,Total,Number,Margins of Error,33
    Eastford,"0901521860",2010-2014,Detached,Number,Housing Units,676
    Eastford,"0901521860",2010-2014,Detached,Number,Margins of Error,43
    Eastford,"0901521860",2010-2014,Detached,Percent,Housing Units,85.5
    Eastford,"0901521860",2010-2014,Detached,Percent,Margins of Error,4.5
    Hampton,"0901536000",2011-2015,Total,Number,Housing Units,755
    Hampton,"0901536000",2011-2015,Total,Number,Margins of Error,40
    Hampton,"0901536000",2011-2015,Detached,Number,Housing Units,696
    Hampton,"0901536000",2011-2015,Detached,Number,Margins of Error,44
    Hampton,"0901536000",2011-2015,Detached,Percent,Housing Units,92.2
    Hampton,"0901536000",2011-2015,Detached,Percent,Margins of Error,3.1
    Hampton,"0901536000",2010-2014,Total,Number,Housing Units,781
    Hampton,"0901536000",2010-2014,Total,Number,Margins of Error,40
    Hampton,"0901536000",2010-2014,Detached,Number,Housing Units,715
    Hampton,"0901536000",2010-2014,Detached,Number,Margins of Error,48
    Hampton,"0901536000",2010-2014,Detached,Percent,Housing Units,91.5
    Hampton,"0901536000",2010-2014,Detached,Percent,Margins of Error,3.8
    Killingly,"0901540500",2011-2015,Total,Number,Housing Units,7811
    Killingly,"0901540500",2011-2015,Total,Number,Margins of Error,358
    Killingly,"0901540500",2011-2015,Detached,Number,Housing Units,5192
    Killingly,"0901540500",2011-2015,Detached,Number,Margins of Error,437
    Killingly,"0901540500",2011-2015,Detached,Percent,Housing Units,66.5
    Killingly,"0901540500",2011-2015,Detached,Percent,Margins of Error,4.7
    Killingly,"0901540500",2010-2014,Total,Number,Housing Units,7817
    Killingly,"0901540500",2010-2014,Total,Number,Margins of Error,371
    Killingly,"0901540500",2010-2014,Detached,Number,Housing Units,5104
    Killingly,"0901540500",2010-2014,Detached,Number,Margins of Error,362
    Killingly,"0901540500",2010-2014,Detached,Percent,Housing Units,65.3
    Killingly,"0901540500",2010-2014,Detached,Percent,Margins of Error,3.7
    Plainfield,"0901559980",2011-2015,Total,Number,Housing Units,6468
    Plainfield,"0901559980",2011-2015,Total,Number,Margins of Error,260
    Plainfield,"0901559980",2011-2015,Detached,Number,Housing Units,4304
    Plainfield,"0901559980",2011-2015,Detached,Number,Margins of Error,318
    Plainfield,"0901559980",2011-2015,Detached,Percent,Housing Units,66.5
    Plainfield,"0901559980",2011-2015,Detached,Percent,Margins of Error,4.4
    Plainfield,"0901559980",2010-2014,Total,Number,Housing Units,6460
    Plainfield,"0901559980",2010-2014,Total,Number,Margins of Error,246
    Plainfield,"0901559980",2010-2014,Detached,Number,Housing Units,4357
    Plainfield,"0901559980",2010-2014,Detached,Number,Margins of Error,297
    Plainfield,"0901559980",2010-2014,Detached,Percent,Housing Units,67.4
    Plainfield,"0901559980",2010-2014,Detached,Percent,Margins of Error,4.1
    Pomfret,"0901561030",2011-2015,Total,Number,Housing Units,1575
    Pomfret,"0901561030",2011-2015,Total,Number,Margins of Error,151
    Pomfret,"0901561030",2011-2015,Detached,Number,Housing Units,1172
    Pomfret,"0901561030",2011-2015,Detached,Number,Margins of Error,111
    Pomfret,"0901561030",2011-2015,Detached,Percent,Housing Units,74.4
    Pomfret,"0901561030",2011-2015,Detached,Percent,Margins of Error,8
    Pomfret,"0901561030",2010-2014,Total,Number,Housing Units,1580
    Pomfret,"0901561030",2010-2014,Total,Number,Margins of Error,118
    Pomfret,"0901561030",2010-2014,Detached,Number,Housing Units,1209
    Pomfret,"0901561030",2010-2014,Detached,Number,Margins of Error,116
    Pomfret,"0901561030",2010-2014,Detached,Percent,Housing Units,76.5
    Pomfret,"0901561030",2010-2014,Detached,Percent,Margins of Error,6.5
    Putnam,"0901562710",2011-2015,Total,Number,Housing Units,4225
    Putnam,"0901562710",2011-2015,Total,Number,Margins of Error,302
    Putnam,"0901562710",2011-2015,Detached,Number,Housing Units,2021
    Putnam,"0901562710",2011-2015,Detached,Number,Margins of Error,254
    Putnam,"0901562710",2011-2015,Detached,Percent,Housing Units,47.8
    Putnam,"0901562710",2011-2015,Detached,Percent,Margins of Error,4.7
    Putnam,"0901562710",2010-2014,Total,Number,Housing Units,4269
    Putnam,"0901562710",2010-2014,Total,Number,Margins of Error,251
    Putnam,"0901562710",2010-2014,Detached,Number,Housing Units,2110
    Putnam,"0901562710",2010-2014,Detached,Number,Margins of Error,234
    Putnam,"0901562710",2010-2014,Detached,Percent,Housing Units,49.4
    Putnam,"0901562710",2010-2014,Detached,Percent,Margins of Error,4.6
    Scotland,"0901567400",2011-2015,Total,Number,Housing Units,646
    Scotland,"0901567400",2011-2015,Total,Number,Margins of Error,31
    Scotland,"0901567400",2011-2015,Detached,Number,Housing Units,565
    Scotland,"0901567400",2011-2015,Detached,Number,Margins of Error,41
    Scotland,"0901567400",2011-2015,Detached,Percent,Housing Units,87.5
    Scotland,"0901567400",2011-2015,Detached,Percent,Margins of Error,4.7
    Scotland,"0901567400",2010-2014,Total,Number,Housing Units,648
    Scotland,"0901567400",2010-2014,Total,Number,Margins of Error,32
    Scotland,"0901567400",2010-2014,Detached,Number,Housing Units,575
    Scotland,"0901567400",2010-2014,Detached,Number,Margins of Error,39
    Scotland,"0901567400",2010-2014,Detached,Percent,Housing Units,88.7
    Scotland,"0901567400",2010-2014,Detached,Percent,Margins of Error,4.5
    Sterling,"0901573420",2011-2015,Total,Number,Housing Units,1274
    Sterling,"0901573420",2011-2015,Total,Number,Margins of Error,100
    Sterling,"0901573420",2011-2015,Detached,Number,Housing Units,1127
    Sterling,"0901573420",2011-2015,Detached,Number,Margins of Error,104
    Sterling,"0901573420",2011-2015,Detached,Percent,Housing Units,88.5
    Sterling,"0901573420",2011-2015,Detached,Percent,Margins of Error,5.5
    Sterling,"0901573420",2010-2014,Total,Number,Housing Units,1289
    Sterling,"0901573420",2010-2014,Total,Number,Margins of Error,128
    Sterling,"0901573420",2010-2014,Detached,Number,Housing Units,1116
    Sterling,"0901573420",2010-2014,Detached,Number,Margins of Error,125
    Sterling,"0901573420",2010-2014,Detached,Percent,Housing Units,86.6
    Sterling,"0901573420",2010-2014,Detached,Percent,Margins of Error,6.1
    Thompson,"0901575870",2011-2015,Total,Number,Housing Units,4132
    Thompson,"0901575870",2011-2015,Total,Number,Margins of Error,168
    Thompson,"0901575870",2011-2015,Detached,Number,Housing Units,3266
    Thompson,"0901575870",2011-2015,Detached,Number,Margins of Error,209
    Thompson,"0901575870",2011-2015,Detached,Percent,Housing Units,79
    Thompson,"0901575870",2011-2015,Detached,Percent,Margins of Error,3.9
    Thompson,"0901575870",2010-2014,Total,Number,Housing Units,4040
    Thompson,"0901575870",2010-2014,Total,Number,Margins of Error,162
    Thompson,"0901575870",2010-2014,Detached,Number,Housing Units,3184
    Thompson,"0901575870",2010-2014,Detached,Number,Margins of Error,218
    Thompson,"0901575870",2010-2014,Detached,Percent,Housing Units,78.8
    Thompson,"0901575870",2010-2014,Detached,Percent,Margins of Error,4
    Windham,"0901586790",2011-2015,Total,Number,Housing Units,9676
    Windham,"0901586790",2011-2015,Total,Number,Margins of Error,379
    Windham,"0901586790",2011-2015,Detached,Number,Housing Units,4127
    Windham,"0901586790",2011-2015,Detached,Number,Margins of Error,299
    Windham,"0901586790",2011-2015,Detached,Percent,Housing Units,42.7
    Windham,"0901586790",2011-2015,Detached,Percent,Margins of Error,2.6
    Windham,"0901586790",2010-2014,Total,Number,Housing Units,9702
    Windham,"0901586790",2010-2014,Total,Number,Margins of Error,438
    Windham,"0901586790",2010-2014,Detached,Number,Housing Units,4045
    Windham,"0901586790",2010-2014,Detached,Number,Margins of Error,360
    Windham,"0901586790",2010-2014,Detached,Percent,Housing Units,41.7
    Windham,"0901586790",2010-2014,Detached,Percent,Margins of Error,3
    Woodstock,"0901588190",2011-2015,Total,Number,Housing Units,3809
    Woodstock,"0901588190",2011-2015,Total,Number,Margins of Error,193
    Woodstock,"0901588190",2011-2015,Detached,Number,Housing Units,3317
    Woodstock,"0901588190",2011-2015,Detached,Number,Margins of Error,246
    Woodstock,"0901588190",2011-2015,Detached,Percent,Housing Units,87.1
    Woodstock,"0901588190",2011-2015,Detached,Percent,Margins of Error,4.8
    Woodstock,"0901588190",2010-2014,Total,Number,Housing Units,3725
    Woodstock,"0901588190",2010-2014,Total,Number,Margins of Error,203
    Woodstock,"0901588190",2010-2014,Detached,Number,Housing Units,3045
    Woodstock,"0901588190",2010-2014,Detached,Number,Margins of Error,208
    Woodstock,"0901588190",2010-2014,Detached,Percent,Housing Units,81.7
    Woodstock,"0901588190",2010-2014,Detached,Percent,Margins of Error,4.5
    """)
