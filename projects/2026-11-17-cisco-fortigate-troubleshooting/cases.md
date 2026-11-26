# Ten controlled troubleshooting cases

These records follow the 17 November [lab topology](README.md#topology). The observations come from that session. Cases 07–09 also document preventive routing, intentional filtering and session verification.

## 01 — Internet ping stops at the firewall

PC1 lost internet reachability after policy 1 was disabled. FortiGate Debug Flow reported `Denied by forward policy check (policy 0)`. The packet had reached the firewall, so the first useful change was to restore the outbound allow policy. PC1’s internet ping then passed.

## 02 — Policy allows traffic but ping fails

With source NAT disabled, Debug Flow showed a policy permit. Wireshark on the WAN side showed ICMP from 192.168.10.10 to 8.8.8.8, with no observed replies. The source address identified the missing translation. Re-enabling NAT on policy 1 restored ping. The upstream drop location remains unknown.

## 03 — R1 has no default route

PC1 received Destination Host Unreachable after R1’s default route was removed. The capture showed echo requests and unreachables. R1 reported `Gateway of last resort is not set`. Restoring the default route via 10.0.0.1 restored the internet ping.

## 04 — PC1 cannot resolve its gateway

PC1 kept its VLAN 10 address when its access port was moved to VLAN 20. Wireshark showed unanswered ARP requests for 192.168.10.1. The access-port assignment placed those broadcasts outside the gateway’s VLAN. Returning SW1 Ethernet0/1 to VLAN 10 restored gateway and internet pings.

## 05 — Gateway responds but server is unreachable

PC1 still reached its gateway while ping to SRV1 showed 100% loss. SW1’s trunk output listed only VLANs 10 and 99 as allowed, active and forwarding. Adding VLAN 20 back to the allowed list restored the server ping. This test preceded the intentional ICMP filter in case 08.

## 06 — Loss of a connected route

When R1 Ethernet0/1.20 was shut down, the subinterface reported administratively down/down and the connected server route disappeared. PC1 received repeated TTL-exceeded messages, and tracepath failed to reach SRV1. R1’s default route and FGT1’s /16 return route explained the apparent loop. Bringing the subinterface up restored four of four replies and a trace to the server.

## 07 — Contain the routing loop

R1 received a discard route for 192.168.0.0/16 via Null0 with administrative distance 250. With VLAN 20 down again, PC1 now received Destination Host Unreachable from R1. The /16 matched before the default route. Once VLAN 20 returned, its connected /24 took precedence over the discard. Both server and internet tests returned four of four replies.

## 08 — SSH port available while ICMP is denied

An inbound ACL on R1 Ethernet0/1.10 permitted TCP/22 from PC1 to SRV1 and denied ICMP for the same pair. A Netcat connection to TCP/22 succeeded. The ACL recorded five TCP permit matches, four ICMP denies and four matches on the final IP permit. The test established TCP port reachability. The ACL remained in place.

## 09 — DNS and stateful return traffic

PC1’s resolver lacked upstream DNS servers. Temporary per-link DNS settings restored name resolution and an HTTPS request returned HTTP/2 200. FortiGate session entries showed policy 1, outbound SNAT and reverse translation on replies. The resolver settings were applied with `resolvectl dns ens3 1.1.1.1 8.8.8.8` and `resolvectl domain ens3 '~.'`. Persistence across reboot was outside the test.

## 10 — Ping works while DNS and HTTPS fail

Restricting policy 1 to PING left ICMP healthy at four of four replies. Debug Flow showed a TCP/53 SYN denied by policy 0 after route lookup. A separate TCP/443 test by IP timed out, removing DNS from that test. Restoring service ALL yielded four of four ping replies, a successful TCP/443 connection and HTTP/2 200. The archived transcription identifies the explicit denial for TCP/53.

[Session excerpts](README.md#session-excerpts) · [Rollback reference](runbook.md)
