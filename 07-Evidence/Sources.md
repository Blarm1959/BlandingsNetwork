# Evidence, status and source register

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## 1. Evidence and status

| Status | Meaning |
|---|---|
| CONFIRMED | Current architecture confirmed by the user in source S1; no new equipment inspection is implied. |
| RELEASED RECORD | Detail retained from v1.0.1 (S2), not independently rechecked during this review. |
| REMEMBERED / VERIFY | Candidate current setting; inspect live equipment before treating it as an exact configuration. |
| HISTORICAL | Earlier discussion or configuration; not authority for current settings. |
| REJECTED | Tested approach the user has rejected; preserve the reason and reopening condition. |
| SUPERSEDED | Replaced design; do not restore it as current. |
| UNKNOWN | Evidence is missing; do not fill the gap with a default or assumption. |

The review used local released files and available recent turns from named chats. The explicit keyword pass searched returned text from all 75 listed ChatGPT chats: 22 recent and all 53 archived chats across two pages, including the 33 archived chats previously screened only by title. Previously retrieved portions were reused where available. The recent listing is capped at 50 entries across ChatGPT and Codex and has no pagination parameter. Most chat reads returned only five recent turns with no older-page cursor. This is not an exhaustive account-wide history search. See [the coverage and findings ledger](../docs/ChatAudit.md) and [the keyword results](../docs/KeywordAudit.md).

The subsequent WDL-Flight-01/GarageSwitch search also examined returned summaries/text from 25 readable listed Codex chats, following their available older-page cursors to the end; two other listed Codex chats were unreadable. This extends the audit for those two name families only. It found GarageSwitch in S9 and no WDL-Flight-01 match in the retrieved history.

No router, switch, Pi-hole, Proxmox or NAS was inspected. Chat modification dates are not test dates. Old assistant claims are evidence of a proposal or discussion, not proof of successful operation. Assistant example names, IP addresses and container IDs must not become inventory entries.

### Source register

