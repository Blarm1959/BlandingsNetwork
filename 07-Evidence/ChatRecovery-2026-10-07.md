# Chat recovery review — 7 October 2026

[Master overview](../BlandingsNetwork.md)

## Purpose and limits

This review was prompted by screenshots of the user's current ChatGPT sidebar and Archived chats page. It searches prior conversation context for home-network material relating to BlandingsNetwork/HomeNetwork, ASUS/Merlin, WAN/LAN, WireGuard, DNS/Pi-hole, Proxmox/LXC, Synology/NAS, NeoHub/Heatmiser, Emby/Dispatcharr and backup workflows.

This is a **recovery aid, not a complete transcript export**. Some prior-chat retrievals expose only selected remembered facts or recent turns, and some visible titles could not be retrieved by title. Therefore:

- do not promote historical values to current configuration without live verification;
- do not infer that an unread title is irrelevant from its name alone;
- do not declare a chat safe to delete unless its complete useful content and attachments have been reviewed or otherwise preserved.

## Newly recovered historical evidence

### Proxmox / NAS

Historical user evidence from 11 December 2025:
- Proxmox hardware: Dell Optiplex 3040M, i5-6500T, 16 GB RAM.
- Synology model stated by the user in that chat: **DS412+**, DSM 6.2.4.
- An older `192.168.1.131` generation used NFS mounts from the Synology to Proxmox.
- `/volume1/Share-WDLPhotos-Tidy` was mounted to `/mnt/Share-WDLPhotos-Tidy`.
- LXC 100 used `mp0`.
- Synology NFS permissions used “Map all users to admin”.
- A `Photos` directory permission problem (`drwx------`) caused an LXC permission failure and was resolved through a DSM recursive-permission change.

Historical user evidence from 23 March 2026:
- Proxmox hostname `pve-01` used Synology NFS at `10.83.59.131`.
- fstab used `_netdev,x-systemd.automount`.
- Historical shares included `Share-WDLMedia`, `Share-WDLMedia-DL`, `Share-WDLPhotos` and `Share-WDLPhotos-Tidy`.
- `immich-wgl` LXC 112 used `10.83.59.112`.
- `10.83.59.131:/volume1/Share-WDLPhotos-WGL` was mounted at `/mnt/Share-WDLPhotos-WGL`.
- These belong to the superseded `10.83` generation and must not replace current `10.59` addresses.

### Heating / NeoHub

A 8 September 2026 user conversation gives stronger historical evidence that the Heatmiser hub was **neoHub Gen 2**. The prior local address in that conversation was `10.0.7.172`. The assistant interpreted screenshots as firmware **2218**.

This strengthens the model/build recovery lead but does not prove the current model, firmware, address or API state. The current released-record address remains `10.59.60.172` pending live verification.

### Media / Emby / Dispatcharr

Historical user evidence from 3 March 2026:
- HDHomeRun: `10.83.54.121`.
- Emby IPTV LXC: ID `123`, `10.83.54.123`.
- Dispatcharr LXC: ID `129`, `10.83.54.129`.
- Dispatcharr nginx listened on `0.0.0.0:9191`.
- Dispatcharr interface `eth0` had `10.83.54.129/16`.
- A working directory shown was `/data/STRM/TV`.

These values belong to the older `10.83` generation.

From the visible recent chat **Emby old video playback fix**:
- Emby ran in unprivileged LXC ID `123`.
- Media path `/mnt/Share-VOD`.
- Old home-video/DVD material stopped after about 30 seconds.
- User had four video folders at `D:\WDLMedia\HomeVideos`.
- Synology-hosted media included a historical path under `/mnt/Share-WDLMedia/HomeVideos/.../VIDEO_TS`.
- The assistant's VIDEO_TS/remux diagnosis remains advice, not a confirmed root cause.

From **Emby Library setup**:
- Movies library folder: `/mnt/Share-VOD/Movies`.
- STRM/NFO content came from Dispatcharr via the `strm2vod` plugin.
- The user reported Movies and TV Shows without images and supplied generated STRM/NFO examples.
- The assistant reported the inspected NFOs lacked useful artwork URLs. This is historical troubleshooting, not current configuration.

### Syncrify / NAS / Restic

