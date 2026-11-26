# Network Monitoring — LibreNMS / Docker / SNMP

**Period:** November 2026 | **Environment:** Personal EVE-NG and Ubuntu lab | **Status:** Device onboarding and a controlled interface event/recovery exercised; raw monitoring evidence pending.

## Objective

Practice the L1 monitoring workflow: onboard a network device, establish visibility, detect a change, investigate it and confirm recovery.

## Environment

- Ubuntu monitoring/management host, private management subnet `192.168.100.0/24`.
- LibreNMS deployed using Docker with application, dispatcher, MariaDB and Redis services (mail relay also present).
- Cisco R1 management address: `192.168.100.11`; SW2 was subsequently added to LibreNMS. SW2's address is not asserted here.
- SNMPv2c read-only monitoring in an isolated lab. Community values are deliberately omitted; prefer SNMPv3 for appropriate production deployments.

## Investigation 01 — SNMP and device onboarding

| Step | Observed result |
|---|---|
| Test SNMP from Ubuntu to R1 | `snmpget` returned the expected sysName.0 response; hostname recorded as R1.automation.lab. |
| Check Docker and web application | Services started; HTTP redirected to login. |
| Initial LibreNMS onboarding | R1 addition failed with an SNMP no-reply error; the service was also reported unavailable during troubleshooting. |
| Subsequent session | R1 successfully added via SNMPv2c and visible in the application; SW2 also added. |

The initial failure's exact root cause and corrective change are not fully documented. Direct SNMP success and subsequent onboarding are separate observations, not proof that a particular change resolved the earlier failure.

## Investigation 02 — Controlled interface-down event

**Device:** Cisco SW2, Gi0/1. **Test:** intentionally administratively shut down a lab interface.

| Phase | Observation |
|---|---|
| Inject fault | Administrative shutdown of SW2 Gi0/1. |
| Detect | LibreNMS recorded ifOperStatus and ifAdminStatus transitions from up to down. |
| First alert check | Event visible, but no alert initially received. |
| Recovery | Interface restored; LibreNMS displayed Up again after approximately four minutes. |
| Subsequent alert test | A notification/alert was reported received for an administrative-shutdown test. Polling interval was left at approximately five minutes. |
| Final connectivity | SW2 ports reported Up; PC1/PC2 connectivity tests succeeded. A subsequent SW2 reachability check recorded 4/4 replies, 0% loss. |

These are observations reconstructed from interactive lab records, not exported LibreNMS events or timestamped alert screenshots. The exact rule expression, notification transport and alert/recovery timestamps are not archived. An event is not the same as an alert; an administrative shutdown is not the same as an unplanned physical-link fault.

## L1 operational workflow (repeatable checklist, not a new test result)

1. Establish baseline device reachability, SNMP response and interface state.
2. Record affected device/interface, expected impact and time.
3. Correlate LibreNMS event state with Cisco `show interfaces status` / `show interfaces Gi0/1` and endpoint connectivity.
4. Restore the interface only in the authorized lab; verify the same connectivity checks and monitoring state.
5. Review rule conditions, polling latency and notification delivery separately; capture actual event and recovery evidence.

## Evidence to archive

- Sanitized SNMP sysName response, device status and polling/discovery output.
- Before/during/after SW2 port-state screenshots, alert rule and actual alert record.
- Notification transport and recovery timestamp, if validated.
- Repeat test with an operational link-down condition (admin up), distinct from the administrative-shutdown test.

## Portfolio summary

Deployed LibreNMS in Docker, onboarded Cisco devices via SNMP and exercised controlled interface-state monitoring, alert detection and recovery. Direct SNMP and reported test observations support the practical exercise; original exported logs and screenshots remain pending.

Related: [Python/Netmiko verification](python-netmiko-network-verification.md) · [L1 incident triage runbook](../runbooks/l1-network-incident-triage.md)

This is independent lab practice, not commercial NOC experience or a claim of production SLA performance.
