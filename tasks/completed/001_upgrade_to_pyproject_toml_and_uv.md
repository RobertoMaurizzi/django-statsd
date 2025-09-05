# Task 001: Upgrade to pyproject.toml and uv

## Summary
Upgrade the repository to use modern pyproject.toml configuration and uv for dependency management, replacing the existing setup.py, requirements.txt, and tox.ini files.

## Checklist
- [x] Create pyproject.toml with project metadata and dependencies
- [x] Configure build system in pyproject.toml
- [x] Set up project dependencies including the required libraries (statsd, py-zabbix, prometheus_client)
- [x] Configure development dependencies for testing
- [x] Remove old configuration files (setup.py, requirements.txt, optional.txt)
- [x] Update documentation if needed
- [x] Verify the project can be built and installed with uv

---

# Summary: Upgrade to pyproject.toml and uv

## Overview
Successfully upgraded the django-statsd repository to use modern Python packaging standards with pyproject.toml and uv for dependency management.

## Changes Made

### 1. Created pyproject.toml
- Configured build system with setuptools
- Defined project metadata (name, version, description, etc.)
- Set up dependencies including statsd and optional dependencies for pluggable backends
- Added development dependencies for testing
- Configured package discovery and static file inclusion

### 2. Removed Legacy Files
- Removed setup.py
- Removed requirements.txt
- Removed optional.txt
- Removed MANIFEST.in

### 3. Updated Configuration
- Fixed license format to comply with SPDX standards
- Updated Python version requirements to >=3.8
- Added specific Django framework classifiers
- Specified statsd dependency as >= 3.2.1, < 4.0

### 4. Verified Functionality
- Successfully built the project with uv build
- Successfully installed the package in development mode with uv pip install -e .

## Benefits
- Modern Python packaging standard compliance
- Faster dependency resolution and installation with uv
- Clearer project structure and metadata
- Better support for optional dependencies (zabbix, prometheus)
- Ready for the next phases of the project (pluggable backends)