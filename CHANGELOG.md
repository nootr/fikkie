# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.4] - 2022-01-08
### Upgraded
- Upgraded celery to 5.2.2 to fix CVE-2021-23727

## [0.3.3] - 2021-12-21
### Added
- Added type checking to CI/CD pipeline
- Added functional tests for Ubuntu and MacOS to CI/CD pipeline

### Fixed
- Fixed issues in the `fikkie init` command

## [0.3.2] - 2021-12-20
### Added
- Added argument to select output format
- Added argument to select loglevel
- Added supported Python versions to documentation

### Changed
- Changed default output format to YAML

### Fixed
- Fixed broken link in documentation

## [0.3.1] - 2021-12-19
### Added
- Added missing typing_extensions dependency which is needed for Python 3.7

### Changed
- Improved documentation

## [0.3.0] - 2021-12-17
### Added
- Added CLI client to control daemon and read check data

## [0.2.2] - 2021-12-16
### Fixed
- Fixed bug where an UTF-8 character was included in an ASCII-decoded string

## [0.2.1] - 2021-12-16
### Fixed
- Fixed bug where an UTF-8 text was sent to e-mail which only supports ASCII

## [0.2.0] - 2021-12-16
### Added
- Added e-mail notifier
- Added CLI flag to initialize workspace

### Fixed
- Fixed bug with empty config file

### Changed
- Improved documentation

## [0.1.0] - 2021-12-15
### Added
- Added Celery-based watchdog
- Added Telegram notifier
- Added CI/CD with linting, tests and packaging
- Added documentation
