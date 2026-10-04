# Addressing and DHCP inventory

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Confirmed address plan

Main LAN `10.59.0.0/16`, mask `255.255.0.0`, router `10.59.0.1`, DHCP pool `10.59.250.201–10.59.250.250`. Infrastructure uses `10.59.60.x`, trusted devices `10.59.120.x`, IoT `10.59.140.x`. Pi-hole is `10.59.20.102`, NAS `10.59.40.131`, Proxmox `10.59.60.99` (S1). Logical groups do not create separate networks or demonstrate isolation.

## Historical repository addressing — verify before promotion

S27 documents preserving the fourth octet from the older `192.168.1.X` identities. It lists IOTM `10.59.210.x`, cloud IoT `10.59.230.x` and unknown/DHCP `10.59.250.x`; these conflict with or extend the current brief's IoT `10.59.140.x`. Do not move devices or adopt that policy without confirmation. The root README instead claims a flat `10.0.0.0/8`, while copied common variables use `10.83.0.0/16`; those are historical generations.

S27 says reservations are held in router NVRAM `dhcp_staticlist`, with friendly names in `custom_clientlist`, exported by `router_nvram_show.sh`. A separate legacy `dhcp_res` plus setup script uses dnsmasq additions. Do not merge both approaches into a new live configuration.

The complete recovered list is in [DeviceInventory.md](DeviceInventory.md), including reservation, lease-only and name-only rows. Historical status codes are not current online/offline assertions. MAC-to-IP assignment method still requires live comparison. Guest-network addressing remains separately documented in [GuestAndVPN.md](GuestAndVPN.md).
