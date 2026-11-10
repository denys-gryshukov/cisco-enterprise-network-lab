# FortiGate Firewall & NAT Troubleshooting Lab

**Platform:** EVE-NG, FortiGate-VM64-KVM / FortiOS 7.4.x (October 2026)  
**Type:** Independent hands-on lab, not production experience  
**Status:** Core connectivity and policy/NAT troubleshooting practiced; a sanitized configuration and full evidence capture still need to be published.

## Objective

Understand how routing, firewall policies and NAT determine whether traffic crosses a FortiGate, and use diagnostic output to investigate a blocked connection.

## Work performed

- Configured FortiGate lab interfaces, a default route, firewall access policy and source NAT.
- Investigated traffic matching using FortiGate flow debugging and policy checks.
- Checked whether the intended security policy was selected and whether a matching default route existed.
- Adjusted the lab's routing/policy/NAT configuration during troubleshooting and verified connectivity with ping tests.
- Examined the relationship between source NAT, policy decisions and return traffic.

The original exercise included a matching firewall policy (policy ID **20**) and verification of outbound reachability. The exact before/after device configuration and terminal output are **not included in this repository**; therefore the steps above are not presented as reproducible proof.

## Diagnostic approach

1. Confirm interfaces, source/destination addressing and intended path.
2. Check route selection, especially the default route.
3. Inspect policy matching and the order/criteria of firewall policies.
4. Verify NAT mode and translation behavior for the observed traffic.
5. Use FortiGate flow diagnostics to identify whether a packet is permitted, denied, or mismatched.
6. Repeat the original connectivity test and record the observed result.

Useful **read-only** FortiOS commands for future evidence collection:

```text
get router info routing-table all
show firewall policy
diagnose sys session list
```

For flow debugging, follow an approved lab-only procedure and turn off debug afterwards. Do not run broad debugging on production firewalls without authorization.

## Evidence to publish next

- Sanitized interface/route/policy/NAT snippets
- A short failed-traffic observation with a matching debug-flow excerpt
- The corrected lab state and the same test repeated
- A concise explanation of the root cause and verification

## Skills demonstrated

FortiGate policy matching, source NAT, default routing, network troubleshooting methodology, traffic-flow analysis.
