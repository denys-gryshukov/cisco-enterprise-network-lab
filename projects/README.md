# Additional Hands-on Networking Labs

These notes document independent practice associated with Cisco networking, network security, automation, and monitoring. They are **lab projects**, not paid network engineering work or production customer incidents.

| Project | What was practiced | Evidence status |
|---|---|---|
| [FortiGate Firewall and NAT Troubleshooting](fortigate-firewall-nat-troubleshooting.md) | FortiOS 7.4, policies, default routing, source NAT and debug flow | Practical steps described; sanitized device configurations and CLI logs not yet committed |
| [Cisco SSH Verification with Netmiko](python-netmiko-network-verification.md) | Linux SSH connectivity, Cisco IOS command collection through Python/Netmiko | Initial Netmiko connection and show-command run completed; script and saved output not yet committed |
| [LibreNMS Monitoring Setup](librenms-monitoring-work-in-progress.md) | Linux-based monitoring installation and service setup | Installation reached success; network device discovery, SNMP polling and alert validation **not yet demonstrated** |

The primary [Cisco Enterprise Network Lab](../README.md) separately includes a topology diagram and actual CLI verification evidence for routing, switching, redundancy and security. Its documented unresolved NAT discrepancy and missing failover captures are not described as resolved.

## Supplementary practice resources

- [Netmiko read-only Python example](network-automation/README.md) — newly written example with a sample inventory; live-device execution not yet verified
- [L1 network incident triage runbook](../runbooks/l1-network-incident-triage.md) — study template for intake, diagnostics, escalation and handover; not a production incident record

## Next evidence to add

- Export sanitized, relevant configuration snippets and actual troubleshooting outputs
- Publish the Netmiko script after removing all credentials, tokens and sensitive values
- Document a completed monitoring workflow with device discovery, interface polling and alert testing
- Add dated before/after tests for each investigated issue

## Information security

Use only lab addresses and fictitious names. Do not publish passwords, SSH private keys, API tokens, SNMP communities, real customer information, or licensed device images.
