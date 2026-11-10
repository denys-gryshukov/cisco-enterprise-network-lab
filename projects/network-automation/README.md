# Netmiko Cisco Read-only Verification — Code Example

This is a **new, educational code example** based on an earlier EVE-NG lab in which Cisco CLI commands were collected with Netmiko. It is **not the original executed script** and is **not yet validated against the running lab**. No device outputs are fabricated or stored here.

## Scope and safety

- Executes only `show ip interface brief` and `show ip route` on lab Cisco IOS devices
- Inventory contains RFC1918 lab addresses, not customer IPs
- No password, credential or API token is committed
- Prints output locally; review and sanitize all command output before publishing
- Supports `--dry-run` to list planned checks without connecting

## Usage

    python3 -m venv .venv
    . .venv/bin/activate
    python -m pip install -r requirements.txt
    python collect_ios_status.py --inventory devices.example.json --dry-run

For **lab-only** live execution, supply `CISCO_USER` and `CISCO_PASSWORD` in your environment and run without `--dry-run`. Do not enter credentials into tracked files.

The old Cisco IOL images in this lab have offered deprecated SSH key-exchange algorithms. Their interoperability can require separate **isolated lab-only** SSH configuration; this example does not weaken global SSH defaults or claim to solve that issue.

## Validation status

- Syntax review / local dry-run: can be verified without devices
- Network connection and actual outputs: **not yet captured for this example**
- Next: run against isolated EVE-NG devices, redact the output, and document successes/failures with timestamps

Do not mistake the example for a production automation solution.