| ID | Source | Scope and limits |
|---|---|---|
| S1 | User's BlandingsNetwork continuation brief, 4 October 2026 | Current confirmation of the baseline; DNS Director GUI values explicitly require verification. |
| S2 | Local BlandingsNetwork v1.0.1, tag at commit `49c6f1a677f9` | Released master record and README; clean checkout at review. Contains some historical assertions without underlying test logs. |
| S3 | `Blandings Network 1`, chat `6ac24ca8-d7b8-83eb-bf28-c6f1ecbeb60a` | Available recent turns confirm successful v1.0.1 release using PSTP v2.7.4 and repeat the starter. Earlier network material was not returned. |
| S4 | `Merlin 3006 DNS changes`, chat `689f82db-2030-8328-8bf0-f7c461b963ac` | Available turns dated 15 August 2025; earlier WAN-DNS failover proposal and contradictory Pi-hole exception advice. |
| S5 | `ASUS Merlin setup`, chat `689bc18a-1dc8-832d-97da-0f80a2185e40` | Available August 2025 turns; old VLAN setup/scripts and user reports of empty or altered generated packages. Some returned code is truncated. |
| S6 | `ASUS Merlin Setup 2`, chat `689b2920-8d30-8322-87f3-05462552ee2b` | Available turns dated 12 August 2025; old addresses/script variables and assistant-reported unused variables. Uploaded source contents unavailable. |
| S7 | `Asus Merlin DDNS setup`, chat `68a0788f-fda4-8326-b46c-836795dd0602` | Available turns dated 16 August 2025; historical DDNS plan and user intent to use Merlin GUI certificate management. No current implementation confirmation. |
| S8 | `ASUS Merlin setup summary`, chat `689f6b3e-3924-8332-bcb6-3af0fdf28a16` | Available turns dated 15 August 2025; user locked uploaded files at that time. File contents unavailable; old topology is superseded. |
| S9 | `Garage switch diagram`, chat `68a78d22-92bc-832b-bb25-e3f446bed3b6` | 21 August 2025 returned turns name GarageSwitch PDF variants; diagrams/port map unavailable. |
| S10 | `Allow laptop access remotely`, chat `6930c112-0dfc-832b-88c1-fede12c55e66` | 3–4 December 2025 user identifies two Windows 11 Pro laptops and a 15-minute screen timeout. RDP target names/IPs are examples. |
| S11 | `Synology Drive Client overview`, chat `69314b02-06b4-8325-aad4-2635bd96f254` | 4 December 2025 user identifies Drive Client on a laptop; actual sync/backup tasks unknown. |
| S12 | `Allow SSH root login`, chat `68f7d800-7108-8331-9813-a1d30dcac69f` | 21 October 2025 request and generic advice only; no host or implementation confirmation. |
| S13 | `NeoHubAPI usage guide`, chat `690d2e35-3958-8325-8755-65b467daf4b5` | 25 November 2025 user logs/item code and assistant binding summary; final rule fix not confirmed by returned user evidence. |
| S14 | `Proxmox LXC - Config locked (mounted)`, chat `691ef785-0094-8330-8fe6-e3025753c90d` | 20 November 2025 user reports backup failure; actual CTID and outcome unavailable. |
| S15 | `Dispatcharr app overview`, chat `68f7d70e-0b74-8331-bcc3-412ce75456d7` | 31 October 2025 user-supplied installer helpers; proposed revisions are not deployed service evidence. |
| S16 | `Using Dispatcharr with Emby`, chat `690f498c-ede4-832e-a51b-923405191981` | 11 November 2025 scan-stall observation and assistant workflow summary/template. |
| S17 | `Xtream player options`, chat `68aba411-f388-8325-b131-522722ca0acb` | 7 September 2025 user requires Xtream API support; provider strings are placeholders. |
| S18 | `Compare .NET and Dispatcharr stack`, chat `68fcfabe-d974-8329-bd35-9524f83acb59` | 25 October 2025 stack discussion; no live listeners or service states confirmed. |
| S19 | `Docker app directory script`, chat `68fd4e46-9b20-832b-acce-0b100a82ca42` | 25 October 2025 helper design revised to print a directory for caller-side cd. |
| S20 | `HP Ink re-enrollment steps`, chat `68ff6420-d358-8328-8ab1-947076d34282` | 27 October 2025 printer reset/cloud-identity history; model supplied by assistant and IP is an example. |
| S21 | `Libpcre3 Debian status`, chat `68dd3055-feb4-8328-b2fe-8d85274658b5` | 1–2 October 2025 user reports missing runtime directories and corrects /data versus app paths; test plan outcome unavailable. |
| S22 | `Neoflo Hub Upgrade Needs`, chat `6aa03303-d6f4-83eb-8bcf-c7015514a347` | 8 September 2026 assistant interpreted user screenshots as Gen 2 / firmware 2218; screenshots unavailable. G3/RF Switch discussion is a proposal. |
| S23 | `Restore ABAAS Database`, chat `6aa816bc-9030-83eb-9442-09fca2251381` | 14 September 2026 user recalls Restic backups; NAS/host mapping is assistant speculation. |
| S24 | `INV-IONOS-01`, chat `6a7d91f8-a678-83eb-822a-857804062175` | 24–25 September 2026 VHDX/split-download history; no current home-network address. |
| S25 | `Carfinder 2`, chat `6ac0c849-17a4-83ed-8e08-b1b31059b34b` | 3 October 2026 user shell/output shows carfinder, /opt/carfinder and successful external API probes. Address/service labels are assistant summary claims. |
| S26 | `Claude export download guide`, chat `6abfd2c1-0894-83eb-b5a8-ec05188874f3` | 2–3 October 2026 user names the CarFinder LXC update command and supplies deployment output; assistant gives address/service and laptop-name candidates. |
## S27 — HomeNetwork repository recovery

