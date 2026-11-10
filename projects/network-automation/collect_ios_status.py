#!/usr/bin/env python3
"""Read-only Cisco IOS interface audit for an isolated lab.

New portfolio example. Live device execution must be validated separately
against the author's EVE-NG topology.
"""
import argparse
import json
import os
import sys
from pathlib import Path

DEFAULT_COMMANDS = ["show ip interface brief", "show ip route"]


def load_devices(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("Inventory must be a non-empty JSON list.")
    for item in data:
        if not isinstance(item, dict) or not item.get("name") or not item.get("host"):
            raise ValueError("Every inventory entry needs name and host.")
        if item.get("device_type", "cisco_ios") != "cisco_ios":
            raise ValueError("This example only supports cisco_ios.")
    return data


def main():
    parser = argparse.ArgumentParser(description="Read-only CLI checks via Netmiko")
    parser.add_argument("--inventory", default="devices.example.json")
    parser.add_argument("--dry-run", action="store_true",
                        help="List intended commands without connecting")
    args = parser.parse_args()
    try:
        devices = load_devices(args.inventory)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"Invalid inventory: {exc}", file=sys.stderr)
        return 2

    if args.dry_run:
        for device in devices:
            print(f"{device['name']} ({device['host']}): {', '.join(DEFAULT_COMMANDS)}")
        return 0

    username = os.getenv("CISCO_USER")
    password = os.getenv("CISCO_PASSWORD")
    if not username or not password:
        print("Set CISCO_USER and CISCO_PASSWORD environment variables.", file=sys.stderr)
        return 2

    try:
        from netmiko import ConnectHandler
        from netmiko.exceptions import (
            NetmikoAuthenticationException,
            NetmikoTimeoutException,
        )
    except ImportError:
        print("Install dependencies: python -m pip install -r requirements.txt",
              file=sys.stderr)
        return 2

    failures = 0
    for device in devices:
        name, host = device["name"], device["host"]
        print(f"\n=== {name} / {host} ===")
        try:
            with ConnectHandler(
                device_type="cisco_ios",
                host=host,
                username=username,
                password=password,
                conn_timeout=8,
                auth_timeout=10,
            ) as conn:
                for command in DEFAULT_COMMANDS:
                    print(f"\n$ {command}")
                    print(conn.send_command(command, read_timeout=20))
        except (NetmikoAuthenticationException, NetmikoTimeoutException, OSError) as exc:
            failures += 1
            print(f"{name}: connection/collection failed: {type(exc).__name__}",
                  file=sys.stderr)
            # Do not dump exception details: they can expose environment specifics.
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
