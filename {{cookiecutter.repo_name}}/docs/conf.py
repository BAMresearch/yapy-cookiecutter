# -*- coding: utf-8 -*-
{% if cookiecutter.sphinx_theme == "sphinx-rtd-theme" -%}
import os

{% endif -%}
{%- if cookiecutter.sphinx_theme != "sphinx-rtd-theme" -%}
{%- if cookiecutter.sphinx_theme != "furo" -%}
import {{ cookiecutter.sphinx_theme|replace('-', '_') }}
{%- endif -%}
{%- endif %}

import subprocess
from os.path import abspath, dirname, join

import toml

base_path = dirname(dirname(abspath(__file__)))
project_meta = toml.load(join(base_path, "pyproject.toml"))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
]
autosummary_generate = True  # Turn on sphinx.ext.autosummary
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
project = {{"{0!r}".format(cookiecutter.project_name)|replace("'",'"')}}
year = "{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}"
author = "{% for name in cookiecutter.full_names.split(',')|map('trim') -%}{% if loop.index > 1 %}{% if loop.index < loop.length %}, {% else %} and {% endif %}{% endif %}{{ name }}{%- endfor %}"
copyright = "{0}, {1}".format(year, author)
version = {{"{0!r}".format(cookiecutter.version)|replace("'",'"')}}
release = version
commit_id = None
try:
    commit_id = (
        subprocess.check_output(["git", "rev-parse", "--short", "HEAD"]).strip().decode("ascii")
    )
except subprocess.CalledProcessError as e:
    print(e)


autodoc_mock_imports = [
    "ipykernel",
    "notebook",
    "pandas",
    "ipywidgets",
    "matplotlib",
    "scipy",
    "h5py",
    "pint",
    "sasmodels",
]

pygments_style = "trac"
extlinks = {
    "issue": (join(project_meta["project"]["urls"]["repository"], "issues", "%s"), "#%s"),
    "pr": (join(project_meta["project"]["urls"]["repository"], "pull", "%s"), "PR #%s"),
}

{%- if cookiecutter.sphinx_theme != "sphinx-rtd-theme" %}
html_theme = "{{ cookiecutter.sphinx_theme|replace("-", "_") }}"
{%- if cookiecutter.sphinx_theme != "furo" %}
html_theme_path = [{{cookiecutter.sphinx_theme | replace("-", "_")}}.get_html_theme_path()]
html_theme_options = {
    "githuburl": "https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/",
}
{%- endif %}
{%- else %}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = "{{ cookiecutter.sphinx_theme|replace("-", "_") }}"
{%- endif %}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
if commit_id:
    html_last_updated_fmt += f" (git {commit_id})"
html_split_index = False
{%  if cookiecutter.sphinx_theme != "furo" -%}
html_sidebars = {
    "**": [
        "searchbox.html",
        "globaltoc.html",
        "sourcelink.html",
    ],
}
{%- endif %}
html_short_title = "%s-%s" % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

linkcheck_ignore = [
    join(
        project_meta["project"]["urls"]["documentation"],
        project_meta["tool"]["coverage"]["report"]["path"],
    )
    + r".*",
    # attempted fix of '406 Client Error: Not Acceptable for url'
    # https://github.com/sphinx-doc/sphinx/issues/1331
    join(project_meta["project"]["urls"]["repository"], "commit", r"[0-9a-fA-F]+")
]
