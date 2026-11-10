# Cisco SSH Verification with Python & Netmiko

**Platform:** Ubuntu Server, Python, Netmiko, Cisco IOL devices in EVE-NG  
**Type:** Independent network automation practice (October–November 2026)  
**Status:** Initial SSH and Netmiko CLI verification completed; the reusable script and execution transcript have not yet been uploaded.

## Objective

Establish management connectivity from a Linux host to lab Cisco devices and use Python/Netmiko to collect operational CLI output.

## Lab layout

Private laboratory subnet: `192.168.100.0/24`.

| Role | Lab address |
|---|---|
| Ubuntu automation host | `192.168.100.10` |
| Cisco router R1 | `192.168.100.11` |
| Cisco router R2 | `192.168.100.12` |
| Cisco switch SW1 (management VLAN) | `192.168.100.13` |

These are **private lab IP addresses**, not internet-facing customer endpoints.

## Work performed

- Prepared an Ubuntu/Python environment and installed Netmiko.
- Tested network reachability and SSH management access to Cisco IOL devices.
- Investigated SSH interoperability issues involving legacy key-exchange algorithms on the lab images.
- Used Netmiko to connect to a Cisco router and run `show ip interface brief` to inspect interface status.
- Practiced basic Linux routing/connectivity checks; explored introductory Ansible concepts.

## Example verification workflow (illustrative, not a claimed captured output)

1. Confirm the Ubuntu host's address and route to the management network.
2. Test IP reachability to each intended device.
3. Verify SSH credentials and permitted algorithms in the **isolated lab**.
4. Use Netmiko to run read-only commands such as `show ip interface brief`.
5. Review interface admin/operational states, recording any down interfaces and their relevance.
6. Store a sanitized command transcript with the device role, timestamp and explanation.

**Security note:** Do not globally enable deprecated SSH key-exchange methods or publish reusable passwords. Modern SSH settings should be preferred outside isolated emulation labs.

## Related code example

A [read-only Netmiko sample](network-automation/README.md) is now available. It is **new example code, not the original script run in October**, and has not yet been tested against the live EVE-NG devices. No captured device output is claimed for it.

## Evidence to publish next

- Tested, sanitized Python script with a `requirements.txt` (without credentials)
- Example CLI output from a lab router
- Error handling for unreachable devices and SSH authentication failures
- A README section describing how to reproduce the test

## Skills demonstrated

Python basics, Netmiko, Cisco IOS CLI verification, SSH troubleshooting, Linux networking, lab automation.
