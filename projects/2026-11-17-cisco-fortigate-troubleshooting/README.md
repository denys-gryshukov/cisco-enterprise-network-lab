# Cisco + FortiGate Network Troubleshooting | 17 November 2026

**Independent hands-on EVE-NG lab** · Cisco IOS XE IOL 17.12.1 · FortiOS 7.6.2 · Linux · Wireshark

> This is a personal, controlled learning environment, **not** production or paid networking experience. All recorded faults were intentionally introduced. Observations below come from interactive CLI outputs, packet captures and retests during the lab; complete device configuration exports and raw PCAP attachments are not yet included.

## Purpose

Build a small routed enterprise-like network; practice L2/L3 fault isolation, firewall policy investigation, source NAT verification, ACL validation and session-table interpretation. Document the symptoms, root cause, remediation and verification rather than simply listing technologies.

## Topology (this session)

```text
  GCP/EVE-NG host (pnet1 172.16.100.1/24) -> upstream NAT -> Internet
                        |
              FortiGate FGT1
        port1 172.16.100.2/24
        port2 10.0.0.1/30
                        |
            Cisco R1 e0/0 10.0.0.2/30
            e0/1 802.1Q subinterfaces:
             .10 = 192.168.10.1/24
             .20 = 192.168.20.1/24
             .99 = 192.168.99.1/24
                        |
                 Cisco SW1 e0/0 trunk
             VLAN 10, VLAN 20, VLAN 99
                  /       |        \
       e0/1 VLAN10   e0/2 VLAN20   e0/3 VLAN99
       PC1           SRV1           ADMIN1
       192.168.10.10 192.168.20.10 192.168.99.10
```

The previously documented multi-router OSPF/HSRP topology in this repository is a **different lab**, with a different VLAN plan. Do not combine its equipment or evidence with this experiment.

### Relevant routing and policies

- R1 default route: `0.0.0.0/0 via 10.0.0.1`.
- FortiGate default route: `0.0.0.0/0 via 172.16.100.1 (port1)`.
- FortiGate static return route: `192.168.0.0/16 via 10.0.0.2 (port2)`.
- FortiGate policy ID 1 `LAN_TO_INTERNET`: `port2 -> port1`, `accept`, `service ALL`, SNAT enabled; briefly restricted to `PING` in scenario 10 and restored.
- R1 preventive discard route added in scenario 07: `192.168.0.0/16 -> Null0` (administrative distance 250). More-specific connected /24 routes take precedence by longest-prefix match.
- R1 inbound extended ACL `USERS_TO_SERVERS` on `Ethernet0/1.10` permits PC1 TCP/22 to SRV1, denies ICMP from PC1 to SRV1, then permits other IP traffic. **The ACL remained configured at the end of the recorded session.**

## Investigation method

For each controlled fault, establish the expected path, introduce one change, observe the symptom, isolate the affected layer or policy, correct or intentionally retain the change, then repeat the relevant checks. The evidence type differs by scenario: CLI, packet observation, session counters or connectivity results. Not every scenario used every tool.

## Verified troubleshooting cases

| ID | Fault injected / topic | Primary evidence | Recovery |
|---|---|---|---|
| 01 | FortiGate policy 1 disabled | Debug Flow: `Denied by forward policy check (policy 0)` | Re-enabled policy; PC1 internet ping restored |
| 02 | Source NAT disabled on FortiGate | Debug Flow allowed policy; WAN Wireshark displayed untranslated `192.168.10.10 -> 8.8.8.8` ICMP with no observed replies | Re-enabled NAT; ping restored |
| 03 | R1 default route removed | `Gateway of last resort is not set`; PC1 saw `Destination Host Unreachable`; Wireshark captured requests/unreachables | Restored default route; internet ping passed |
| 04 | SW1 PC1 access port moved VLAN 10 → 20 | `show vlan brief` baseline; Wireshark ARP requests for `192.168.10.1` without replies | Returned port to VLAN 10; gateway and internet pings passed |
| 05 | Removed VLAN 20 from SW1 trunk allowed list | `show interfaces trunk` displayed allowed/active/forwarding VLANs `10,99`; PC1 gateway passed, server ping 100% loss | `switchport trunk allowed vlan add 20`; server ping restored |
| 06 | Shut down R1 VLAN 20 subinterface | `administratively down/down`; route absent; repeated TTL-exceeded reports; tracepath did not reach server | `no shutdown`; PC1→SRV1 4/4 and tracepath reached destination |
| 07 | Prevent routing loop when connected VLAN disappears | Added Null0 /16; after VLAN 20 shutdown, error changed from `Time to live exceeded` to `Destination Host Unreachable` from R1 | Restored VLAN 20; SRV1 4/4 and internet 4/4 |
| 08 | Selectively filter ICMP but permit SSH | Cisco ACL counters: 5 TCP/22 permit, 4 ICMP deny, 4 general IP permit; Netcat TCP/22 succeeded | Intentional filtering retained |
| 09 | Session tracking + temporary DNS resolver fault | FortiGate ICMP/TCP session entries `policy_id=1`, SNAT/return DNAT; resolver lacked upstream servers; `HTTP/2 200` after temporary DNS assignment | DNS working during test; **persistence not configured** |
| 10 | Restrict FortiGate policy service `ALL` → `PING` | ICMP 4/4; DNS TCP/53 SYN denied by implicit policy 0; direct IP TCP/443 test timed out | Reverted service to `ALL`; ping 4/4, Netcat TCP/443 succeeded, HTTPS HTTP/2 200 |

