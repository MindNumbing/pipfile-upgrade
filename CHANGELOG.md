# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Added CONTRIBUTING.md for contributor guidelines.
- Added types-requests to pipfile.
- Added pre-commit support.
- Added arguments for only_dev and only_required to allow upgrading of only one part of the pipfile.

### Changed
- Changed mypy to not use --strict.
- Renamed test/ -> tests/.
- Renamed instances of *constraints -> *constraint
- Updated readme with more documentation with regards to running / linting the project.

## [0.0.2] - 2022-03-22
### Added
- Created CHANGELOG to record changes between versions.
- Created dataclasses.py to handle domain objects for pipfile format and dependency objects.
- Created errors.py to store file access errors.
- Added an argument_parser which parses arguments provided to the package with support for blocked package updates,
  file path configuration and a dryrun.
- __main__.py was added to make package executable, call the argument parser and run control code.
- pipfile.py is the main code that calls for creation of the tomlfile and controls when upgrades are performed.
- tomlfile.py handles parsing of the tomlfile into a usable format and is used to save off data once upgrades
  are finished.
- Added helper file: Makefile.
- Added dependency management: Pipfile, Pipfile.lock.
- Added repo documentation: README.md, License.txt.
- Added configuration files for tooling: .gitignore, .flake8.
- Added package deployment code: pyproject.toml, setup.py.
