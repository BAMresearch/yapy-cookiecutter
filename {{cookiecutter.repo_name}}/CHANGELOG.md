
Changelog
=========

% <!--next-version-placeholder-->

{% set datestring -%}
{% if cookiecutter.release_date == 'today' -%}
{% now 'utc', '%Y-%m-%d' %}
{%- else %}{{ cookiecutter.release_date }}{% endif %}
{%- endset %}
## {{ cookiecutter.version }} ({{ datestring }})

* First release
