# Network Engineering Lab Portfolio

Independent hands-on networking projects, aligned with entry-level Network Operations / NOC roles. These are personal learning environments, not commercial customer incidents.

## Featured projects

| Project | Practical result | Evidence |
|---|---|---|
| [Cisco + Fortinet Network Fault Investigation](2026-11-17-cisco-fortigate-troubleshooting/README.md) | Ten controlled investigations: VLANs, trunks, routing, ACLs, policies, SNAT, session inspection and DNS/service reachability. | Interactive CLI and Wireshark observations transcribed; raw PCAPs/configuration exports pending. |
| Network Monitoring and Automation — [LibreNMS](librenms-monitoring-work-in-progress.md) / [Python + Netmiko](python-netmiko-network-verification.md) | SNMP device onboarding, controlled interface event/alert and recovery; single-router CLI collection and SSH interoperability diagnosis. | Observations from prior sessions; original alerts, device outputs and script pending. October SSH success does not establish resolution of November regression. |
| [Cisco Enterprise Network](../README.md#network-topology) | OSPFv2 FULL adjacencies and ECMP, OSPFv3 learned routes, HSRP roles, Rapid-PVST+, LACP, DHCP and security state. | Original [Cisco verification outputs](../verification/ospf.txt) linked from the main README. Failover, IPv6 endpoint tests and NAT audit outstanding. |

## Supporting practice

- [FortiGate 7.4 firewall and NAT troubleshooting](fortigate-firewall-nat-troubleshooting.md): earlier October exercise; separate from the FortiOS 7.6.2 investigation.
- [Read-only Netmiko example](network-automation/README.md): illustrative code, not a tested live-device script.
- [L1 network incident triage runbook](../runbooks/l1-network-incident-triage.md): learning template, not a production incident record.
- [Cisco/FortiGate lab rollback runbook](2026-11-17-cisco-fortigate-troubleshooting/runbook.md): controlled lab baseline.

## Protocol scope

OSPF equal-cost routes in the enterprise topology were learned via **OSPF**, not EIGRP. Earlier learning history includes EIGRP AS 100 and variance practice in October 2025, but no original EIGRP CLI output or configuration has been recovered for this portfolio; it is separate from the documented OSPF evidence. BGP and VPN theory are not presented as verified practical projects.

## Evidence standards

- **Archived CLI:** original saved device outputs; strongest evidence in this repository.
- **Observed / transcribed:** actual session observations reconstructed from earlier lab records, with limitations stated.
- **Example / planned:** learning material or future checks; not evidence of execution.

Keep lab topologies separate. Never publish credentials, SNMP communities, SSH private keys, cloud public management addresses, licensed images or customer information. Outstanding tests are not described as completed.

## Next steps

Export sanitized Cisco and FortiGate configurations, archive paired packet captures, capture LibreNMS polling and alert/recovery evidence, validate the current Netmiko environment, and close the enterprise NAT and HSRP verification gaps with before/after tests.
