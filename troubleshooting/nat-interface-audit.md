# R1 NAT interface-role audit

**Status: unresolved — no R1 running configuration or corrected test output has been committed.**

## Evidence

The [network topology](../topology/topology.png) shows R1 connected to the simulated ISP on `Gi0/0`, R2 on `Gi0/1`, and R3 on `Gi0/2`.

However, [verification/nat.txt](../verification/nat.txt) records:

```text
Outside interfaces:
  GigabitEthernet0/0, GigabitEthernet0/2
Inside interfaces:
  GigabitEthernet0/1
```

It also shows ICMP translations from `192.168.10.21` to `203.0.113.2` for the simulated `8.8.8.8` destination. This demonstrates that *some* NAT processing occurred, but **does not prove both paths through R2 and R3 work correctly**.

## Working hypothesis

If R1 uses conventional inside/outside NAT as the README describes, `Gi0/2` (towards internal R3) should be Inside, not Outside. The saved result may represent a misconfiguration or an earlier lab state. Without the running configuration, we cannot establish which.

## Check and resolve in EVE-NG

1. On R1 inspect `show running-config`, `show ip nat statistics`, `show ip nat translations`, and `show ip route`.
2. Confirm the intended NAT roles: `Gi0/0` Outside; `Gi0/1` and `Gi0/2` Inside.
3. **Only if the live configuration and lab topology confirm this discrepancy**, update R1's `Gi0/2` role:

   ```cisco
   configure terminal
   interface GigabitEthernet0/2
    no ip nat outside
    ip nat inside
   end
   ```

4. Repeat tests from internal hosts to the simulated external destination, including tests with traffic routed via R2 and via R3. Check return traffic.
5. Save fresh NAT statistics/translations and host ping results with the test conditions and a date.
6. Update the README and close this audit **only once tests pass**.

Do not apply the suggested command to unrelated or production equipment.

## Resolution

**Pending validation on the running EVE-NG devices.**
