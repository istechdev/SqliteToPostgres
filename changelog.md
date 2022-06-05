# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [DEV - Version9] - 2022-06-04
### Added
### Changed
### Removed
### Fixed
## [DEV - Version10] - 2022-06-05
### Added
- sqlalchemy engine disposal after data transfer
### Changed
- sqlite and pg database parameters and config function were put in inicializations at the beginning of the script
- same names of the parameters were changed
- all parameters definitions were taken to the pg.ini file
- number of Bloques diminish from 6 to 5
- the data transfer is made with "with" and a connection

## [DEV - Version9] - 2022-06-04
### Changed
- Table names autochange in the convertion

## [DEV - Version8] - 2022-05-27
### Added
- changelog.md
- requirements-dev.txt
### Changed
- requirents.txt (short version - only primary packages)
