# Section coverage and empty-file audit

[Master overview](../BlandingsNetwork.md) · [HomeNetwork review](HomeNetworkReview.md)

Audit date: 5 October 2026. Local BlandingsNetwork v1.0.7 contains **no zero-length Markdown files**. The older HomeNetwork checkout contains **18 zero-length Markdown pages** and **three empty Mermaid files**. Those are source-repository placeholders; they were not copied as blank pages into the new master record.

The important topics have been populated in BlandingsNetwork using confirmed facts, recovered historical evidence and explicit unknowns. A populated page does not mean its procedure is tested or its current configuration complete.

| Empty HomeNetwork page | Populated BlandingsNetwork coverage |
|---|---|
| 02-Hardware/cabling-layout.md | [Topology](../02-Hardware/Topology.md), [GarageSwitch](../02-Hardware/GarageSwitch.md) |
| 02-Hardware/garage-switch-tl-sg1218mpe.md | [GarageSwitch](../02-Hardware/GarageSwitch.md), recovered 18-port map |
| 02-Hardware/loft-switch-gs308e.md | [LoftSwitch](../02-Hardware/LoftSwitch.md); downstream port numbers remain unknown |
| 02-Hardware/router-rt-ax86u-pro.md | [Router](../02-Hardware/Router.md), architecture pages |
| 03-Services/heatmiser-neohub.md | [Heating](../03-Services/Heating.md) |
| 03-Services/media-storage.md | [Media](../03-Services/Media.md), [NAS and clients](../03-Services/NASAndClients.md) |
| 03-Services/pihole-unbound.md | [PiHoleUnbound](../03-Services/PiHoleUnbound.md), [DNS](../01-Architecture/DNS.md), [RouterScripts](../01-Architecture/RouterScripts.md) |
| 03-Services/proxmox.md | [Proxmox](../03-Services/Proxmox.md), recovered [device inventory](../01-Architecture/DeviceInventory.md) |
| 04-Rebuild-Guide/01-factory-reset-router.md | [Rebuild](../04-Rebuild-Guide/Rebuild.md): prerequisites only, no tested reset sequence |
| 04-Rebuild-Guide/02-configure-lan-and-dhcp.md | [Addressing](../01-Architecture/Addressing.md), [Rebuild](../04-Rebuild-Guide/Rebuild.md) |
| 04-Rebuild-Guide/03-configure-dnsmasq-reservations.md | [Addressing](../01-Architecture/Addressing.md), [RouterScripts](../01-Architecture/RouterScripts.md); legacy apply script is incompatible |
| 04-Rebuild-Guide/04-configure-firewall-policy.md | [Firewall](../01-Architecture/Firewall.md): historical intent, no verified deployment |
| 04-Rebuild-Guide/05-verify-and-test.md | [Verification backlog](Verification.md), [Rebuild](../04-Rebuild-Guide/Rebuild.md) |
| 05-Disaster-Recovery/dr-dns-issues.md | [Incidents](../05-Disaster-Recovery/Incidents.md), DNS evidence requirements |
| 05-Disaster-Recovery/dr-internet-down.md | [Incidents](../05-Disaster-Recovery/Incidents.md), WAN/link versus DNS evidence |
| 05-Disaster-Recovery/dr-locked-out.md | [Incidents](../05-Disaster-Recovery/Incidents.md), local access and agreed recovery prerequisites |
| 05-Disaster-Recovery/dr-pihole-down.md | [Incidents](../05-Disaster-Recovery/Incidents.md), [RouterScripts](../01-Architecture/RouterScripts.md) |
| 05-Disaster-Recovery/dr-router-failure.md | [Incidents](../05-Disaster-Recovery/Incidents.md), [Backups](../05-Disaster-Recovery/Backups.md) |

The empty physical-topology Mermaid file now has a populated historical topology counterpart with source JSON, Mermaid, PDF and SVG in BlandingsNetwork. The empty logical-topology and policy-flow files have no established current diagram to migrate; architecture/DNS/firewall pages preserve the known design and conflicts. See [diagram registry](../diagrams/README.md).

Keep improving these populated pages as new evidence arrives. Priorities are exact router DNS settings, actual script copies/cron, current LXC and NAS configuration, remaining switch ports/cable labels and tested backup/restore steps. Do not fill a blank in the record with a guessed procedure or promote historical instructions to tested recovery. The [verification backlog](Verification.md) remains the completion checklist.

This update does not modify HomeNetwork. BlandingsNetwork is the continuing master record; copying new content back into the older conflicting repository would create two competing authorities.
