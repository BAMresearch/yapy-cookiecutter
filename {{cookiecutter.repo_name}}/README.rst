========
Overview
========

{{ cookiecutter.project_short_description|wordwrap(119) }}

.. start-badges

| |version| |commits-since| |license|
| |supported-versions| |wheel| |downloads|
| |cicd| |coverage|

.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}
    :alt: PyPI Package latest release

.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...{{ cookiecutter.repo_main_branch }}
    :alt: Commits since latest release

.. |license| image:: https://img.shields.io/pypi/l/{{ cookiecutter.distribution_name }}.svg
    :target: https://en.wikipedia.org/wiki/{{ cookiecutter.license|truncate(34,end='')|replace(" ","_") }}
    :alt: License

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}
    :alt: Supported versions

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}#files
    :alt: PyPI Wheel

.. |downloads| image:: https://img.shields.io/pypi/dw/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}/
    :alt: Weekly PyPI downloads

.. |cicd| image:: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}/actions/workflows/ci-cd.yml/badge.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}/actions/workflows/ci-cd.yml
    :alt: Continuous Integration and Deployment Status

.. |coverage| image:: https://img.shields.io/endpoint?url={{ cookiecutter.docs_url }}/coverage-report/cov.json
    :target: {{ cookiecutter.docs_url }}/coverage-report/
    :alt: Coverage report

.. end-badges


Installation
============

::

    pip install {{ cookiecutter.distribution_name }}

You can also install the in-development version with::
{% if cookiecutter.repo_hosting_domain == "github.com" %}
    pip install https://github.com/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/archive/{{ cookiecutter.repo_main_branch }}.zip
{% elif cookiecutter.repo_hosting_domain == "gitlab.com" %}
    pip install https://gitlab.com/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/-/archive/{{ cookiecutter.repo_main_branch }}/{{ cookiecutter.repo_name }}-{{ cookiecutter.repo_main_branch }}.zip
{% else %}
    pip install git+ssh://git@{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}.git@{{ cookiecutter.repo_main_branch }}
{%- endif %}

Documentation
=============

{{ cookiecutter.docs_url }}

Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
