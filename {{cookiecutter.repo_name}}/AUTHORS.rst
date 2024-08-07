
Authors
=======
{% for n in range(cookiecutter.author_count|int) %}
{% set contact = cookiecutter.emails.split(',')[n]|trim or cookiecutter.websites.split(',')[n]|trim -%}
* {{ cookiecutter.full_names.split(',')[n]|trim }}{% if contact %} - {{ contact }}{% endif %}
{%- endfor %}
