# L1 troubleshooting runbook — Cisco / FortiGate EVE-NG

Scope: independent lab, not a record of a production incident.

## Workflow
1. Record source, destination, protocol, port, symptom and timestamps. Check whether failure is isolated or widespread.
2. Confirm interface state (`show ip interface brief`; `ip -br addr`), IP, default gateway and relevant routing table (`show ip route`, `get router info routing-table all`).
3. Check L2 domain (`show vlan brief`, `show interfaces ... switchport`, `show interfaces trunk`) and ARP (`ip neigh`, Wireshark `arp`).
4. Determine whether traffic is reaching the firewall, matching a policy, and receiving NAT: `diagnose debug flow`, `diagnose sys session list`.
5. Distinguish ICMP vs DNS vs TCP failures. Use `ping`, `tracepath`, `resolvectl query`, `nc -vz`, and `curl -I`. Test HTTPS via destination IP or `curl --resolve` if DNS is suspect.
6. Apply minimal controlled correction; re-run the **same** baseline tests; document observed results. Save changes only after validation.
7. For ACLs, examine matching counters and direction (`show ip access-lists`, `show ip interface`). A TCP/22 permit rule alone does not prove an SSH login; confirm the service separately.

## Controlled-fault rollback reference
- SW1 PC1 `Ethernet0/1` access VLAN: **10**.
- SW1 uplink `Ethernet0/0`: trunk allowing **10,20,99**.
- R1 `Ethernet0/1.20`: **no shutdown**.
- R1 default route: `ip route 0.0.0.0 0.0.0.0 10.0.0.1`.
- R1 lab-only loop guard: `ip route 192.168.0.0 255.255.0.0 Null0 250`.
- FortiGate policy 1: `set service "ALL"`, `set nat enable`, `set status enable`.
- R1 ACL `USERS_TO_SERVERS` remains **inbound VLAN10**; ICMP PC1→SRV1 intentionally denied, SSH TCP/22 permitted. Do not mistake this policy for a new outage.

Do not publish passwords, API keys, FortiGate config backups containing secrets, private SSH keys or external public cloud IPs. Review exported configurations before committing.
