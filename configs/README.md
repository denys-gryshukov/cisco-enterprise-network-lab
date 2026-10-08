# Configuration exports — pending

This folder does **not yet** contain reproducible device configurations. The topology and verification captures elsewhere in this repository do not replace running configurations.

## Files to add from EVE-NG

- `R1.txt`, `R2.txt`, `R3.txt`, `ISP.txt`
- `SW1.txt`, `SW2.txt`

Use `show running-config` to capture each **lab** device after checking that it matches the documented topology. Include the relevant interfaces, VLANs, routing, NAT, ACL, DHCP and redundancy settings.

**Before publishing:** remove passwords, password hashes, private keys, SNMP community strings, tokens, and any actual production information. Do not commit Cisco software images or license material.

For R1 specifically, compare its NAT inside/outside interface roles with the [open audit](../troubleshooting/nat-interface-audit.md).