From **Syncrify to NAS workflow design** (December 2025):
- VPS: `INV-IONOS-01`.
- Laptop: `INV-LAP-01`.
- NAS: `INV-NAS-01`.
- Syncrify client transferred VPS data to the laptop; Syncrify server was on the laptop.
- Laptop paths:
  - `D:\Syncrify\syncrify@inventive.co.uk\INV-LAP-01-L`
  - `D:\Syncrify\syncrify@inventive.co.uk\INV-LAP-01-Z`
  - `D:\Syncrify\syncrify@inventive.co.uk\access.log`
- NAS targets:
  - `\\INV-NAS-01\Share-01\Inventive_Backup\L`
  - `\\INV-NAS-01\Share-01\Inventive_Backup\Z`
  - `\\INV-NAS-01\Share-01\Inventive_Backup\access.log`
- Restic repository: `/volume1/restic_repos/inventive`.
- User requirement: full retention; no `forget`/`prune` for this historical workflow.

Much of this overlaps the v2.0.4 Restic recovery, but this review confirms the exact per-laptop source subfolders.

## Visible chats already represented in the released repository

The following visible titles are already represented by named sources or recovered excerpts in released v2.0.4:

| Chat title | Existing source/status |
|---|---|
| Allow laptop access remotely | S10 |
| Allow SSH root login | S12 |
| NeoHubAPI usage guide | S13 |
| Proxmox LXC - Config locked (mounted) | S14 |
| Dispatcharr app overview | S15 |
| Using Dispatcharr with Emby | S16 |
| Compare .NET and Dispatcharr stack | S18 |
| Neoflo Hub Upgrade Needs | S22 |
| INV-IONOS-01 | S24 |
| Update nvram_setup.sh for loop handling | S40 excerpt |
| Edit nvram_pihole_failover.sh path | S39 excerpt |
| Add validate_vlan_sequence test | S38 excerpt |
| Add tests for SSID and DHCP validation | S37 excerpt |
| Update iptables in nvram_setup.sh for DNS | S36 excerpt |

These are **represented**, but several were only partially read or preserved as excerpts. Representation does not automatically mean the original chat is safe to delete.

## Additional visible chats whose useful facts are captured by this v3.0.1 package

| Chat title | Captured here |
|---|---|
| Emby old video playback fix | LXC 123, `/mnt/Share-VOD`, home-video paths and ~30-second playback symptom |
| Emby Library setup | `/mnt/Share-VOD/Movies`, Dispatcharr/strm2vod origin, image/NFO issue |
| Syncrify to NAS workflow design | exact VPS/laptop/NAS names, source/target paths and Restic repository |

The retrieval available for these chats is still not a guaranteed complete transcript or attachment set, so they should not yet be marked safe to delete.

## Visible archived titles that still need a complete content review

The screenshot also shows titles that may relate to the older ASUS/Merlin/codebase work but were not sufficiently retrievable in this pass:

- OpenHAB Heatmiser Setup
- Generate complete bash script
- Find common code check tasks
- Run shellcheck on scripts
- Update VERSIONS.md for accuracy
- Refactor functions to use local variables
- Escape markers in replace_marked_block
- Find and fix typos
- Provide complete coding guidelines
- Find and fix an important bug
- Add CODEGEN.md to repo root

Do **not** delete these on the strength of this review. Some may be generic coding work; the titles alone are not enough to prove they contain no unique router/script material.

## Other visible current chats worth retaining for now

- **BlandingsNetwork 3** — this is the current working chat and should remain.
- **Neoflo Hub Upgrade Needs** — already represented as S22 but screenshot/attachment provenance is still useful until the live NeoHub state is verified.
- **INV-IONOS-01** — mostly VPS/virtual-machine recovery rather than the physical Blandings LAN, but some NAS/Syncrify naming context overlaps this project.

## Retirement status after v3.0.1

This package improves preservation but **does not clear the above chats for deletion** under the project's existing evidence rule. The remaining blocker is completeness: several prior-chat reads returned only selected turns or remembered facts, and attachment content was not always available.

A chat can be moved to “ready to remove” after:
1. its full useful text has been reviewed or exported;
2. unique attachments/scripts/commands have either been preserved or deliberately classified as unnecessary;
3. relevant facts have been stored in the repository with historical/current status kept separate; and
4. the package containing that recovery has been released successfully through PSTP.
