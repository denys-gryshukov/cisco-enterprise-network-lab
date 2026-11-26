# Network Automation — Cisco CLI Verification with Python / Netmiko

**Period:** October–November 2026 | **Environment:** Ubuntu, Python, Netmiko, Cisco EVE-NG lab | **Status:** Single-device CLI check executed; reusable multi-device automation and later SSH compatibility require validation.

## Objective

Establish management access to Cisco devices and collect operational state using a read-only Python workflow.

## Management addressing

| Device | Private lab IP |
|---|---|
| Ubuntu automation host | 192.168.100.10 |
| R1 | 192.168.100.11 |
| R2 | 192.168.100.12 |
| SW1 management | 192.168.100.13 |

The automation topology is separate from the enterprise OSPF/HSRP lab and the 17 November FortiGate lab.

## Investigation 01 — SSH compatibility (23 October 2026)

**Symptom:** legacy IOS SSH algorithms were not accepted by the modern SSH client. The router offered SHA-1-based Diffie-Hellman KEX and ssh-rsa.

**Diagnostic action:** compared the peer's offered algorithms with the client policy. A narrowly scoped OpenSSH connection succeeded using explicit legacy KEX/host-key options for the isolated lab device. No global SSH security settings were weakened in the documented procedure.

**Corrective action:** changed the Python environment's Paramiko version from 5.1.0 (reported at the time) to 3.5.1. Netmiko subsequently connected to R1.

**Verification:** issued `show ip interface brief` through Netmiko. The recorded observation was:

| Interface | Address | Administrative / operational state |
|---|---|---|
| Gi0/0 | 192.168.100.11 | up/up |
| Gi0/1–Gi0/3 | unassigned | administratively down/down |

This table is a reconstruction of the observed output, not an original archived transcript. The successful session establishes a read-only single-device check, not a tested fleet-wide health-check tool.

## Investigation 02 — Compatibility regression (10 November 2026)

In the later Python environment, a Netmiko run against R1 failed with `NetmikoTimeoutException` caused by `Incompatible ssh peer (no acceptable kex algorithm)`. OpenSSH exposed the legacy KEX offers again. A successful follow-up in that later environment was not recovered from the lab records.

**Status:** October workaround succeeded; November regression remains open. Do not assume that downgrading a library is a permanent or production-safe fix. Prefer supported device firmware and current SSH algorithms; isolate any legacy lab exceptions.

## Reproducible next steps (not yet verified)

- Check IP reachability and SSH negotiation before Python tests.
- Use an isolated virtual environment and record Python, Netmiko and Paramiko versions.
- Run read-only CLI collection against R1, then R2 and SW1 individually.
- Record connection failures, exact commands and output; avoid embedding credentials.
- Test exception handling and compare expected interface state with actual results.

See [read-only sample code](network-automation/README.md). It was written as an educational example and is not the original executed script; live execution remains unverified. Ansible was explored at introductory level only.

## Portfolio summary

Used Python/Netmiko to collect Cisco interface status and investigated SSH key-exchange incompatibility, restoring a successful lab session in October. Subsequent compatibility failure and multi-device automation are explicitly outstanding.

Related: [LibreNMS monitoring](librenms-monitoring-work-in-progress.md).

Independent lab experience only; no commercial automation or production deployment claimed.
