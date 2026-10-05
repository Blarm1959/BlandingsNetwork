# BlandingsNetwork

**Master record for the Blandings home network.** Read this overview before making recommendations, then follow the relevant section. Documentation review: 5 October 2026; released baseline v1.0.7. This is an unreleased documentation Change Package, not a network change.

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
| Heating hub | Heatmiser NeoHub; exact model/version UNKNOWN | S1 |
| Main LAN | `10.59.0.0/16` | S1 |
| Router LAN address | `10.59.0.1` | S1 |
| DHCP pool | `10.59.250.201`–`10.59.250.250` | S1 |
| Main LAN design | Flat LAN; **NO VLANs** | S1 |

The flat main LAN is a tested decision. Logical address groups are administrative labels within one `/16`; they do not establish separate subnets or security isolation. The deliberate Guest Network Pro service below does not reopen the rejected main-LAN VLAN design. Historical physical topology is now documented in the hardware section; current cabling and numbered port assignments remain unverified.

### Address plan and known devices

| Purpose / device | Range / address | Status / source |
|---|---|---|
| Infrastructure | `10.59.60.x` | CONFIRMED, S1 |
| Trusted devices | `10.59.120.x` | CONFIRMED, S1 |
| IoT | `10.59.140.x` | CONFIRMED, S1 |
| Pi-hole + Unbound LXC | `10.59.20.102` | CONFIRMED, S1 |
| Synology NAS | `10.59.40.131` | CONFIRMED, S1 |
| Proxmox host | `10.59.60.99` | CONFIRMED, S1 |
| TP-Link switch | `10.59.60.136` | RELEASED RECORD, S2; recheck address and assignment method |
| Heatmiser NeoHub | `10.59.60.172` | RELEASED RECORD, S2; recheck address and assignment method |

Historical MAC/name/reservation records have now been recovered from HomeNetwork (S27); current assignments, lease duration and a reconciled live inventory remain unverified. S2 also lists a Samsung S23 among trusted devices; its address and current VPN role need verification.

### Guest Network Pro

- CONFIRMED subnet: `10.52.0.0/24` (S1).
- CONFIRMED design: guests must **not** depend on Pi-hole; guest DNS uses Quad9 (S1).
- UNKNOWN: exact Quad9 addresses entered in the guest GUI, guest gateway, DHCP pool, SSID, access-to-intranet setting and effective firewall behaviour.

Do not infer guest isolation rules solely from the separate subnet. Confirm the intended access policy and observed behaviour when recording exact settings.

### DNS baseline

- CONFIRMED: Pi-hole + local Unbound in an LXC at `10.59.20.102` (S1).
- CONFIRMED fallback resolver: `9.9.9.11` (S1).
- UNKNOWN: which router fields implement this fallback, exact forwarding path, Unbound listen address/port, software versions and current failover logic.

The existence of a fallback address does not establish how or when it is selected. DHCP DNS, WAN DNS, DNS Director and guest DNS must be recorded separately.

### WireGuard

- CONFIRMED router tunnel address: `10.6.0.1/24`; UDP **443**; split tunnel (S1).
- Derived network: `10.6.0.0/24`.
- RELEASED RECORD: intended main-LAN route `10.59.0.0/16` and basic connectivity should avoid an unnecessary Pi-hole dependency (S2).
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
| Evidence/control | [Status and sources](07-Evidence/Sources.md), [verification backlog](07-Evidence/Verification.md), [change control/future-chat starter](07-Evidence/ChangeControl.md), [HomeNetwork review](07-Evidence/HomeNetworkReview.md), [historical Pi-hole source](07-Evidence/RecoveredPiHoleSource.md), [frozen v1.0.5 master](07-Evidence/ReleasedRecord-v1.0.5.md). |
| Chat coverage | [Audit ledger](docs/ChatAudit.md), [keyword/name search](docs/KeywordAudit.md). Older turns, unlisted chats and attachments remain gaps. |

## What still needs confirmation

HomeNetwork adds useful historical evidence, not a replacement baseline. It mixes10.0,10.59 and10.83 generations,140 versus210/230 IoT addressing, conflicting DNS Director modes, proposed firewall policy and incomplete script/rebuild inputs. Current GUI and live script evidence remain the first priority. The flight device's fuller name and duplicate MAC need checking; the original GarageSwitch port map has now been recovered from user text (S28), with a reconstructed diagram; current wiring remains to be checked. All verification items remain open.

Use CONFIRMED only for user-confirmed current facts. RELEASED RECORD is retained older documentation; HISTORICAL/VERIFY covers repository snapshots and recovered claims; UNKNOWN stays unknown. Plans, proposed scripts, empty pages and policy statements are not successful tests. No audited networking chat or the old HomeNetwork repository is cleared for deletion.

## Package/release workflow

This project uses PSTP. Change Packages contain changed files only; PSTP owns release.json, build-info.json, commits, tags and pushes. The README change in this package updates navigation, not release metadata.

```powershell
cd C:\WDL\GitHub\BlandingsNetwork
.\PSTP.ps1 Release -Zip
```

## Documentation release lineage

v1.0.1 established the baseline; v1.0.2 added evidence/contradictions; v1.0.3 broadened chat recovery; v1.0.4 added keyword/CarFinder leads; v1.0.5 added device-name/diagram recovery. v1.0.6 organised the overview and section files and recovered HomeNetwork evidence. v1.0.7 added the recovered GarageSwitch port table and diagram. Local release metadata confirms v1.0.7. This pending change stores diagram sources/builders and section-coverage evidence; it does not declare v1.0.8 released.


## Recovered GarageSwitch connections (S28)

The user's original message now preserves all 18 numbered ports: 14 named destinations and four unspecified. See the [complete port table](02-Hardware/GarageSwitch.md#recovered-original-port-map-s28) and [printable diagram](diagrams/GarageSwitch.pdf). The odd/even layout is retained. Current wiring and blank-port use remain verification items.


## Reusable diagram sources and section coverage

[Diagram source and regeneration](diagrams/README.md) stores structured facts, renderer and instructions for the garage-switch and physical-topology PDFs, SVGs and marked Markdown blocks. Diagrams can now be regenerated without old chats. [Section coverage](07-Evidence/SectionCoverage.md) maps all 18 empty HomeNetwork Markdown placeholders to populated BlandingsNetwork pages. BlandingsNetwork has no zero-length Markdown pages; current verification and tested-recovery gaps remain explicit.
