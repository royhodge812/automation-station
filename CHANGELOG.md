# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- Initial project setup.
- `roys-instructions.md` and `geminis-instructions.md` to define project goals and roles.
- GitHub Actions workflow for automated daily reporting.
- Python script to generate dummy daily reports.
- `README.md` and `CHANGELOG.md`.

### Changed
- Improved `daily.py` to generate a clean `index.html` with a list of reports.
- Fixed GitHub Actions permissions issue.
- Updated `daily.py` to generate HTML reports in a `dist` directory.
- Updated workflow to deploy the `dist` directory to fix the URL issue.

### Fixed
- GitHub Pages deployment URL resulting in a 404 error.
