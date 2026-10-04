# Guest Network Pro and WireGuard

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### Guest Network Pro

- CONFIRMED subnet: `10.52.0.0/24` (S1).
- CONFIRMED design: guests must **not** depend on Pi-hole; guest DNS uses Quad9 (S1).
- UNKNOWN: exact Quad9 addresses entered in the guest GUI, guest gateway, DHCP pool, SSID, access-to-intranet setting and effective firewall behaviour.

Do not infer guest isolation rules solely from the separate subnet. Confirm the intended access policy and observed behaviour when recording exact settings.

### WireGuard

- CONFIRMED router tunnel address: `10.6.0.1/24`; UDP **443**; split tunnel (S1).
- Derived network: `10.6.0.0/24`.
- RELEASED RECORD: intended main-LAN route `10.59.0.0/16` and basic connectivity should avoid an unnecessary Pi-hole dependency (S2).
- UNKNOWN: live peer addresses, AllowedIPs, endpoint hostname, peer DNS, keepalive, routes and firewall access.
## Historical HomeNetwork leads (S27)

Main SSID `ASUS-BT` and guest `ASUS-BT-G2`, one Guest Network Pro network, guest gateway `10.52.0.1`, intended guest isolation/no main-LAN access. These are repository records to verify; exact live settings remain unknown. Overview claims WireGuard rebuilt on UDP 443 and working internet at 900+ Mbps; these are historical claims without recovered test logs. A name-only `pve-01_LXC_Wireguard` does not establish the current WireGuard endpoint location.
