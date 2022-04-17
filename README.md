## pipfile-upgrade

A package to upgrade your pinned pipenv dependencies to the latest stable versions.

#### Getting started

```bash
$ pip install pipfile-upgrade

# Move to a directory that contains a Pipfile 
$ cd ~/project

$ pipfile_upgrade
```

It's as easy as that :crossed_fingers:.

#### Arguments

```bash
$ pipfile_upgrade --help

usage: Upgrades your outdated pipfile packages

positional arguments:
  package_blocklist     list of packages to be ignored

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           path where pipfile exists
  -d, --dry, --dry-run  only print outdated package updates
```

#### Local Development

To run the package locally there is a series of make commands which can be found in the [Makefile](Makefile).

This package uses pipenv to manage dependencies, for more information please read the pipenv docs [here](https://pipenv.pypa.io/en/latest/)

#### Testing

A test suite has been included to ensure Reviews functions correctly.

To run the entire test suite with verbose output, run the following:

```bash
$ pytest -vvv
```

Alternatively, to run a single set of tests.

```bash
$ pytest -vvv tests/test_file.py
```

#### Linting

You can lint the project by executing the lint make command. This will run black, isort, mypy, flake8 & vulture.

```shell
make lint
```

You can also set up [pre-commit](https://pre-commit.com/) to run the code quality checks automatically during the commit phase, the pre-commit pipeline can be set up by running the following command on the project root and will run on every commit:

```shell
pre-commit install
```


### Contributions

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.
