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



## Network Design

### Layer 2 Design

SW1 and SW2 are connected using an LACP EtherChannel consisting of two physical links.

The Port-Channel operates as an 802.1Q trunk and carries VLANs 10, 20, 30, and 99.

Rapid-PVST+ is used for Layer 2 loop prevention and convergence.

To optimize traffic paths:

- SW1 is the STP root bridge for VLANs 10 and 20
- SW2 is the STP root bridge for VLANs 30 and 99

This design aligns the Layer 2 forwarding path with the preferred HSRP gateway for each VLAN.

### First-Hop Redundancy

HSRP provides redundant default gateways for all user VLANs.

- R2 is the preferred Active router for VLANs 10 and 20
- R3 is the preferred Active router for VLANs 30 and 99

Each VLAN uses `.1` as the HSRP virtual IPv4 gateway.

HSRP preemption is enabled so that the preferred router resumes the Active role after recovery.

### Layer 3 Routing

R1, R2, and R3 participate in OSPF Area 0.

The routed point-to-point links are:

- R1-R2: 10.0.12.0/30
- R1-R3: 10.0.13.0/30

R2 and R3 advertise the internal VLAN networks into OSPF.

User-facing VLAN interfaces are configured as passive OSPF interfaces. This allows the networks to be advertised without forming unnecessary OSPF adjacencies on access VLANs.

R1 learns the internal networks through both R2 and R3 and can install equal-cost routes when both paths are available.

### Internet Edge

R1 acts as the enterprise edge router.

It provides:

- Static default routing toward the simulated ISP
- NAT/PAT for internal IPv4 networks
- OSPF default-route advertisement toward R2 and R3

The ISP router uses a Loopback interface with address `8.8.8.8/32` to simulate an external Internet destination.

### IPv6 Design

The network operates in dual-stack mode.

IPv6 routing uses OSPFv3 over the same routed topology.

IPv6 prefixes are assigned per VLAN using the documentation prefix `2001:db8::/32`.

As with OSPFv2, user-facing interfaces are configured as passive OSPFv3 interfaces to prevent unnecessary neighbor formation.



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


