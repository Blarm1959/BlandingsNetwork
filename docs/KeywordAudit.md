# BlandingsNetwork keyword audit

Audit date: 4 October 2026. Released baseline: v1.0.3. This audit accompanies an unreleased documentation Change Package.

## Scope and limits

The requested terms were searched case-insensitively in returned user and assistant text from **75 listed ChatGPT chats: 22 recent and all 53 archived**. Previously retrieved text was reused; the 33 archived chats previously screened only by title were also opened, together with one newly listed recent chat. Twenty chats contain at least one requested keyword family.

This is a complete keyword search of those retrieved portions, **not a complete account-history search**. The recent listing is capped at 50 combined Codex/ChatGPT entries and has no older-entry cursor. Most chat reads returned at most five latest turns despite requesting ten, with no older-turn cursor. Some text remains truncated even with an 18,000-character allowance. Images, original attached files and older sandbox downloads were not recovered. Codex histories were not included. ChatGPT in the available browser was signed out, so browser search of older history was unavailable.

A match can be user evidence, an assistant example, a proposal or a historical configuration. Counts below describe chats with matching text; they do not establish installed devices or current settings. Absence of a match does not establish absence or retirement of a device/service.

## Requested terms

| Keyword family | Matching chats | Exact chat titles |
|---|---:|---|
| Heatmiser | 3 | Blandings Network 1; Neoflo Hub Upgrade Needs; NeoHubAPI usage guide |
| Netgear | 0 | No match in retrieved portions |
| Raspberry Pi / RPi | 0 | No match in retrieved portions |
| Flightradar | 0 | No match in retrieved portions |
| Pi-hole / pihole | 5 | Blandings Network 1; ASUS Merlin setup; Merlin 3006 DNS changes; ASUS Merlin Setup 2; ASUS Merlin setup summary |
| Unbound | 3 | Blandings Network 1; Merlin 3006 DNS changes; ASUS Merlin setup summary |
| ADS-B | 0 | No match in retrieved portions |
| Proxmox | 4 | Blandings Network 1; Allow SSH root login; Proxmox LXC - Config locked (mounted); Using Dispatcharr with Emby |
| LXC | 9 | Blandings Network 1; Carfinder 3; Carfinder 2; Claude export download guide; Allow SSH root login; Proxmox LXC - Config locked (mounted); Dispatcharr app overview; Using Dispatcharr with Emby; Libpcre3 Debian status |
| Emby | 2 | Using Dispatcharr with Emby; Xtream player options |
| Dispatcharr | 5 | Dispatcharr app overview; Using Dispatcharr with Emby; Compare .NET and Dispatcharr stack; Docker app directory script; Libpcre3 Debian status |
| Synology | 2 | Blandings Network 1; Synology Drive Client overview |
| Garage Switch | 1 | Garage switch diagram |
| TP Link / TL-SG1218MPE | 2 | Blandings Network 1; Garage switch diagram |

Variants included Heatmiser/NeoHub/neoFlo, Netgear with spacing, Raspberry Pi/RPi/Raspbian, Flightradar24/FR24, pi-hole/pihole with spacing or underscores, Proxmox/PVE, singular/plural LXC, TP-Link/TP Link and TL-SG1218MPE. ADS-B variants included dash styles, dump1090, the whole word readsb and 1090 MHz. Whole-word boundaries excluded unrelated text such as “reads back”.

## Findings and evidence status

- **Heatmiser:** existing master-record leads include user openHAB logs and heating-zone names in NeoHubAPI usage guide, plus assistant interpretation of hub screenshots in Neoflo Hub Upgrade Needs. Current hub generation/build, API mode and automation platform still require verification. A neoFlo/G3 upgrade proposal is not an installed change.
- **Pi-hole and Unbound:** the current user-confirmed LXC baseline remains 10.59.20.102. Older Merlin chats contain transitional DNS and script designs. Exact current DNS Director/router GUI values and live script contents remain unverified; earlier configurations are preserved as history.
- **Proxmox/LXC:** preserve the mounted/locked container backup incident without inventing its CTID or successful resolution. The additional CarFinder evidence below provides a named LXC lead. Generic SSH advice does not establish a deployed configuration.
- **Emby/Dispatcharr:** user-reported scan stalls and implementation/path discussions remain useful recovery leads. Assistant schedules, diagnosis, exporter settings and mount mappings are not confirmed running values. A comparison chat alone does not establish deployment.
- **Synology:** the baseline NAS address remains 10.59.40.131. The Drive Client chat mentions a laptop client but does not establish the NAS model or current endpoint.
- **Garage Switch/TP-Link:** switch diagram filenames were retrieved, but the PDF diagrams and port map were unavailable. The confirmed model remains TL-SG1218MPE from the baseline; diagram discussion is not sufficient to reconstruct wiring.
- **Netgear, Raspberry Pi/RPi, Flightradar and ADS-B:** no matches in the retrieved portions. These are explicit recovery gaps. Do not infer that they were never used, were decommissioned, or that the Pi-hole LXC runs on a Raspberry Pi.