Reviewed 5 October 2026 from the clean local checkout of Blarm1959/HomeNetwork at commit `e70900c801e1056a86e23c50150322d4d01fec2d` (commit date 23 February 2026, subject “Backup 10.59 Router”). An authenticated GitHub read returned 404; the local checkout's equality with the current remote was not verified. Source filenames and SHA256 fingerprints are in [HomeNetworkReview.md](HomeNetworkReview.md).

The repository contains mutually inconsistent generations. Its architecture pages and exported router lists are historical evidence; their “current”, “verified” and “fully operational” labels are the older author's claims, not new user confirmation. The confirmed S1 baseline remains authoritative. New names, MACs, devices, topology, GUI fields and script behaviour require current verification before promotion.

The router NVRAM export carries its own timestamp: 21 February 2026 at 23:20:13 UTC. The adjacent DHCP CSV has no independent timestamp; treat it as an undated repository snapshot, not a current lease list. Named backup directories indicate collection labels, not successful restore tests. No live equipment was inspected and no recovered script was executed.

## S28 — User-recovered GarageSwitch original message

On 5 October 2026 the user supplied the original Garage Switch / TP Link - TL-SG1218MPE port-destination grid in this working chat. Fourteen numbered destinations are supplied; four are blank. The even-row tab spacing is read as port 16 = neoHub and port 14 blank. The spelling “Studty 1” is normalised to Study 1; Diner is preserved. The [hardware record](../02-Hardware/GarageSwitch.md) contains all 18 rows and the reconstructed PDF/SVG diagram.

This is direct user-supplied historical evidence, stronger than the earlier inaccessible diagram references. The original PDF is lost/unavailable, and the new diagram is a reconstruction. Current wiring, later changes, blank-port use, router uplink, downstream switch ports and PoE state were not independently verified. Do not promote those missing details from inference.

## S29 — Home LAN Revisit, user-pasted visible chat

Supplied by the user on 5 October 2026 as a Ctrl-A/Ctrl-C text attachment, identified by the user as Home LAN Revisit. [Review and fingerprint](HomeLANRevisit.md); [unaltered capture](HomeLANRevisit-Pasted.txt). Starts “Loading older messages…”; dates, structured roles, earlier messages and referenced original attachments are missing. Initial export proposal, later final-script reference, architecture drafts, IoT discussion handoff and contradictory DNS reminder tail are preserved. Assistant operational claims and unattributed reminder lines do not establish current settings or user-confirmed tests. No live equipment was inspected.

## Named archived-chat batch — S8a, S29a, S30–S35

Read on 5 October 2026; [findings and fingerprinted capture register](ArchivedChatReview.md). Structured role labels distinguish direct user observations from assistant proposals. One to five turns returned per chat, despite requests for ten; no older cursor or attachment contents. Not a complete-history audit.

| Source | Chat | Limits |
|---|---|---|
| S8a | ASUS Merlin setup summary, `689f6b3e-3924-8332-bcb6-3af0fdf28a16` | 5 available turns; partial capture, originals absent |
| S35 | NAS Tidy, `692e2f98-a374-8326-acca-c0421b521c4c` | 5 available turns; partial capture, originals absent |
| S34 | Restore and compare restic tags, `69308031-f08c-8332-84df-c744c4e5c00d` | 5 available turns; partial capture, originals absent |
| S33 | Backup strategy improvement, `693232fa-6214-8326-b977-43b16e5ec51f` | 5 available turns; partial capture, originals absent |
| S32 | Restic Stage 2 Tagging, `69332a9d-4290-8323-af4a-d5ec6b93a02a` | 2 available turns; partial capture, originals absent |
| S29a | Home LAN Revisit, `6991bdcd-48e0-8392-ba04-e7aed9481063` | 1 available turns; partial capture, originals absent |
| S31 | Firewall Segmentation Design, `699521fe-2ccc-8394-ba70-a3cfa9fcdfab` | 1 available turns; partial capture, originals absent |
| S30 | DNS Director Configuration, `6995ed68-ad00-8393-b0b3-6b0448b46bf0` | 5 available turns; partial capture, originals absent |
