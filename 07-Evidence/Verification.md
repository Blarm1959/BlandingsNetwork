# Verification and recovery backlog

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## 7. Verification and recovery backlog

All items below are OPEN. Record observation date, source, actual values and user confirmation when closing an item. Old chats can supply context, but exact current equipment settings need current evidence.

| ID | Priority | Area | Evidence needed / completion condition |
|---|---|---|---|
| V1 | First | Router DNS | Exact firmware build; DNS Director enable/mode/custom resolver/client list, WAN DNS and LAN DHCP DNS. Resolve the contradictions in ../01-Architecture/DNS.md. |
| V2 | First | Guest network | Current subnet/gateway/pool, exact DNS addresses, SSID and access policy. Record user-confirmed guest resolution independent of Pi-hole and intended LAN access. |
| V3 | First | Automation | Verbatim three scripts and `common_vars` with secrets excluded; `cru l`, hook inventory, state/log locations. Identify actual failover key and prerequisites. |
| V4 | First | DNS operation | Current Pi-hole/Unbound versions/configuration; host/container resolvers; user-confirmed normal resolution, fallback and recovery evidence. Any outage test requires a separately agreed test window. |
| V5 | Next | WAN/router | WAN connection type and relevant settings, DDNS/certificates, IPv6, Dual-WAN state, firewall/port-forward rules, current Wi-Fi settings. |
| V6 | Next | WireGuard | Server fields and non-secret peer inventory, AllowedIPs, DNS, endpoint and firewall routes. Record user-confirmed remote split-tunnel LAN access. |
| V7 | Next | Inventory | Static/reserved assignment method, MAC/hostname records, switch/NeoHub address check, switch configuration, port/cable/PoE map, NAS model/services. |
| V8 | Next | Proxmox/LXC | PVE version, storage/bridges, Pi-hole VMID and LXC configuration, startup order, gateway/DNS, other LXCs and required services. |
| V9 | Recovery | Backups | Router configuration/JFFS, Pi-hole export plus Unbound config, Proxmox/LXC, switch and NAS configuration: backup locations, dates, coverage and restore prerequisites. |
| V10 | Recovery | Restore validation | A user-approved restore procedure with dependency order, access prerequisites, rollback and evidence of a successful restore. No restore test has been completed in this review. |
| V11 | History | Missing decisions | Exact VLAN failure evidence/builds, guest-interception rejection reason, IPv6-removal reason and February 2026 migration evidence. Preserve uncertainty if originals cannot be recovered. |
| V12 | Inventory | Laptops/NAS/backups | Actual computer/NAS names and addresses, Synology Drive tasks, Restic scripts/repositories/snapshots and restore evidence; resolve speculative INV-NAS-012 mapping. |
| V13 | Recovery | Heating automation | Actual hub model/build/address, openHAB versus Home Assistant roles, Legacy API state, custom binding source/JAR and tested heatmiser_summary rule. Confirm any G3/neoFlo change separately. |
| V14 | Recovery | Media services | Current LXC IDs/addresses, services/versions, exporter files, real schedules/timezone, shared mount mapping/permissions and the outcome of Emby scan/installer experiments. |
| V15 | History | Complete chat audit | Obtain older conversation turns and original attachments, search unlisted active chats and recover switch diagrams/device inventories. Close only when coverage is explicit and reviewed. |
| V16 | Inventory | Keyword gaps | Recover Netgear, Raspberry Pi/RPi, Flightradar/FR24 and ADS-B history from unreturned older chats/attachments; record actual devices, addresses and active/retired state only with evidence. |
| V17 | Inventory | CarFinder LXC | Verify current host/location/CTID/address, service and routes; reconcile candidate 10.83.59.181:8501 with confirmed 10.59 LAN and verify Laptop 1 name. |
| V18 | Inventory | WDL-Flight-01 | Recover original chat/attachments and verify actual hostname, role, hardware, address/MAC, services, location, connectivity and active/retired status; search remains incomplete. |
| V19 | Recovery | GarageSwitch | Recover original diagram PDFs and earlier chat turns; verify current switch identity/hostname, management address, port labels, uplink and PoE consumers. Preserve the requested printable label layout. |

Suggested first evidence batch: current DNS Director, WAN DNS, LAN DHCP and Guest Network Pro pages, followed by the current script files and `cru l`. Capture existing state before considering edits. Keep credentials, VPN private keys and tokens outside this record; document where the user can retrieve them privately.

### Backup/restore record template

For each component record: backup method; contents covered; private storage location; date/version; integrity check; required hardware/software/access; restore steps; dependency order; rollback; test date/result and user confirmation. Until V9/V10 are completed, this file is **not a complete disaster-recovery reference**.
## Recovery progress on 5 October 2026 — items stay open

S27 recovers historical router script source (V3), MAC/name/reservation data (V7/V12), named backup sets (V9), Netgear and flight-RPi/FR24 leads (V16/V18), and general garage/loft topology (V19). None is a current live observation or verified restore. V18 now has candidate WDL-RPI3-FLIGHT-01 plus duplicate-MAC conflict. The original numbered-port PDF is still awaited. V16 no longer means no repository evidence for Netgear/RaspberryPi/FR24; its earlier statement describes chat-only coverage.

| ID | Priority | Area | Evidence needed |
|---|---|---|---|
| V20 | First | HomeNetwork contradictions | Current10.59 versus10.83/10.0 generations;140 versus210/230 grouping; DNS Global Router versusCustom1; actual script versions, Pi-hole MAC exception and effective policy. |
| V21 | Next | Inventory reconciliation | Current device list/MACs, duplicate flight/Pi-hole labels, unnamed .100, actual LXC CTIDs, firmware/hardware identities and switch/cable maps. |
