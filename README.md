# BlandingsNetwork

Authoritative configuration and change history for the Blandings home network.

The main reference is:

```text
BlandingsNetwork.md
```

The project records both:

- the **current confirmed network configuration**, and
- important **tested-and-rejected / superseded designs**, so known dead ends are not repeatedly suggested.

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
| v1.0.1 | Initial | Initial project created. |

<!-- PROJECTRELEASE:END -->
