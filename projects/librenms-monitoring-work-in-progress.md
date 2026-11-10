# LibreNMS Network Monitoring Lab — In Progress

**Platform:** Linux / EVE-NG / LibreNMS  
**Type:** Independent monitoring practice (November 2026)  
**Status:** **Installation completed; network-device monitoring is not yet demonstrated.**

## Goal

Build an entry-level network operations monitoring workflow: device onboarding, availability checks, interface monitoring, and initial incident triage.

## Progress so far

- Used an existing cloud-hosted EVE-NG/Linux lab environment.
- Installed LibreNMS and reached the installation success screen.
- Worked through basic local application / web access and connectivity checks.
- Continued preparing the environment for monitoring lab devices.

The current notes **do not** establish that Cisco or Fortinet devices were discovered, polled by SNMP, graphed or alerted on. Until there is evidence of these steps, this is an installation/setup exercise rather than a completed monitoring project.

## Intended validation steps (not yet completed)

1. Confirm the web interface is reachable and authentication works.
2. Configure a suitable test device for read-only SNMP in the isolated lab.
3. Add the device to LibreNMS and verify discovery/polling.
4. Check interface status, traffic graphs and availability over a useful period.
5. Trigger a controlled **lab-only** interface-down event and capture the alert and recovery.
6. Document a sample incident, verification commands and escalation/handover notes.
7. Store sanitized screenshots and outputs with clear timestamps.

## Evidence to publish next

- Device-discovery result and successful SNMP polling
- Interface monitoring data and a controlled alert/recovery example
- Short troubleshooting record for a monitoring issue

## Skills being developed

Network monitoring, SNMP fundamentals, Linux services, incident investigation and operational documentation.

**Do not represent this project as completed network monitoring experience until the validation steps have been performed.**
