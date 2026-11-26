# FortiGate outbound connectivity | October 2026

I configured interfaces, a default route, firewall policy 20 and source NAT on a FortiGate VM running FortiOS 7.4.x in EVE-NG. I used flow debugging and ping to check outbound connectivity.

## Investigation

| Check | Purpose |
| --- | --- |
| Interface addressing and default route | Establish where the packet enters and which interface should carry it toward the destination. |
| Policy lookup in Debug Flow | Determine whether policy 20 matches the traffic. |
| NAT settings and return traffic | Check whether the outbound source is translated and replies can return. |
| Repeat the ping | Verify outbound reachability after adjusting the lab configuration. |

## Result and evidence

The session record describes a matching policy and successful outbound ping. The exact sequence of configuration changes and the raw flow trace were not archived, so the record does not isolate a single root cause.

The [17 November investigation](2026-11-17-cisco-fortigate-troubleshooting/README.md) used FortiOS 7.6.2 and policy 1. It contains separate policy-denial and missing-SNAT cases with recorded packet observations.
