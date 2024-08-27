# Thoth-Server

Thoth core.

## Installation

Python 3.10 and above is needed to run this porject.

```bash
# creating the virtual environment

python -m venv env

# linux 

source env/bin/activate

# windows

env/Scripts/activate

## install git hooks: this step is required

flask --app manage.py install-hooks

# run tests: 

flask --app manage.py test
```
