# Task 003: Inspect existing code and design StatSender architecture

## Summary
Analyze the existing django-statsd middleware to understand how metrics are configured and sent, then design the StatSender architecture for pluggable backends (StatsD, Zabbix, Prometheus).

## Checklist
- [ ] Analyze existing django-statsd middleware (GraphiteMiddleware, GraphiteRequestTimingMiddleware)
- [ ] Understand how metrics are configured and sent (e.g., statsd.incr, statsd.timing)
- [ ] Identify all current metric types and usage patterns
- [ ] Design StatSender base class architecture
- [ ] Define interface for backend-specific subclasses
- [ ] Plan configuration via STATSD_CONFIG dictionary
- [ ] Document requirements for each backend (StatsD, Zabbix, Prometheus)