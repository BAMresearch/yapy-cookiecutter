========
Overview
========

{{ cookiecutter.project_short_description|wordwrap(119) }}

.. start-badges

| |version| |commits-since| |license|
| |build| |supported-versions| |wheel| |downloads|
| |tests| |coverage|
| |docs|

.. |docs| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/actions/workflows/docs.yml/badge.svg
    :target: {{ cookiecutter.docs_url }}
    :alt: Documentation Status

.. |build| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/actions/workflows/build.yml/badge.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}
    :alt: GitHub Actions Build Status

.. |tests| image:: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/actions/workflows/tests.yml/badge.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/actions
    :alt: GitHub Actions Tests Status

.. |coverage| image:: https://img.shields.io/endpoint?url={{ cookiecutter.docs_url }}/coverage-report/cov.json
    :target: {{ cookiecutter.docs_url }}/coverage-report/
    :alt: Coverage report

.. |version| image:: https://img.shields.io/pypi/v/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}
    :alt: PyPI Package latest release

.. |license| image:: https://img.shields.io/pypi/l/{{ cookiecutter.distribution_name }}.svg
    :target: https://en.wikipedia.org/wiki/{{ cookiecutter.license|truncate(34,end='') }}
    :alt: License

.. |wheel| image:: https://img.shields.io/pypi/wheel/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}#files
    :alt: PyPI Wheel

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}
    :alt: Supported versions

.. |commits-since| image:: https://img.shields.io/github/commits-since/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/v{{ cookiecutter.version }}.svg
    :target: https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/compare/v{{ cookiecutter.version }}...{{ cookiecutter.repo_main_branch }}
    :alt: Commits since latest release

.. |downloads| image:: https://img.shields.io/pypi/dw/{{ cookiecutter.distribution_name }}.svg
    :target: https://{{ cookiecutter.pypi_host }}/project/{{ cookiecutter.distribution_name }}/
    :alt: Weekly PyPI downloads

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
