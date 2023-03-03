#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import tempfile
import shutil
import sys

print('NOTE', __file__)


if __name__ == '__main__':

    cwd = Path().resolve()
    src = cwd / 'src'
    ci = cwd / 'ci'

    # backup files, see post_gen_project.py hook
    exclude_files = {{cookiecutter.extra_context.exclude_existing}}
    bckp = Path(
        tempfile.mkdtemp(prefix='cookiecutter.', suffix='.backup', dir=cwd)
    )
    for fn in exclude_files:
        if not (cwd / fn).is_file():
            continue
        print('backup:', fn)
        print('to:    ', bckp / fn)
        target_path = Path(bckp / fn).parent
        target_path.mkdir(parents=True, exist_ok=True)
        shutil.copy(cwd / fn, target_path)
