#!/bin/bash

pip -V

pip install --target=local_lib --upgrade git+https://github.com/jaraco/path.git > install.log

INSTALL_PATH_PIP="$(pip freeze --path ./local_lib)"

if [[ "$INSTALL_PATH_PIP" == *"path"* ]]; then
    python3 ./my_program.py
fi