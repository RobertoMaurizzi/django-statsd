Product Requirements Document (PRD): django-statsd Fork with Pluggable Backends

# 1. Overview

This PRD outlines requirements for a fork of the django-statsd project, extending its functionality to support pluggable backends for sending statistics to StatsD, Zabbix (via py-zabbix), and Prometheus, in addition to the existing Graphite integration. The fork will refactor the codebase to encapsulate statistics handling in a StatSender class and allow configuration of the backend via a STATSD_CONFIG dictionary in Django's settings.py.

# 2. Objectives

Enhance django-statsd to support multiple monitoring backends (StatsD, Zabbix, Prometheus).
Refactor statistics sending logic into a modular StatSender class.
Enable flexible backend configuration via a STATSD_CONFIG dictionary in settings.py.
Maintain compatibility with existing django-statsd functionality.

# 3. Requirements

## 3.1 Pluggable Backends

StatsD: Retain existing functionality to send metrics to a StatsD server over UDP for Graphite integration.
Zabbix: Add support for sending metrics to Zabbix using the py-zabbix library, compatible with Zabbix trapper items. Metrics will use the full stat name as the item key, with underscores replaced by periods.
Prometheus: Add support for exporting metrics to Prometheus via a statsd_exporter sidecar, transforming StatsD-style metrics into Prometheus-compatible formats (e.g., hello_requests_total_counter).

## 3.2 Code Inspection and Refactoring

Inspection: Analyze existing django-statsd middleware (GraphiteMiddleware, GraphiteRequestTimingMiddleware) to understand how metrics are configured and sent (e.g., statsd.incr, statsd.timing).
Refactoring: Encapsulate all metric-sending logic into a StatSender class. This class will:
Handle metric formatting and transmission for each backend.
Support counters, timers, and gauges.
Map Django metrics to backend-specific formats (e.g., Zabbix keys, Prometheus counters).

## 3.3 Configuration in settings.py

Allow specification of the StatSender class and its configuration via a STATSD_CONFIG dictionary in settings.py.
The STATSD_CONFIG dictionary will specify the backend class as the key and its configuration as a sub-dictionary.
Example settings.py configuration:STATSD_CONFIG = {
'myapp.stats.StatsDSender': {
'host': 'localhost',
'port': 8125,
},
'myapp.stats.ZabbixSender': {
'host': 'zabbix.example.com',
'port': 10051,
'target_hostname': 'host.example.com',
},
'myapp.stats.PrometheusSender': {
'exporter_host': 'localhost',
'exporter_port': 9102,
},
}

Support multiple backends simultaneously by iterating over STATSD_CONFIG keys and instantiating each StatSender subclass with its respective configuration.

## 3.4 Middleware Integration

Update GraphiteMiddleware and GraphiteRequestTimingMiddleware to use the configured StatSender classes from STATSD_CONFIG for sending metrics.
Ensure middleware remains compatible with Django versions (1.10+ for is_authenticated, etc.).
Preserve existing functionality (e.g., response code tracking, authenticated user metrics).

## 3.5 Debugging and Testing

Retain debug mode to log metrics without sending to backends.
Add unit tests for each backend to validate metric formatting and transmission.
Include integration tests for Django middleware with each backend.

## 3.6 Project Development tracking

Keep track of all tasks you're asked to do by creating a new file for each in the directory ./tasks
Name the files with a three-digit-number, an underscore then a short description, like 001_refactor_statsd_config_into_class.md, 002_add_support_for_zabbix.mdm, etc. and increment the number when you create a new task.
This file should contain a summary of the request then a checklist of sub-tasks to be done, each starting with `- [ ]`
If during interaction the user asks for any change to any tasks, evaluate the request then update the existing file with the new specifications.
While you work on the tasks, update the task file by marking completed sub-tasks with `- [x]`
When you complete all subtasks of a task, ask the user to confirm it's completed and if yes move the file to the directory ./tasks/completed
After each task completion, append a summary of what was done and the problems encountered, both solved and still pending, at the end of the
task file in the ./task/completed directory.
Create directories and files as needed using tools.

# 4. Technical Specifications

Dependencies:
statsd (Python client for StatsD).
py-zabbix (for Zabbix integration).
prometheus_client (for Prometheus integration via statsd_exporter).

Code Structure:
statsender.py: Define StatSender base class and backend-specific subclasses (StatsDSender, ZabbixSender, PrometheusSender).
middleware.py: Update to instantiate and use configured StatSender classes from STATSD_CONFIG.
settings.py: Add STATSD_CONFIG dictionary parsing.

Compatibility: Support Django 1.11+ and Python 3.6+.

# 5. Deliverables

Forked django-statsd repository with pluggable backends.
Updated middleware using StatSender with STATSD_CONFIG.
Configurable backend selection via STATSD_CONFIG dictionary.
Documentation for setup, configuration, and usage.
Unit and integration tests for all backends.

# 6. Success Criteria

Metrics successfully sent to StatsD, Zabbix, and Prometheus backends.
Seamless integration with existing Django projects.
No performance degradation compared to original django-statsd.
Comprehensive test coverage (>80%).

# 7. Initial tasks

1. Upgrade the repository to use pyproject.toml and uv
2. Replace the testing system with one using tox and pytest, testing only recent (supported) versions of Django and Python.
3. Inspect existing code, design StatSender architecture.
4. Implement StatSender and backend subclasses.
5. Update middleware, add STATSD_CONFIG parsing.
6. Write tests, documentation, and release fork.

# 8. Risks and Mitigation

Risk: Backend-specific formatting errors.
Mitigation: Rigorous testing for each backend, validate metric formats.

Risk: Performance overhead from new abstractions.
Mitigation: Benchmark and optimize StatSender implementation.

Risk: Compatibility issues with older Django versions.
Mitigation: Test across supported Django versions, use conditional imports.
