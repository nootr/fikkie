# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
