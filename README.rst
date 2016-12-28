pytest-ctdata_datatest
===================================

.. image:: https://travis-ci.org/CT-Data-Collaborative/pytest-ctdata-datatest.svg?branch=master
    :target: https://travis-ci.org/CT-Data-Collaborative/pytest-ctdata-datatest
    :alt: See Build Status on Travis CI

Plugin for testing `Tidy data` with accompanying YAML-based metadata file

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Features
--------

- Leverage YAML file to setup a series of fixtures for easy testing of `Tidy data`_


Requirements
------------

* Tidy-formatted data stored as a .csv
* YAML-based metadata file


Installation
------------

You can install "pytest-ctdata_datatest" via `pip`_ from `PyPI`_::

    $ pip install pytest-ctdata_datatest


Usage
-----

This plugin loads and structures a CTData CKAN dataset for value testing and structure testing.

In either your test file or your conftest file, set `METADATA_FILE` to be the path to the dataset YAML file. The plugin
will load, parse and set up a number of fixtures that can be used to run basic and more complex tests.

Provided fixtures include:

* metadata::dict representing the parsed YAML file

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