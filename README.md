# BlandingsNetwork

Authoritative configuration and change history for the Blandings home network.

Start with [BlandingsNetwork.md](BlandingsNetwork.md), the master overview and index. Architecture, hardware, services, rebuild, disaster recovery, history and evidence each have focused Markdown pages. Confirmed current settings are separate from historical HomeNetwork and chat recovery leads. The full [device inventory](01-Architecture/DeviceInventory.md), [GarageSwitch record](02-Hardware/GarageSwitch.md) and [verification backlog](07-Evidence/Verification.md) are linked from the overview.

The main reference is:

```text
BlandingsNetwork.md
```

The project records both:

- the **current confirmed network configuration**, and
- important **tested-and-rejected / superseded designs**, so known dead ends are not repeatedly suggested.

## Stored diagrams

[Diagram source and regeneration](diagrams/README.md) explains how to rebuild printable PDFs, SVGs and linked tables from the stored JSON and builder. [Section coverage](07-Evidence/SectionCoverage.md) maps the older HomeNetwork empty placeholders to populated pages here.

## Repository workflow

This project uses the same PowerShellTools/PSTP workflow as the other local projects.

New project bootstrap:

```powershell
cd C:\WDL\GitHub\PowerShellTools
.\ProjectCreate.ps1 BlandingsNetwork
```

Release workflow from the project folder:

```powershell
cd C:\WDL\GitHub\BlandingsNetwork
.\PSTP.ps1 Release -Zip
```

Change Packages should contain only files that are actually being changed.  
PSTP manages the normal release/version metadata.

<!-- PROJECTRELEASE:BEGIN -->

## Release History

| Version | Type | Notes |
|---------|------|-------|
| v2.0.3 | Package | Released from imported Change Package. |
| v2.0.2 | Package | Released from imported Change Package. |
| v2.0.1 | Explicit | Version-only test release. |
| v1.0.8 | Package | Released from imported Change Package. |
| v1.0.7 | Package | Released from imported Change Package. |
| v1.0.6 | Package | Released from imported Change Package. |
| v1.0.5 | Package | Released from imported Change Package. |
| v1.0.4 | Package | Released from imported Change Package. |
| v1.0.3 | Package | Released from imported Change Package. |
| v1.0.2 | Package | Released from imported Change Package. |
| v1.0.1 | Initial | Initial project created. |

<!-- PROJECTRELEASE:END -->
