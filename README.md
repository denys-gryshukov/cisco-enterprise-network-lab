# Network engineering labs | Denys Gryshukov

I built these EVE-NG labs to practice the work of a junior network engineer: trace a failed connection, interpret a monitoring event and verify how routers and switches forward traffic.

| Project | A result you can inspect |
| --- | --- |
| [Cisco + FortiGate fault investigation](projects/2026-11-17-cisco-fortigate-troubleshooting/README.md) | When PC1 lost internet access, FortiGate allowed the traffic. A WAN capture showed PC1’s private source address leaving the firewall. Ping recovered after source NAT was restored. [Case 02](projects/2026-11-17-cisco-fortigate-troubleshooting/cases.md#02--policy-allows-traffic-but-ping-fails) |
| Network monitoring and automation | LibreNMS recorded a controlled SW2 interface outage and recovery. In a separate session, Python/Netmiko collected R1 interface state over SSH. [Monitoring timeline](projects/librenms-monitoring-work-in-progress.md) · [Automation session](projects/python-netmiko-network-verification.md) · [Python collector](projects/network-automation/README.md) |
| [Cisco enterprise network](projects/cisco-enterprise/README.md) | R1 installed two equal-cost paths to four IPv4 VLAN prefixes with OSPF. In a separate EIGRP test, R1 installed two paths to VLAN 10. [OSPF output](verification/ospf.txt) · [EIGRP output](verification/eigrp-vlan10.txt) |

## Network topology

The [enterprise topology and addressing plan](projects/cisco-enterprise/README.md#network-topology) covers the redundant Cisco campus. The [firewall topology](projects/2026-11-17-cisco-fortigate-troubleshooting/README.md#topology) uses a single router and a FortiGate edge.

## Verification and evidence

The campus lab includes nine [archived CLI captures](projects/cisco-enterprise/README.md#verification-and-evidence). The FortiGate, monitoring and SSH reports identify observations transcribed from lab sessions. The [project index](projects/README.md) maps each skill to its source and records the open verification items.

[Network incident triage runbook](runbooks/l1-network-incident-triage.md) · [Open R1 NAT investigation](troubleshooting/nat-interface-audit.md)
