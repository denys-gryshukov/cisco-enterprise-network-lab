# Monitoring Cisco devices with LibreNMS

I deployed LibreNMS on Ubuntu in Docker and used it to observe a controlled interface outage on SW2. The session notes record three separate signals: the interface event, the displayed recovery and a notification in a later test.

## Device onboarding

LibreNMS ran with a dispatcher, MariaDB, Redis and a mail relay. From Ubuntu on the private management network, an SNMPv2c read-only query to R1 at 192.168.100.11 returned the expected sysName, `R1.automation.lab`. The application redirected HTTP requests to its login page.

LibreNMS initially reported no SNMP reply during onboarding, and the service was reported unavailable during troubleshooting. In a subsequent session, R1 appeared in LibreNMS and SW2 was added. The records establish the final device state. The exact change that fixed onboarding is unknown.

## SW2 Gi0/1 event and recovery

| Stage | Observation | Interpretation |
| --- | --- | --- |
| Shut down Gi0/1 in the lab | LibreNMS recorded both ifAdminStatus and ifOperStatus changing from up to down. | Both values fit an administrative shutdown. |
| Check notification | The event appeared. No initial notification was received. | The interface event alone establishes detection. |
| Restore Gi0/1 | LibreNMS displayed Up about four minutes later. The configured polling interval was approximately five minutes. | Four minutes describes the observed display delay for this exercise. |
| Repeat alert exercise | A notification was reported for a subsequent administrative-shutdown test. | Its rule, delivery transport and timestamp are unavailable. |
| Check connectivity | SW2 ports showed Up and PC1/PC2 connectivity checks passed. A subsequent SW2 reachability check returned four of four replies. | Monitoring state and connectivity were both checked. |

## Evidence for a repeat run

Record the interface state and time on Cisco, then capture the matching LibreNMS event. Save the rule expression and the delivered notification separately. After restoring the port, repeat the reachability test and capture the recovery time. This would allow a reader to compare device state, poll visibility and notification delivery for one test.

The observations above were reconstructed from interactive lab notes. Original event exports, screenshots and notification records are pending.

[Automation session](python-netmiko-network-verification.md) · [L1 triage runbook](../runbooks/l1-network-incident-triage.md)
