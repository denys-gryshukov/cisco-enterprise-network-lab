# Collecting Cisco interface state with Python and Netmiko

I used an Ubuntu host to read Cisco interface state over SSH. Two sessions show why the client environment matters when working with older IOS images.

| Management node | Lab address |
| --- | --- |
| Ubuntu | 192.168.100.10 |
| R1 | 192.168.100.11 |
| R2 | 192.168.100.12 |
| SW1 | 192.168.100.13 |

## 23 October 2026 · Successful R1 session

SSH negotiation failed with the legacy IOS offer. Comparing the router’s offered algorithms with the client settings isolated a key-exchange compatibility issue. A device-specific OpenSSH test succeeded. The session notes record a change in the isolated Python environment to Paramiko 3.5.1, followed by a successful Netmiko connection to R1.

Netmiko returned the following interface state for `show ip interface brief`. The table transcribes the observation from the session notes.

| R1 interface | IP address | Status / protocol |
| --- | --- | --- |
| Gi0/0 | 192.168.100.11 | up/up |
| Gi0/1–Gi0/3 | Unassigned | administratively down/down |

## 10 November 2026 · Later SSH failure

A later R1 run raised `NetmikoTimeoutException` with `Incompatible ssh peer (no acceptable kex algorithm)`. The OpenSSH client again reported legacy key-exchange offers. A successful retest in this later environment remains open.

## Reusable collection example

The [Python collector](network-automation/README.md) takes a JSON inventory and requests interface and routing state. It was written after the original R1 session. Its README includes the exact local validation procedure. Live outputs for this implementation, including R2 and SW1, remain to be captured.

[LibreNMS monitoring](librenms-monitoring-work-in-progress.md) · [Project index](README.md)
