# Read-only Cisco CLI collector

This Python example runs two commands per inventory entry: `show ip interface brief` and `show ip route`. It prints each device’s output locally and continues to the next device after a connection or read timeout. The [recorded R1 session](../python-netmiko-network-verification.md) used an earlier script.

## Preview the inventory

From this directory, run the following command with Python 3. Dry-run mode reads the JSON inventory and prints the planned commands without opening an SSH connection or importing Netmiko.

```sh
python3 collect_ios_status.py --inventory devices.example.json --dry-run
```

Each device needs a name and host. The example inventory contains R1, R2 and SW1. The supported device type is `cisco_ios`.

## Collect live output in the lab

1. Create a virtual environment and install the dependencies.
2. Verify each device’s SSH host-key fingerprint through the lab console or another trusted channel. Enroll the verified key in the current user’s SSH known_hosts file under the inventory hostname or IP. The collector checks these keys when connecting.
3. Set `CISCO_USER` and `CISCO_PASSWORD` in the shell environment using your local credential workflow.
4. Run the collector from this directory. Review the terminal output before sharing it.

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python collect_ios_status.py --inventory devices.example.json
```

| Exit code | Meaning |
| --- | --- |
| 0 | Dry-run completed or all live collections succeeded. |
| 1 | At least one device failed during connection or collection. |
| 2 | Setup or input error, such as an invalid inventory or missing credentials. |

## Validation

Local checks covered Python compilation, a dry-run for all three inventory entries, invalid inventory and missing credentials. With Netmiko 4.8.0 and Paramiko 5.1.0 installed, simulated sessions also verified command order, strict host-key settings and continued collection after a per-device SSH error or read timeout. Live SSH, current IOS interoperability and output from this implementation still require a run in EVE-NG.
