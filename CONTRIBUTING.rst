============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

Bug reports
===========

When `reporting a bug <https://github.com/BAMresearch/yapy-cookiecutter/issues>`_ please include:

    * Your operating system name and version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Documentation improvements
==========================

yapy-cookiecutter could always use more documentation, whether as part of the
official yapy-cookiecutter docs, in docstrings, or even on the web in blog posts,
articles, and such.

Feature requests and feedback
=============================

The best way to send feedback is to file an issue at https://github.com/BAMresearch/yapy-cookiecutter/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions are welcome :)

Development
===========

To set up `yapy-cookiecutter` for local development:

1. `Fork yapy-cookiecutter on GitHub <https://github.com/BAMresearch/yapy-cookiecutter/fork>`_.
2. Clone your fork locally::

    git clone git@github.com:your_name_here/yapy-cookiecutter.git

3. Create a branch for local development::

    git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

4. When you're done making changes run all the checks and docs builder with `tox <https://tox.wiki/en/latest/installation.html>`_ one command::

    tox

5. Commit your changes and push your branch to GitHub::

    git add .
    git commit -m "Your detailed description of your changes."
    git push origin name-of-your-bugfix-or-feature

6. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

If you need some code review or feedback while you're developing the code just make the pull request.

Tips
----

If you want to add a context option, you need to:

* Add the actual option in `cookiecutter.json <https://github.com/BAMresearch/yapy-cookiecutter/blob/main/cookiecutter.json>`_
* Add it in the cookiecutter test builder suite:

  * Edit `setup.cfg <https://github.com/BAMresearch/yapy-cookiecutter/blob/main/ci/setup.cfg>`_
  * Run ``./ci/update.py`` to regenerate the test ``.cookiecutterrc`` files.
* Change the `bare tox.ini <https://github.com/BAMresearch/yapy-cookiecutter/blob/main/%7B%7Bcookiecutter.repo_name%7D%7D/tox.ini>`_ to have an conditional for it.
* Change the `template tox.ini <https://github.com/BAMresearch/yapy-cookiecutter/blob/main/%7B%7Bcookiecutter.repo_name%7D%7D/ci/templates/tox.ini>`_
  (don't forget the raw sections) to have a conditional for it
