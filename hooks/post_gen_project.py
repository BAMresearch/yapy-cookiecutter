import pathlib
import shutil
import subprocess
import sys

print("NOTE", __file__)
try:
    from click.termui import secho
except ImportError:
    warn = note = print
else:
    def warn(text):
        for line in text.splitlines():
            secho(line, fg="white", bg="red", bold=True)

    def note(text):
        for line in text.splitlines():
            secho(line, fg="yellow", bold=True)


if __name__ == "__main__":

    cwd = pathlib.Path().resolve()
    src = cwd / 'src'
    ci = cwd / 'ci'

{%- if cookiecutter.repo_hosting == 'no' %}
    cwd.joinpath('CONTRIBUTING.rst').unlink()
{% endif %}

{%- if cookiecutter.license == "no" %}
    cwd.joinpath('LICENSE').unlink()
{% endif %}

    print("""
################################################################################

    Generating CI configuration ...
""")
    try:
        subprocess.check_call(['tox', '-e', 'bootstrap', '--sitepackages'])
    except Exception as e:
        print("There was an error!", e)
        pass
        # try:
        #     subprocess.check_call([sys.executable, '-mtox', '-e', 'bootstrap', '--sitepackages'])
        # except Exception:
        #     subprocess.check_call([sys.executable, ci / 'update.py'])
    else:
        print("""
################################################################################
################################################################################

    You have succesfully created `{{ cookiecutter.repo_name }}`.

################################################################################

    You've used these cookiecutter parameters:
{% for key, value in cookiecutter.items()|sort %}
        {{ "{0:26}".format(key + ":") }} {{ "{0!r}".format(value).strip("u") }}
{%- endfor %}

    See .cookiecutterrc for instructions on regenerating the project.

################################################################################

    To get started run these:

        cd {{ cookiecutter.repo_name }}
        git init
        git add --all
        git commit -m "Add initial project skeleton."
        git tag v{{ cookiecutter.version }}
        git remote add origin git@{{ cookiecutter.repo_hosting_domain }}:{{ cookiecutter.repo_userorg }}/{{ cookiecutter.repo_name }}.git
        git push -u origin {{ cookiecutter.repo_main_branch }} v{{ cookiecutter.version }}

    To regenerate your tox.ini and .github/workflow files, run:

        tox -e bootstrap

    You can also run:

        python /ci/update.py --no-env

""")
