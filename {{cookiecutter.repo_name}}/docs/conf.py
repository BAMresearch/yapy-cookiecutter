# -*- coding: utf-8 -*-
{% if cookiecutter.sphinx_theme == 'sphinx-rtd-theme' -%}
import os
{% endif -%}
{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' -%}
import {{ cookiecutter.sphinx_theme|replace('-', '_') }}
{% endif %}

import toml

base_path = dirname(dirname(abspath(__file__)))
project_meta = toml.load(join(base_path, 'pyproject.toml'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx_mdinclude',
]
source_suffix = '.rst'
master_doc = 'index'
project = {{ '{0!r}'.format(cookiecutter.project_name) }}
year = '{% if cookiecutter.year_from == cookiecutter.year_to %}{{ cookiecutter.year_from }}{% else %}{{ cookiecutter.year_from }}-{{ cookiecutter.year_to }}{% endif %}'
author = {{ '{0!r}'.format(cookiecutter.full_name) }}
copyright = '{0}, {1}'.format(year, author)
version = '{{ "{0!r}".format(cookiecutter.version) }}'
release = version
commit_id = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).strip().decode('ascii')

autodoc_mock_imports = ["ipykernel", "notebook", "pandas", "ipywidgets", "matplotlib", "scipy"]

pygments_style = 'trac'
templates_path = ['.']
extlinks = {
    'issue': (join(project_meta['project']['urls']['repository'], 'issues', '%s'), '#%s'),
    'pr': (join(project_meta['project']['urls']['repository'], 'pull', '%s'), 'PR #%s'),
}

{%- if cookiecutter.sphinx_theme != 'sphinx-rtd-theme' %}
html_theme = '{{ cookiecutter.sphinx_theme|replace("-", "_") }}'
html_theme_path = [{{ cookiecutter.sphinx_theme|replace('-', '_') }}.get_html_theme_path()]
html_theme_options = {
    'githuburl': 'https://{{ cookiecutter.repo_hosting_domain }}/{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}/',
}
{%- else %}
# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only set the theme if we're building docs locally
    html_theme = '{{ cookiecutter.sphinx_theme|replace("-", "_") }}'
{%- endif %}

html_use_smartypants = True
html_last_updated_fmt = '%b %d, %Y'
html_split_index = False
html_sidebars = {
    '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
}
html_short_title = '%s-%s' % (project, version)

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

linkcheck_ignore = [
    join(
        project_meta['project']['urls']['documentation'],
        project_meta['tool']['coverage']['report']['path'],
    )
    + r'.*',
]
