# Physical topology and cabling

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Historical topology recovered from HomeNetwork (S27)

Repository overview: EE → ASUS router → TP-Link TL-SG1218MPE in garage cabinet. Cat6 room runs return to the garage switch; one socket per room, three in Study. A Cat6 loft uplink reaches Netgear GS308E; NAS, Proxmox and FR24 Raspberry Pi are shown there. NeoHub is shown wired from the garage switch. These are documented historical connections, not a live inspection or numbered port map.

```mermaid
flowchart TD
  ISP[EE Full Fibre 900] --> Router[ASUS RT-AX86U Pro]
  Router --> Garage[Garage TP-Link TL-SG1218MPE]
  Garage --> Rooms[Cat6 rooms; Study three sockets]
  Garage --> Loft[Loft Netgear GS308E]
  Garage --> NeoHub[Heatmiser NeoHub]
  Loft --> NAS[Synology NAS]
  Loft --> PVE[Proxmox pve-01]
  Loft --> Flight[FR24 Raspberry Pi]
```

The diagram represents S27's recorded topology; arrows are not port assignments. See [GarageSwitch.md](GarageSwitch.md), [LoftSwitch.md](LoftSwitch.md) and [FlightReceiver.md](../03-Services/FlightReceiver.md). Recover numbered ports, outlet labels, uplink endpoints, cable labels and current PoE loads from the original PDF or a physical inventory. HomeNetwork's cabling and switch pages and Mermaid files are empty.
