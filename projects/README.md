# Project index and evidence

These independent labs support the projects section of my network engineering CV. Device names recur across labs. Each link points to the environment where the observation was made.

| Project and skill | What I can demonstrate | Source |
| --- | --- | --- |
| Cisco + FortiGate troubleshooting | Investigated ten controlled scenarios across switching, routing, access control, NAT and application reachability. Recorded the test and outcome for each. | [Case records](2026-11-17-cisco-fortigate-troubleshooting/cases.md) and [transcribed CLI excerpts](2026-11-17-cisco-fortigate-troubleshooting/README.md#session-excerpts) |
| LibreNMS monitoring | Deployed LibreNMS in Docker, added Cisco devices via SNMP and observed an administrative interface shutdown and recovery. | [Monitoring session notes](librenms-monitoring-work-in-progress.md) |
| Python automation | Collected R1 interface status with Netmiko and investigated an SSH key-exchange mismatch. An October session succeeded. The November failure is open. | [SSH session records](python-netmiko-network-verification.md) and [read-only example](network-automation/README.md) |
| Cisco routing and switching | Verified OSPF neighbors and IPv4 ECMP, HSRP roles, spanning-tree roots and LACP member state. Inspected DHCP leases, ACL counters and switch security state. | [Campus evidence register](cisco-enterprise/README.md#verification-and-evidence) |

## Evidence readers can review

- **Device output.** Original Cisco CLI captures are in [verification](../verification). Route code `O` identifies OSPF in the ECMP example. Prior EIGRP practice has no archived output here.
- **Session record.** The dated reports reconstruct observations from interactive exercises. The original PCAPs, notification records and Python SSH transcripts have yet to be archived.
- **Reusable practice material.** The [triage template](../runbooks/l1-network-incident-triage.md), [firewall rollback reference](2026-11-17-cisco-fortigate-troubleshooting/runbook.md) and [collector](network-automation/README.md) can guide another run. The collector page lists its local validation separately.

The [October FortiOS 7.4 exercise](fortigate-firewall-nat-troubleshooting.md) used policy 20. The [November FortiOS 7.6.2 exercise](2026-11-17-cisco-fortigate-troubleshooting/README.md) used policy 1.

## Open verification items

| Area | Evidence needed to close it |
| --- | --- |
| Campus NAT | Verify R1 Gi0/2 against the live configuration and test traffic through each internal path. [Audit](../troubleshooting/nat-interface-audit.md) |
| Campus redundancy and IPv6 | Capture HSRP roles and host reachability before, during and after failover. Capture IPv6 host-to-host tests. [Test scope](cisco-enterprise/README.md#follow-up-tests) |
| Firewall | Archive paired packet captures and sanitized configuration for a repeat of a documented case. |
| Monitoring | Capture a timestamped event, alert rule, delivered notification and recovery for the same test. |
| Automation | Record the current SSH environment and a live collector run per device. |
