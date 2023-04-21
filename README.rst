=================
yapy-cookiecutter
=================

Yet Another Python Cookiecutter_ template for a Python modules and applications focussing on data science, processing and analysis natural sciences stuff.

*Notes*:

It is based on and derived from the excellent `cookiecutter-pylibrary <https://github.com/ionelmc/cookiecutter-pylibrary/>`_ cookiecutter by Ionel Cristian Mărieș.

.. contents:: Table of Contents

Features
--------

Related to the original `cookiecutter-pylibrary <https://github.com/ionelmc/cookiecutter-pylibrary/>`_ some flexibility was removed and some choices are implemented:

* Python packaging without the now obsolete Setuptools_:

  * based on `pyproject.toml`
  * no `setup.py` or `setup.cfg`

* Employs automatic semantic versioning based on commit messages, please see version-management_
* Generates GitHub workflow files for CI/CD, which

  #. run tests matrix of multiple Python versions and OS platforms
  #. set release version number
  #. generate documentation
  #. build packages (binary and source)
  #. upload the packages to PyPI (test.pypi by default) and create a GitHub release page for regular releases

* Tox_ for managing test environments for Python 3.7+
* Pytest_ for testing Python 3.7+
* Code coverage report of all tests compiled by ``pytest-cov`` for coverage tracking, added to the online documentation
* Documentation with Sphinx_ to be hosted on GitHub Pages
* Choice of various licenses.
* Configurations for (also via pre-commit_):

  * isort_
  * black_
  * flake8_

* EditorConfig_ - for being picked up by VS-Code_, it seems `a plugin <https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig>`_ is needed
* Packaging and code quality checks. This template comes with a tox environment (``check``) that will:

  * Check if your ``README.rst`` is valid.
  * Check if the ``MANIFEST.in`` has any issues.
  * Run ``flake8`` (a combo of PEP8, pyflakes and McCabe checks)

Requirements
------------

Projects using this template have these minimal dependencies:

* Cookiecutter_ - just for creating the project
* Tox_ - for running the tests

To get quickly started on a new system, just `install pip
<https://pip.pypa.io/en/latest/installing.html>`_. And install Tox_ and Cookiecutter_ by running this in your shell or command prompt::

  pip install tox cookiecutter

Usage and options
-----------------

Please see also the common `cookiecutter use guide <https://cookiecutter.readthedocs.io/en/stable/usage.html>`_.
First generate your project::

  cookiecutter gh:BAMresearch/yapy-cookiecutter

You will be asked for these fields:

.. note:: Fields that work together usually use the same prefix. If you answer "no" on the first one then the rest
   won't have any effect so just ignore them. Maybe in the future cookiecutter will allow option hiding or something
   like a wizard.

