# L1 Network Incident Triage Runbook (Practice Template)

**Scope:** A study and documentation template for simulated incidents in an EVE-NG lab. **Not** a record of a production incident or experience with a commercial ticketing platform.

## Initial intake

Record the time (with time zone), affected site/device/interface, source and destination, symptoms, business impact, and first/last known good status. Distinguish a single-host issue from a wider network outage. Avoid making configuration changes before identifying impact and authorization.

## Read-only troubleshooting workflow

1. **Confirm scope:** What fails? For whom? Is the issue intermittent? Can it be reproduced?
2. **Layer 1 / 2:** Check link/admin status, interface errors, VLAN membership, trunks, STP and EtherChannel where applicable.
3. **Layer 3:** Check addressing, gateway, ARP, route selection, routing adjacencies and reachability from each relevant hop.
4. **Security / NAT:** Check relevant ACLs, firewall policy matching and NAT only for the path in question.
5. **Evidence:** Record the exact command, device, timestamp and redacted output. Compare to known-good state.
6. **Resolution / escalation:** Perform only authorized L1 actions. Escalate with impact, evidence, attempted tests, suspected cause and next recommended checks.
7. **Handover:** Summarize the current state, open questions, owner and immediate next step.

### Example Cisco IOS verification commands

    show ip interface brief
    show interfaces status
    show interfaces counters errors
    show vlan brief
    show interfaces trunk
    show etherchannel summary
    show spanning-tree
    show ip route
    show ip ospf neighbor
    show standby brief
    show access-lists

Commands are device/platform-dependent: use only those supported in the relevant lab image. A command list is **not** proof of successful execution.

## Sample incident report fields

| Field | Information to capture |
|---|---|
| Ticket ID | Lab placeholder, not a fabricated ITSM number |
| Reported / detected | Date, local time and time zone |
| Severity and impact | Affected hosts, users, applications and urgency |
| Affected devices | Hostname, role, interface (sanitize addresses) |
| Symptoms | Error message and steps to reproduce |
| Tests and evidence | Commands, outputs, ping/traceroute results |
| Suspected cause | Explicitly label hypothesis vs confirmed result |
| Changes | Authorized actions only, with timestamps |
| Outcome | Resolved, monitoring or escalated |
| Handover | Next owner, outstanding questions and follow-up |

## What has been validated?

This document itself is an **L1 operational checklist**. It does not claim that a real service incident, escalation or customer handover occurred. The repository's existing verification files contain actual lab CLI outputs, with separate known limitations listed in the main README.
