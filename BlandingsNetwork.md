# BlandingsNetwork

**Master record for the Blandings home network.** Read this overview before making recommendations, then follow the relevant section. Documentation review: 7 October 2026; released baseline v2.0.4. This is a documentation Change Package for the next v3.0.1 release, not a network change.

> This file records tested decisions as well as the current configuration. Do not replace a confirmed design with a theoretically preferable alternative unless new evidence or changed hardware/software justifies reopening the decision.

The user's confirmed baseline takes precedence over old repository/chat claims. Only promote changes after the user confirms they work. No main-LAN VLANs; do not reopen that rejected design without an explicit request or material firmware/hardware change addressing the limitation. This working chat supports the review; the released repository carries the durable record so important context does not depend on keeping old chats.

## Confirmed current overview

### Internet and infrastructure

| Component / setting | Confirmed value | Source |
|---|---|---|
| ISP | EE Full Fibre 900 | S1 |
| Router | ASUS RT-AX86U Pro | S1 |
| Firmware family | Asuswrt-Merlin 3006 line; exact installed build UNKNOWN | S1 |
| Switch | TP-Link TL-SG1218MPE PoE | S1 |
| Virtualisation | Proxmox PVE host with LXCs | S1 |
| Storage | Synology NAS; exact model UNKNOWN | S1 |
| Heating hub | Heatmiser NeoHub; exact current model/version UNKNOWN | S1 |
| Main LAN | `10.59.0.0/16` | S1 |
| Router LAN address | `10.59.0.1` | S1 |
| DHCP pool | `10.59.250.201`–`10.59.250.250` | S1 |
| Main LAN design | Flat LAN; **NO VLANs** | S1 |

The flat main LAN is a tested decision. Logical address groups are administrative labels within one `/16`; they do not establish separate subnets or security isolation. The deliberate Guest Network Pro service below does not reopen the rejected main-LAN VLAN design. Historical physical topology is documented in the hardware section; current cabling and numbered port assignments remain unverified.

### Address plan and known devices

| Purpose / device | Range / address | Status / source |
|---|---|---|
| Infrastructure | `10.59.60.x` | CONFIRMED, S1 |
| Trusted devices | `10.59.120.x` | CONFIRMED, S1 |
| IoT | `10.59.140.x` | CONFIRMED, S1 |
| Pi-hole + Unbound LXC | `10.59.20.102` | CONFIRMED, S1 |
| Synology NAS | `10.59.40.131` | CONFIRMED, S1 |
| Proxmox host | `10.59.60.99` | CONFIRMED, S1 |
| TP-Link switch | `10.59.60.136` | RELEASED RECORD; recheck address and assignment method |
| Heatmiser NeoHub | `10.59.60.172` | RELEASED RECORD; recheck address and assignment method |

Historical MAC/name/reservation records have been recovered from HomeNetwork; current assignments, lease duration and a reconciled live inventory remain unverified.

### Guest Network Pro

- CONFIRMED subnet: `10.52.0.0/24`.
- CONFIRMED design: guests must **not** depend on Pi-hole; guest DNS uses Quad9.
- UNKNOWN: exact Quad9 addresses entered in the guest GUI, guest gateway, DHCP pool, SSID, access-to-intranet setting and effective firewall behaviour.

Do not infer guest isolation rules solely from the separate subnet. Confirm the intended access policy and observed behaviour when recording exact settings.

### DNS baseline

- CONFIRMED: Pi-hole + local Unbound in an LXC at `10.59.20.102`.
- CONFIRMED fallback resolver: `9.9.9.11`.
- UNKNOWN: which router fields implement this fallback, exact forwarding path, Unbound listen address/port, software versions and current failover logic.

The existence of a fallback address does not establish how or when it is selected. DHCP DNS, WAN DNS, DNS Director and guest DNS must be recorded separately.

### WireGuard

- CONFIRMED router tunnel address: `10.6.0.1/24`; UDP **443**; split tunnel.
- Derived network: `10.6.0.0/24`.
- RELEASED RECORD: intended main-LAN route `10.59.0.0/16` and basic connectivity should avoid an unnecessary Pi-hole dependency.
- UNKNOWN: live peer addresses, AllowedIPs, endpoint hostname, peer DNS, keepalive, routes and firewall access.