.. list-table::
    :header-rows: 1

    * - Field
      - Default
      - Description

    * - ``full_name``
      - .. code:: python

            "Ingo Breßler"
      - Main author of this library or application (used in ``AUTHORS.rst`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``email``
      - .. code:: python

            "dev@ingobressler.net"
      - Contact email of the author (used in ``AUTHORS.rst`` and ``pyproject.toml``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``website``
      - .. code:: python

            "https://github.com/ibressler"
      - Website of the author (used in ``AUTHORS.rst``).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``repo_userorg``
      - .. code:: python

            "ibressler"
      - GitHub user name or organization name of this project (used for GitHub link, as in `<https://github.com/ibressler>`_).

        Can be set in your ``~/.cookiecutterrc`` config file.

    * - ``project_name``
      - .. code:: python

            "My Test Project"
      - Verbose project name, used in headings (docs, readme, etc).

    * - ``repo_hosting_domain``
      - .. code:: python

            "github.com"
      - Use ``"no"`` for no hosting (various links will disappear). You can also use ``"gitlab.com"``.

    * - ``repo_name``
      - .. code:: python

            "my-test-project"
      - Repository name on GitHub (and project's root directory name). Derived from the ``project_name``.

    * - ``package_name``
      - .. code:: python

            "my_test_project"
      - Python package name (whatever you would import), with underscores for spaces. Derived from the ``project_name``.

    * - ``distribution_name``
      - .. code:: python

            "my-test-project"
      - PyPI distribution name (what you would ``pip install``), with dashes for spaces. Derived from the ``project_name``.

    * - ``project_short_description``
      - .. code:: python

            "An example package [...]"
      - One line description of the project (used in ``README.rst`` and ``pyproject.toml``).

    * - ``release_date``
      - .. code:: python

            "today"
      - Release date of the project (ISO 8601 format) default to today (used in ``CHANGELOG.md``).

    * - ``year``
      - .. code:: python

            "now"
      - Copyright year (used in Sphinx ``conf.py``).

    * - ``version``
      - .. code:: python

            "0.1.0"
      - Release version (see ``pyproject.toml``, ``src/my_test_project/__init__.py`` and in Sphinx ``docs/conf.py``).

    * - ``license``
      - .. code:: python

            "BSD license"
      - License to use. Available options:

        * BSD license
        * MIT license
        * Apache License 2.0
        * and more …

        What license to pick? https://choosealicense.com/

    * - ``sphinx_theme``
      - .. code:: python

            "sphinx-rtd-theme"
      - What Sphinx_ theme to use.

        Suggested alternative: `sphinx-py3doc-enhanced-theme <https://pypi.org/project/sphinx_py3doc_enhanced_theme>`__
        for a responsive theme based on the Python 3 documentation.

    * - ``pypi_host``
      - .. code:: python

            "test.pypi.org"
      - Choose between the PyPI Test repo (which is the default) and the *real* PyPI repository. Please remember, files uploaded to PyPI once can not be replaced with files of the same name: files can be deleted (removed from being visible) but not replaced. Therefore, package deployment should be tested on `PyPI Testing <https://test.pypi.org>`_ first.

The testing (``tox.ini``) configuration is generated from templates. For your convenience there's an
initial bootstrap ``tox.ini``, to get the initial generation going just run::

  tox

You can later regenerate files in ``.github/workflows`` by running::

  tox -e bootstrap

After this you can create the initial repository (make sure you `create <https://github.com/new>`_ an *empty* Github
project)::

  git init .
  git add .
  git commit -m "Initial skel."
  git remote add origin git@github.com:ibressler/my-test-project.git
  git push -u origin master

Developing the project
``````````````````````

To run all the tests, just run::

  tox

To see all the tox environments::

  tox -l

To only build the docs::

  tox -e docs

To build and verify that the built package is proper and other code QA checks::

  tox -e check

Releasing the project
`````````````````````
Before releasing your package on PyPI you should have all the tox environments passing.

.. _version-management:

Version management
''''''''''''''''''

This template provides a semantic-release_ configuration. It raises the version number by parsing the GIT commit history:

* Commits starting with ``fix(…): …`` will increase the patch version number (``1.0.0`` to ``1.0.1``) and
* Commit messages starting with ``feat(…): …`` will increase the minor version number (``1.0.0`` to ``1.1.0``).
* Commits with ``BREAKING CHANGE:`` in the message footer will increase the major version number ``1.0.0`` to ``2.0.0``.
* All other changes will generate a new pre-release version number (``1.0.1`` to ``1.0.2-dev.1``).

This behavior is implemented by the GitHub action workflow files and templates in ``ci/templates``.

For the basic convention of semantic version numbering, please see `Semantic Versioning 2.0.0 <http://semver.org/>`_ and the commit message format expected here is documented in the `AngularJS project <https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#-git-commit-guidelines>`_:

Commit Message Format
.....................

Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special
format that includes a **type**, a **scope** and a **subject**::

  <type>(<scope>): <subject>
  <BLANK LINE>
  <body>
  <BLANK LINE>
  <footer>

The **header** is mandatory and the **scope** of the header is optional.

Any line of the commit message cannot be longer than 100 characters! This allows the message to be easier
to read on GitHub as well as in various git tools.

Type
~~~~

Must be one of the following:

* **feat**: A new feature
* **fix**: A bug fix
* **docs**: Documentation only changes
* **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing
  semi-colons, etc)
* **refactor**: A code change that neither fixes a bug nor adds a feature
* **perf**: A code change that improves performance
* **test**: Adding missing or correcting existing tests
* **chore**: Changes to the build process or auxiliary tools and libraries such as documentation
  generation

Scope
~~~~~

The scope could be anything specifying place of the commit change. For example ``$location``,
``UI``, ``calculus``, ``$rootScope``, etc...

You can use `*` when the change affects more than a single scope.

Subject
~~~~~~~

The subject contains succinct description of the change:

* use the imperative, present tense: "change" not "changed" nor "changes"
* don't capitalize first letter
* no dot (.) at the end

Body
~~~~

Just as in the **subject**, use the imperative, present tense: "change" not "changed" nor "changes".
The body should include the motivation for the change and contrast this with previous behavior.

Footer
~~~~~~

The footer should contain any information about **Breaking Changes** and is also the place to
`reference GitHub issues that this commit closes <https://help.github.com/articles/closing-issues-via-commit-messages/>`_.

**Breaking Changes** should start with the word ``BREAKING CHANGE:`` with a space or two newlines.
The rest of the commit message is then used for this.

Building and uploading
''''''''''''''''''''''

Before building dists make sure you got a clean build area::

    rm -rf build
    rm -rf src/*.egg-info

Note:

    Dirty ``build`` or ``egg-info`` dirs can cause problems: missing or stale files in the resulting dist or
    strange and confusing errors. Avoid having them around.

Then you should check that you got no packaging issues::

    tox -e check

And then you can build the ``sdist``, and if possible, the ``bdist_wheel`` too::

    tox -e build

To make a release of the project on PyPI, assuming you got some distributions in ``dist/``, the most simple usage is::

    twine upload --skip-existing dist/*.whl dist/*.gz dist/*.zip

Note:

    `twine <https://pypi.org/project/twine>`_ is a tool that you can use to securely upload your releases to PyPI.
    You can still use the old ``python setup.py register sdist bdist_wheel upload`` but it's not very secure - your PyPI
    password will be sent over plaintext.

Changelog
---------

Please see the GIT commit history ;)

Questions & answers
-------------------

Why does ``tox.ini`` have a ``passenv = *``?

  Tox 2.0 changes the way it runs subprocesses - it no longer passes all the environment variables by default. This causes
  all sorts of problems if you want to run/use any of these with Tox: SSH Agents, Browsers (for Selenium), Appengine SDK,
  VC Compiler and so on.

  By default this is not needed. You can always add ``passenv = *`` if you like the convenience.

Why is the version stored in several files (``pkg/__init__.py``, ``docs/conf.py``)?

  We cannot use a metadata/version file [#]_ because this template is to be used with both distributions of packages (dirs
  with ``__init__.py``) and modules (simple ``.py`` files that go straight in ``site-packages``). There's no good place
  for that extra file if you're distributing modules.

  But this isn't so bad - semantic-release_ manages the version string quite
  neatly.

.. [#] Example, an ``__about__.py`` file.

Not Exactly What You Want?
--------------------------

No way, this is the best. :stuck_out_tongue_winking_eye:


If you have criticism or suggestions please open up an Issue or Pull Request.

.. _Tox: https://tox.wiki/en/latest/
.. _Sphinx: http://sphinx-doc.org/
.. _Coveralls: https://coveralls.io/
.. _ReadTheDocs: https://readthedocs.org/
.. _Setuptools: https://pypi.org/project/setuptools
.. _Pytest: http://pytest.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Nose: http://nose.readthedocs.org/
.. _isort: https://pypi.org/project/isort
.. _black: https://pypi.org/project/black/
.. _flake8: https://pypi.org/project/flake8
.. _semantic-release: https://python-semantic-release.readthedocs.io
.. _Codecov: http://codecov.io/
.. _Codacy: https://codacy.com/
.. _CodeClimate: https://codeclimate.com/
.. _pre-commit: https://pre-commit.com/
.. _EditorConfig: https://editorconfig.org/
.. _VS-Code: https://code.visualstudio.com/