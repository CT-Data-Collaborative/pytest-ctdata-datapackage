pytest-ctdata-datapackage
=========================

.. image:: https://travis-ci.org/CT-Data-Collaborative/pytest-ctdata-datapackage.svg?branch=master
    :target: https://travis-ci.org/CT-Data-Collaborative/pytest-ctdata-datapackage
    :alt: See Build Status on Travis CI

Plugin for testing `Tabular Data Packages`_ with `Tidy data`_ resources.

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

- Leverage `datapackage.json`_ and `JSON Table Schema`_ to setup a series of fixtures for easy testing of`Tidy data`_


Requirements
------------

* Tidy-formatted data stored as a .csv
* Datapackage.json


Installation
------------

You can install "pytest-ctdata-datapackage" via `pip`_ from `Github`_::

:bash:`$ pip install -e git+https://github.com/CT-Data-Collaborative/pytest-ctdata-datapackage#egg=pytest-ctdata
-datapackage`


Usage
-----

This plugin loads and structures a CTData CKAN dataset for value and structure testing. It is designed to be used
alongside `CTData Dataset Cookiecutter`_.

The plugin makes a few assumptions about the structure and organization of your data. It assumes that the root of
your directory will contain a :code:`datapackage.json` and the presence of only one resource file. This is more
strict that the requirements imposed by the Tabular Data Package standards and stems from how we publish and display
data.

Using the :code:`datapackage.json`, the plugin will set up a number of fixtures that can then be used to run some
basic tests against the final data set. Our cookiecutter plugin contains a testing file that includes a number of
standard tests.

Most data published by CTData is associated with a limited set of geographies. Specifically:

* Town/City
* School District
* County

When we publish data, we follow a number of conventions that impact data set testing.

1. All geographic entities are represented in the raw data file, even if no data is available. We consider the
absence of data to be a meaningful data point itself and so we back fill our data files to communicate this. We
usually indicate the absence of data by setting the :code:`Value` field to be :code:`-9999`.

2. All combinations of variables should be present. This follows, from #1, in that if we choose to present a given
disaggregation that is not uniformally available, we will communicate this by setting the :code:`Value` field to be
:code:`-9999`.


Provided fixtures include:

* metadata - a dict representing the parsed datapackage.json file
* dataset - a list of dicts representing the parsed tidy data file
* spotchecks - a list of lookup keys and expected value
* geographies - a list of geographical entities present in data
* domain - a boolean representing check that dataset domain is valid
* years - a list of the years as specified in the metadata


Metadata Schema
---------------

Testing row counts and the success / failure of backfilling and subgroup calculations requires knowing the relationship
between factors and the degree to which factors are nested or in parallel.

For example, let's imagine that there is a data set where observations include information about Sex and Race/Ethnicity.
There are two common scenarios. These variables could either represent a hierarchy of disaggregation or represent
parallel disaggregations.

Let's say that the Sex factor includes the following levels

- Male
- Female
- All

And the Race/Ethnicity factor includes the following levels

- White
- Black
- Hispanic
- All

If these are nested each observation where sex is indicated to be 'Male' will have a corresponding Race/Ethnicity level
that can be one of the three choices. This results in twelve possible combinations

- Male/White
- Female/White
- All/White
- Male/Black
and so on until
- All/All

As an alternative, these factors could be parallel, in which case a given observation can either include information
about sex OR information about Race/Ethnicity. The combinations can

- Male/All
- Female/All
- All/All
- All/White
- All/Black
- All/Hispanic

Sometimes the situation is more complex. Some factors can be hierarchical, while others can be parallel. This is often
the case with education data. For example, data may be disaggregated by Sex and Race/Ethnicity with a separate
disaggregation by grade.

We can generalize this specification as follows in the YAML file.

First, we include a specification of each factor and the available levels.

Second, we can include a list of the valid combinations.

For example one (Sex and Race/Ethnicity nested), we would specify as follows:

- [Sex, Race/Ethnicity]

For the second example (Sex and Race/Ethnicity in parallel), we would specify as follows:

- Sex
- Race/Ethnicity

For the third, (Sex and Race/Ethnicity nested, Grade in parallel):

- [Sex, Race/Ethnicity]
- Grade

Roadmap
-------

Fixtures to add:

* subdomain - a boolean representing check that dataset subdomain is a valid value
* domain_subdomain - a boolean representing check that domain/subdomain combination is a valid value
* units - a list of expected measurement types
* default - a dict of the expected default settings for CKAN
* variables - a list of expected variables in dataset - will need to specify disaggregation relationship

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-ctdata_datatest" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`Apache Software License 2.0`: http://www.apache.org/licenses/LICENSE-2.0
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/scuerda/pytest-ctdata_datatest/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.io/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`Tidy data`: http://vita.had.co.nz/papers/tidy-data.pdf
.. _`CTData Dataset Cookiecutter`: https://github.com/CT-Data-Collaborative/ctdata-dataset-cookiecutter
.. _`Tabular Data Packages`: http://frictionlessdata.io/guides/tabular-data-package/
.. _`datapackage.json`: http://frictionlessdata.io/guides/data-package/#datapackagejson
.. _`Github`: https://github.com
.. _`JSON Table Schema`: http://frictionlessdata.io/guides/json-table-schema/

.. role:: bash(code)
   :language: bash