## Additional CarFinder evidence

The LXC search found relevant material under titles that do not identify home networking:

| Source | User evidence | Status / limits |
|---|---|---|
| S25 — Carfinder 2 | On 3 October 2026, pasted shell output uses `(.venv) root@carfinder:/opt/carfinder#`; an external Ford API test returned HTTP 200 and results. | Historical evidence for hostname label, application path, Python virtual environment and successful outbound API access at that time. No current CTID, home-network location or address established. |
| S26 — Claude export download guide | User explicitly requested the LXC update command `cd /opt/carfinder && bash admin/update_lxc.sh`. Pasted release/update output records CarFinder v2.0.13 and a fetch/fast-forward to commit `b74331e`. | Historical command and update evidence. The retrieved output does not independently verify the final running service or current release. |
| S25/S26 assistant statements | Candidate endpoint `http://10.83.59.181:8501`, service `carfinder-streamlit.service`, and Laptop 1 name `INV-LAP-01`. | Assistant claims requiring user/live verification. The address is outside confirmed `10.59.0.0/16`; do not add a new home subnet or replace the confirmed range. |
| Carfinder 3 | Assistant mentions LXC deployment. | No additional user-confirmed network setting retrieved. |

The earlier remote-access chat used names such as INV-LAP-01 as examples. Later CarFinder assistant text uses it as a specific candidate. Preserve that distinction and verify the mapping before adding it to confirmed inventory.

## Matching source register

All titles below are the exact returned chat titles. IDs allow matching to source records; no chats have been cleared for deletion.

| Chat title | Chat ID | Matched keyword families |
|---|---|---|
| Blandings Network 1 | `6ac24ca8-d7b8-83eb-bf28-c6f1ecbeb60a` | Heatmiser; Pi-hole / pihole; Unbound; Proxmox; LXC; Synology; TP Link / TL-SG1218MPE |
| Carfinder 3 | `6ac0dc71-2308-83ed-a19e-12b3f7977def` | LXC |
| Neoflo Hub Upgrade Needs | `6aa03303-d6f4-83eb-8bcf-c7015514a347` | Heatmiser |
| Carfinder 2 | `6ac0c849-17a4-83ed-8e08-b1b31059b34b` | LXC |
| Claude export download guide | `6abfd2c1-0894-83eb-b5a8-ec05188874f3` | LXC |
| Garage switch diagram | `68a78d22-92bc-832b-bb25-e3f446bed3b6` | Garage Switch; TP Link / TL-SG1218MPE |
| ASUS Merlin setup | `689bc18a-1dc8-832d-97da-0f80a2185e40` | Pi-hole / pihole |
| Merlin 3006 DNS changes | `689f82db-2030-8328-8bf0-f7c461b963ac` | Pi-hole / pihole; Unbound |
| ASUS Merlin Setup 2 | `689b2920-8d30-8322-87f3-05462552ee2b` | Pi-hole / pihole |
| Synology Drive Client overview | `69314b02-06b4-8325-aad4-2635bd96f254` | Synology |
| Allow SSH root login | `68f7d800-7108-8331-9813-a1d30dcac69f` | Proxmox; LXC |
| NeoHubAPI usage guide | `690d2e35-3958-8325-8755-65b467daf4b5` | Heatmiser |
| Proxmox LXC - Config locked (mounted) | `691ef785-0094-8330-8fe6-e3025753c90d` | Proxmox; LXC |
| Dispatcharr app overview | `68f7d70e-0b74-8331-bcc3-412ce75456d7` | LXC; Dispatcharr |
| Using Dispatcharr with Emby | `690f498c-ede4-832e-a51b-923405191981` | Proxmox; LXC; Emby; Dispatcharr |
| Xtream player options | `68aba411-f388-8325-b131-522722ca0acb` | Emby |
| Compare .NET and Dispatcharr stack | `68fcfabe-d974-8329-bd35-9524f83acb59` | Dispatcharr |
| Docker app directory script | `68fd4e46-9b20-832b-acce-0b100a82ca42` | Dispatcharr |
| Libpcre3 Debian status | `68dd3055-feb4-8328-b2fe-8d85274658b5` | LXC; Dispatcharr |
| ASUS Merlin setup summary | `689f6b3e-3924-8332-bcb6-3af0fdf28a16` | Pi-hole / pihole; Unbound |

## Remaining recovery work

Recover older active chats, older turns and original attachments before claiming complete coverage. Prioritise the four no-match families, original garage switch diagrams/port labels, device names and addresses, current container inventory and the CarFinder address conflict. Keep new evidence in historical/verification sections until the user confirms the current working state. The master record backlog V15–V17 tracks these gaps.

