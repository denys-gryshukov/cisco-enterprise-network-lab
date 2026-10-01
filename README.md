# Cisco Enterprise Network Lab

Enterprise network lab built in EVE-NG using Cisco IOL routers and switches.

The project demonstrates Layer 2 and Layer 3 redundancy, dynamic routing, IPv4/IPv6 dual-stack connectivity, network security, and troubleshooting.


## Network Topology

![Cisco Enterprise Network Topology](topology/topology.png)


## VLAN Design

| VLAN | Name | Purpose | IPv4 Subnet | IPv6 Prefix |
|---|---|---|---|---|
| 10 | USERS | User workstations | 192.168.10.0/24 | 2001:db8:10::/64 |
| 20 | ADMIN | Administrative devices | 192.168.20.0/24 | 2001:db8:20::/64 |
| 30 | SERVERS | Server segment | 192.168.30.0/24 | 2001:db8:30::/64 |
| 99 | MANAGEMENT | Network management | 192.168.99.0/24 | 2001:db8:99::/64 |

## IP Addressing Plan

### Routed Links

| Link | Device | Interface | IPv4 Address | IPv6 Address |
|---|---|---|---|---|
| ISP-R1 | ISP | Gi0/0 | 203.0.113.1/30 | - |
| ISP-R1 | R1 | Gi0/0 | 203.0.113.2/30 | - |
| R1-R2 | R1 | Gi0/1 | 10.0.12.1/30 | 2001:db8:12::1/64 |
| R1-R2 | R2 | Gi0/0 | 10.0.12.2/30 | 2001:db8:12::2/64 |
| R1-R3 | R1 | Gi0/2 | 10.0.13.1/30 | 2001:db8:13::1/64 |
| R1-R3 | R3 | Gi0/0 | 10.0.13.2/30 | 2001:db8:13::2/64 |

### HSRP Gateways

| VLAN | Virtual Gateway | R2 Address | R3 Address | Preferred Active Router |
|---|---|---|---|---|
| 10 | 192.168.10.1 | 192.168.10.2 | 192.168.10.3 | R2 |
| 20 | 192.168.20.1 | 192.168.20.2 | 192.168.20.3 | R2 |
| 30 | 192.168.30.1 | 192.168.30.2 | 192.168.30.3 | R3 |
| 99 | 192.168.99.1 | 192.168.99.2 | 192.168.99.3 | R3 |

## Endpoint Assignment

| Host | VLAN | IPv4 Addressing | Default Gateway |
|---|---|---|---|
| PC1 | 10 | DHCP | 192.168.10.1 |
| PC2 | 20 | DHCP | 192.168.20.1 |
| PC3 | 10 | DHCP | 192.168.10.1 |
| PC4 | 30 | DHCP | 192.168.30.1 |


## Technologies

- VLANs
- 802.1Q Trunking
- LACP EtherChannel
- Rapid-PVST+
- Router-on-a-Stick
- HSRP
- OSPFv2
- OSPFv3
- IPv4 / IPv6 Dual Stack
- DHCP
- NAT/PAT
- Extended ACLs
- Port Security
- DHCP Snooping
- ECMP
- Passive OSPF Interfaces

## Platform

- EVE-NG
- Cisco IOL
- Cisco IOL L2
- VPCS

## Project Status

Lab implementation completed.

Documentation and verification outputs are being added.