## Detailed record

| Section | Pages and purpose |
|---|---|
| Architecture | [Addressing](01-Architecture/Addressing.md), [device inventory](01-Architecture/DeviceInventory.md), [DNS](01-Architecture/DNS.md), [guest/VPN](01-Architecture/GuestAndVPN.md), [firewall history](01-Architecture/Firewall.md), [Merlin scripts](01-Architecture/RouterScripts.md). |
| Hardware | [Physical topology/cabling](02-Hardware/Topology.md), [GarageSwitch/port map](02-Hardware/GarageSwitch.md), [loft Netgear switch](02-Hardware/LoftSwitch.md), [ASUS router](02-Hardware/Router.md). |
| Services | [Proxmox/LXCs](03-Services/Proxmox.md), [Pi-hole/Unbound](03-Services/PiHoleUnbound.md), [flight RaspberryPi/FR24](03-Services/FlightReceiver.md), [NAS/clients](03-Services/NASAndClients.md), [heating](03-Services/Heating.md), [media](03-Services/Media.md), [CarFinder](03-Services/CarFinder.md). |
| Rebuild | [Prerequisites and procedure outline](04-Rebuild-Guide/Rebuild.md); not yet a tested rebuild guide. |
| Disaster recovery | [Backup evidence](05-Disaster-Recovery/Backups.md), [incident evidence/outlines](05-Disaster-Recovery/Incidents.md). |
| History | [Rejected/superseded decisions](06-History/Decisions.md), [other implementation history](06-History/OtherRecovery.md). |
| Evidence/control | [Status and sources](07-Evidence/Sources.md), [verification backlog](07-Evidence/Verification.md), [change control/future-chat starter](07-Evidence/ChangeControl.md), [7 October chat recovery](07-Evidence/ChatRecovery-2026-10-07.md). |

## What still needs confirmation

Historical material mixes `192.168.1`, `10.0`, `10.83` and the current `10.59` generation, plus conflicting DNS Director designs. Historical addresses and LXC details recovered from old chats must not be silently promoted to the current network.

Current GUI and live-script evidence remain the first priority: exact Merlin firmware, WAN DNS, LAN DHCP DNS, DNS Director, Guest Network Pro, installed Pi-hole failover scripts/cron, and current Pi-hole/Unbound operation.

Use CONFIRMED only for user-confirmed current facts. RELEASED RECORD is retained older documentation; HISTORICAL/VERIFY covers repository snapshots and recovered claims; UNKNOWN stays unknown. Plans, proposed scripts and old assistant claims are not successful tests.

## Package/release workflow

This project uses PSTP. Change Packages contain changed files only; PSTP owns release.json, build-info.json, commits, tags and pushes.

```powershell
cd C:\WDL\GitHub\BlandingsNetwork
.\PSTP.ps1 Release -Zip
```

## Documentation release lineage

v1.0.1 established the baseline; later v1 releases expanded evidence, recovery and diagrams. v2.0.1 was the requested dummy/version-only release. v2.0.2 and v2.0.3 added the Home LAN Revisit and archived-chat recovery work. **v2.0.4 is confirmed released** and contains the five recovered legacy Merlin task excerpts. The next requested Change Package/release is **v3.0.1**.

## Recovered GarageSwitch connections

The user's original message preserves all 18 numbered ports: 14 named destinations and four unspecified. See the complete port table in `02-Hardware/GarageSwitch.md` and the reproducible diagram sources. Current wiring and blank-port use remain verification items.

## 7 October 2026 chat-list recovery

[ChatRecovery-2026-10-07.md](07-Evidence/ChatRecovery-2026-10-07.md) records the additional network-related chats visible in the user's current and archived chat lists and the extra historical facts recovered from account conversation context.

Important additions include historical Proxmox/NAS mount evidence, older `10.83` media-service details, Emby library/playback evidence, Syncrify-to-NAS paths, and stronger dated NeoHub Gen 2 evidence. These are **historical evidence only** unless separately confirmed against the current `10.59` network.

The review also records which visible chats are already represented in the repository and which titles still need a complete read before deletion. A title being visible, a summary being recovered, or a few turns being available is not sufficient by itself to declare a chat safe to delete.
