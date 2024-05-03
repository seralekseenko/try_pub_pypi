# try_pub_pypi

Only test to automate publishing to pypi.org

### virtual python3 ENV

1. Create virtual ENV → `python3 -m venv .venv` # смотри conda (Anaconda)
2. Activate → `source .venv/bin/activate`
3. Check virt env → `echo $VIRTUAL_ENV` → should be non empty output
4. Deactivate → `deactivate` or reopen terminal session

### Requirements

- instal `pip install -r requirements.txt`
- save `pip freeze > requirements.txt`
- check to old requirements `pip list --outdated`
- upgrade some package `pip install -U package_name`

### Run tests

A simple way: `python3 -m unittest discover -s ./tests` or `pytest`