### Representative observations (transcribed, not original raw evidence files)

```text
SW1# show interfaces trunk
Port    Status    Native vlan
Et0/0   trunking  1
Vlans allowed on trunk: 10,99        # injected fault, VLAN 20 missing

R1# show ip access-lists USERS_TO_SERVERS
10 permit tcp host 192.168.10.10 host 192.168.20.10 eq 22 (5 matches)
20 deny icmp host 192.168.10.10 host 192.168.20.10 log (4 matches)
30 permit ip any any (4 matches)

FGT1 (Debug Flow for DNS):
received a packet(proto=6, 192.168.10.10:47890->8.8.8.8:53) from port2, flag [S]
find a route ... gw-172.16.100.1 via port1
Denied by forward policy check (policy 0)

FGT1 (HTTPS session):
proto=6 ... policy_id=1
hook=post dir=org act=snat 192.168.10.10:49152->172.66.147.243:443(172.16.100.2:49152)
hook=pre dir=reply act=dnat 172.66.147.243:443->172.16.100.2:49152(192.168.10.10:49152)
statistic ... org=1429/12/1 reply=6005/12/1
```

## Practical conclusions

1. **The interface can stay up while connectivity fails.** Access-VLAN assignment and trunk allowed VLANs must be checked separately.
2. **Packets can be routable and still be denied by policy.** FortiGate Debug Flow separates route lookup from policy enforcement.
3. **Missing SNAT can cause failed return connectivity.** The observed pre-/post-NAT captures verified translation when enabled and untranslated egress when disabled. The precise upstream drop location was not independently proven.
4. **Routes interact.** R1's default route and FortiGate's broad /16 return route created symptoms consistent with a forwarding loop after a connected /24 disappeared. A /16 discard route, more specific than the default route but less specific than connected /24s, prevented the observed TTL-exceeded behavior in this lab.
5. **An application failure is not always an HTTPS failure.** DNS TCP/53 was explicitly denied after allowing only the PING service; a separate IP-based TCP/443 test timed out.
6. **Stateful inspection is observable.** FortiGate recorded bidirectional sessions and reverse NAT mapping for ICMP and HTTPS.

## Evidence scope and limitations

- Results are based on commands and output shared in an interactive session on 17 Nov 2026; not all outputs were archived as separate timestamped log files.
- Wireshark captures were viewed during the session; raw PCAPs have not been committed.
- The DNS fix used `resolvectl dns ens3 1.1.1.1 8.8.8.8` plus `resolvectl domain ens3 '~.'`. It is **temporary** and may not survive reboot.
- The Cisco ACL continues to intentionally deny ICMP PC1→SRV1; this is expected and must be considered when interpreting future pings.
- The Null0 route `192.168.0.0/16` intentionally drops traffic to otherwise-unknown destinations in that range. This is a specific **lab safeguard**, not a general recommendation for all networks.
- The FortiGate evaluation-license limits constrain number of policies/routes/interfaces; this is not a production security design.
- No claim of commercial network operations experience, full incident-management workflow, untested alerts, or production change implementation.

## Suggested next verification work

- Export sanitized `show running-config`, `show interfaces trunk`, `show ip route`, `show ip access-lists`, FortiGate `show firewall policy` and `get router info routing-table all` outputs.
- Save paired PCAPs for ICMP before/after SNAT and ARP during wrong-access-VLAN test.
- Validate TCP SYN/SYN-ACK/ACK and RST-vs-timeout with Wireshark in a new controlled exercise.
- Add a rollback checklist, timestamped verification table, and monitoring/automation integration.

**Portfolio-ready, accurately scoped description:** Investigated ten controlled fault and verification scenarios involving routing, VLANs, trunks, ACLs, firewall policies and SNAT using Cisco IOS XE, FortiOS Debug Flow and Wireshark. Validated changes with scenario-specific CLI counters, packet observations, session/NAT entries and connectivity retests. Intentional ACL filtering was retained; the DNS repair was temporary.
