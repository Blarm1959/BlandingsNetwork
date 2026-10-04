# Released record snapshot — v1.0.5

Frozen evidence copy of the master file present in the local v1.0.5 release. Its body is preserved verbatim below, including stale review-baseline and unreleased wording carried through earlier releases. This snapshot is historical evidence. Start at [the current master overview](../BlandingsNetwork.md) for current authority and the organised section files.

---

# BlandingsNetwork

**Authoritative master record for the Blandings home network**

Documentation review: **4 October 2026**. Released baseline for this revision: **v1.0.4**.
This revision is a documentation Change Package, not a released version or a network change.

> This file records tested decisions as well as the current configuration. Do not replace a confirmed design with a theoretically preferable alternative unless new evidence or changed hardware/software justifies reopening the decision.

Read this file before making recommendations. The user's confirmed current architecture takes precedence over earlier chat proposals, generated scripts and screenshots. Only promote a network change after the user confirms it works.

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

The review used local released files and available recent turns from named chats. The explicit keyword pass searched returned text from all 75 listed ChatGPT chats: 22 recent and all 53 archived chats across two pages, including the 33 archived chats previously screened only by title. Previously retrieved portions were reused where available. The recent listing is capped at 50 entries across ChatGPT and Codex and has no pagination parameter. Most chat reads returned only five recent turns with no older-page cursor. This is not an exhaustive account-wide history search. See [the coverage and findings ledger](docs/ChatAudit.md) and [the keyword results](docs/KeywordAudit.md).

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

## 2. Current confirmed architecture

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

The flat main LAN is a tested decision. Logical address groups are administrative labels within one `/16`; they do not establish separate subnets or security isolation. The deliberate Guest Network Pro service below does not reopen the rejected main-LAN VLAN design. Physical cabling and port assignments are UNKNOWN.

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

Static configuration versus DHCP reservation, MAC addresses, hostnames, DHCP lease duration and the full client inventory are UNKNOWN. S2 also lists a Samsung S23 among trusted devices; its address and current VPN role need verification.

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

## 3. Candidate exact settings and reconciliation

**REMEMBERED / VERIFY — this table is not an instruction to configure the router.**

| Field / rule | Latest remembered design (S1) | Evidence needed |
|---|---|---|
| DNS Director Global Mode | Router | Current GUI page, enable state and installed firmware build |
| User defined 1 IPv4 | `10.59.20.102` | Current GUI value and relevant script logic |
| Pi-hole exception | No redirect | Exact client/rule entry and address or MAC match |
| Guest SSID DNS | Quad9 | Guest Network Pro DNS fields and effective resolver |
| DHCP DNS Server 1 / Server 2 | UNKNOWN | Current LAN DHCP fields, router-advertisement options and client lease evidence |
| WAN DNS entries / automatic DNS | UNKNOWN | Current WAN GUI fields |

### Contradictions requiring resolution

1. **Pi-hole exception:** S1 remembers No redirect. S4 contains older assistant advice that 3006 Router mode did not need the Pi-hole in the client list. That reply is not a verified firmware fix or a current setting. Preserve S1 as the latest candidate and inspect the live rule; do not remove the exception based on S4.
2. **Failover target:** S4 proposed switching WAN DNS between Pi-hole and public resolvers. S2 mentions `dnsfilter_custom1`; S1 remembers User defined 1. These are different possible mechanisms. Current scripts and GUI values must establish which is active; do not combine them into a new design.
3. **DNS Director OFF:** S2 records a temporary OFF state during the February 2026 migration. The latest remembered design is Router mode. OFF belongs in history until live inspection resolves the exact current state.
4. **Guest resolver addresses:** S1 confirms Quad9 use, but not the exact guest pair. Older scripts used `9.9.9.9` and `149.112.112.112`; the current fallback is `9.9.9.11`. Do not substitute one set for another without evidence.
5. **IPv6:** S2 records removal during earlier work; current router state is UNKNOWN. Do not treat historical removal as a fresh live inspection or add IPv6-specific rules without deliberate re-enablement and testing.
6. **Old topology and VPN:** S5/S6/S8 contain different LAN/Pi-hole/VPN values and VLAN port descriptions. They are superseded historical context, not alternate current configurations.

## 4. Scripts and services in use

CONFIRMED script names and shared variables location (S1):

```text
pihole_failover.sh
pihole_status.sh
pihole_updown.sh
/jffs/blarm/common/common_vars
```

RELEASED RECORD full paths and state directory (S2), pending live inventory:

```text
/jffs/blarm/scripts/pihole_failover.sh
/jffs/blarm/scripts/pihole_status.sh
/jffs/blarm/scripts/pihole_updown.sh
/jffs/blarm/state
```

Known cron cadence is every 15 minutes (S1). S2 gives this full command:

```cron
*/15 * * * * /jffs/blarm/scripts/pihole_failover.sh
```

The live `cru l` entry, job name, boot registration and duplicate-job state are UNKNOWN. A 15-minute schedule is not evidence of a tested recovery time.

Capture current files verbatim before documenting their behaviour. Record each script's purpose, dependencies, variables, health test, timeouts/retries, failover and recovery triggers, NVRAM keys, service restarts, state/log paths and manual command syntax. Do not infer commands from filenames or source `common_vars` merely to inspect it.

`dnsfilter_custom1` is a historical implementation clue from S2, not proof that the current script changes it. Inventory relevant `/jffs/scripts/` hooks and any persistent firewall additions. No live script bodies or backups are currently preserved in this repository.

## 5. Rejected and superseded decisions

### D1. Main-LAN VLAN segmentation — REJECTED

- **Goal:** separate infrastructure, trusted devices and IoT.
- **What was tested:** VLAN designs on this ASUS/Merlin setup (S1/S2). S5/S6 show an earlier scripted Main/IoT/CCTV/Guest proposal; exact deployed test variants, firmware builds and failure logs are unavailable.
- **Result:** unstable / not viable for this setup, as confirmed by the user (S1).
- **Reason rejected:** did not provide a sufficiently usable and stable network (S1/S2). Do not invent a more specific root cause.
- **Current decision:** flat `10.59.0.0/16` with logical addressing groups.
- **DO NOT RECOMMEND AGAIN unless material firmware/hardware change addresses limitation, or the user explicitly asks to reopen testing.** Record the changed evidence before reopening.

### D2. Earlier LAN and service addressing — SUPERSEDED

- **Goal:** organise the earlier network and services.
- **What was tested / proposed:** S2 records older `192.168.x.x` designs. S5/S6 also contain router `10.0.0.1`, Pi-hole `10.52.252.1` and WireGuard `10.99.0.0/24`, UDP 51820, with full-tunnel AllowedIPs in generated configuration.
- **Result:** replaced by the current baseline; exact deployment history of each generated value is UNKNOWN.
- **Reason superseded:** current user-confirmed addressing and split-tunnel VPN take precedence.
- **Decision:** do not restore old addressing or VPN defaults from old scripts. Historical `10.52` VLAN ranges must not be confused with current guest `10.52.0.0/24`.

Historical generated values in S5/S6/S8 additionally include LAN `10.0.0.0/16` / mask `255.255.0.0`, DHCP start `10.0.0.201` versus `10.0.0.210` in different copies, end `10.0.0.250`, media range `10.52.253.0/24`, SSID `BLARM-00`, generated SSID prefix `BLARM-` and reservation label prefix `ZDR-`. The old VLAN list named 52 Main, 53 IOT, 54 CCTV and 55 Guest. These are historical script proposals, not current SSIDs, reservations or active address groups. Do not preserve old wireless passwords in this record.

### D3. Guest DNS interception scripts — SUPERSEDED / PARTLY REJECTED

- **Goal:** keep guests independent of Pi-hole and direct guest DNS to public Quad9.
- **What was tested:** S2 records custom `iptables` DNAT/forwarding experiments; S4 describes replacing earlier DNS-bypass logic with DNS Director client rules in a VLAN proposal.
- **Result:** preserved as historical work; current basis is Guest Network Pro.
- **Reason rejected / replaced:** specific failure mechanism and final rule removal evidence are missing. Do not claim a technical root cause from the summary alone.
- **DO NOT RECOMMEND AGAIN unless material firmware/hardware change addresses limitation, or the user explicitly reopens it.** First recover the missing reason; do not recreate historical rules automatically.

### D4. Transitional DNS Director OFF — HISTORICAL

- **Goal:** stabilise the February 2026 `10.59` migration (S2).
- **What was done:** DNS Director deliberately OFF during that stage.
- **Result:** later discussions reintroduced DNS Director / failover; exact current state requires verification.
- **Reason historical:** migration-stage settings do not override S1's latest remembered design.

### D5. IPv6 removal — HISTORICAL DECISION

- **Goal / exact test:** not recovered; S2 records IPv6 removal during earlier firewall/DNS work.
- **Result:** removed from an earlier design; current live state UNKNOWN.
- **Reason removed:** not recovered. Retain the decision without inventing its cause.
- **Decision:** do not reintroduce IPv6-specific firewall/DNS-bypass work unless IPv6 has deliberately been re-enabled and tested.

### D6. Earlier WAN-DNS failover and script layout — HISTORICAL / SUPERSEDED CANDIDATE

- **Goal:** Pi-hole failover with public DNS bypass.
- **What was proposed:** S4's August 2025 Router-mode design switched WAN DNS, left DHCP DNS blank and generated VLAN bypass rules. Script names included `/jffs/pihole.sh`, `nvram_setup.sh` and `nvram_setup_vars`.
- **Result:** current confirmed names/layout differ (section 4). Current behaviour is not established by the old proposal.
- **Reason retained:** prevents mixing old WAN-DNS switching and VLAN rules into the later design.
- **Decision:** archive old proposals; verify current script bodies before describing failover.

## 6. Recovered details pending current confirmation

### DDNS and certificates (S7)

Historical proposal: ASUS DDNS `blarm-home.asuscomm.com`; Cloudflare DNS-only CNAMEs `home.blarm.com` and `wg.blarm.com` pointing to it. The user stated an intention to use Let's Encrypt through Merlin's DDNS GUI. This establishes historical intent, not successful deployment or today's settings.

Verify the current provider, hostname, alias records, WireGuard endpoint, certificate setting, covered names and renewal status. Do not promote old assistant claims about certificate/NVRAM behaviour into an operational procedure.

### Old script/package integrity (S5/S6/S8)

S5 names an old seven-file set: `nvram_setup_vars`, `nvram_setup.sh`, `nvram_dhcp_res`, `nvram_firewall.add`, `nvram_pihole_updown.sh`, `nvram_pihole_failover.sh` under `asus_merlin/3006/`, plus `firewall-start` under the system hook directory. This is a historical inventory only.

The user reported empty packages and packages whose comments/formatting differed from locked copies. S6 includes assistant-reported unused variables, but the uploaded files are unavailable for independent checking. S8's earlier lock-in does not make that design current.

Preserve actual live files and any original locked copies byte-for-byte. Record hashes and compare archive contents before calling them a backup. Regenerated chat code is not a recovered original. Expired sandbox download links and missing uploaded contents were not recovered in this review. Do not reconstruct deployment scripts from truncated replies.

### NAS, laptops and backup/name candidates (S10/S11/S23/S24)

- **HISTORICAL USER EVIDENCE:** two laptops running Windows 11 Pro (S10); user changed a laptop screen timeout to 15 minutes. Sleep/hibernate Never was discussed, but the returned evidence does not prove the actual power plan, RDP enable state, successful connection or laptop names.
- **HISTORICAL USER EVIDENCE:** Synology Drive Client on a laptop (S11). Task direction, source/target folders, NAS endpoint and retention remain unknown; do not assume two-way sync or backup is configured.
- **HISTORICAL USER RECOLLECTION:** ABAAS may exist in Restic backups from earlier years (S23). Repository location, snapshot IDs, backup scripts, retention and restore outcome were not recovered.
- **CANDIDATE NAME:** `INV-NAS-012` appears only in conditional assistant advice in S23. It is not a confirmed name for the Synology at `10.59.40.131`, and must not be mapped to it without evidence.
- **HISTORICAL ARTIFACT NAME:** `INV-IONOS-01` appears as a chat and VHDX/split-download name (S24). User confirms split parts reached OneDrive. The assistant describes an 83 GB VHDX, ten split parts, `INV-IONOS-01-Hyper-V-Setup.pdf` and `Join-INV-IONOS-01.zip`; files were not inspected. This does not establish a live home host or IP.
- **EXCLUDE FROM CONFIRMED INVENTORY:** `INV-LAP-01`, `192.168.1.120`, `.150` and `.132` in S10 are explicitly assistant examples. Later S25/S26 summaries use `INV-LAP-01` as a specific Laptop 1 candidate, but no returned user evidence verifies that mapping. Preserve the later candidate separately; do not assign the example IPs to either laptop.

### NeoHub, automation and zones (S13/S22)

S13 contains user logs showing openHAB NeoHub socket traffic and device discovery on 25 November 2025. Thing identifier `neohub:neohub:192_168_1_172` is historical naming evidence; it does not by itself prove the configured socket address. S22 later recalls `10.0.7.172` only in assistant text. Both are historical and must not replace the released-record address `10.59.60.172`.

The assistant interpreted September 2026 screenshots as **neoHub Gen 2, firmware 2218** (S22). The images were not available in this audit, so retain this as a candidate model/build pending verification. An earlier assistant summary also describes Gen 2 with Legacy API enabled (S13).

User logs expose these historical Neo device names: `1st_Floor_Rads`, `Lounge`, `Dining`, `Snug`, `Utility`, `Kitchen`, `Hall_and_WC`, `Hot_Water`, `EnSuite`, `Bathroom`. They are zone names, not independently addressed LAN hosts. Item prefixes in user code include `Rads1F`, `HallWC`, `HW` and the matching room names, with `_Temp`, `_Setpoint` and `_TPS` items. Preserve the distinction between Thing IDs, Item names, zone names and hostnames.

The assistant summary describes a custom openHAB binding adding `timeClockMode`, `awayMode` and `holidayMode`, publishing UNDEF for meaningless hot-water/time-clock temperatures, built using Maven/Java 21 and deployed to `/usr/share/openhab/addons/`. This is a recovery lead, not a preserved build. Capture the source revision, exact JAR, openHAB version, Items/Things/rules and current deployment before declaring it recoverable.

**Recorded failure:** user logs show `Could not cast UNDEF to ... QuantityType` in `heatmiser_summary.rules`, followed by `Parse Error in heatmiser_summary` after attempted replacements. A later assistant summary claims resolution, but no returned user log/test confirms the final fix. Preserve the failure and verify the working rule; do not deploy an old generated replacement automatically.

S22 describes Home Assistant integration, whereas S13 directly evidences openHAB. Whether both were used, whether there was a migration, and what remains current are UNKNOWN. The neoFlo/G3/RF Switch V2 discussion records contemplated purchases/upgrades only; no installation was confirmed. This audit does not validate compatibility or wiring advice.

### Media services and implementation history (S15–S19/S21)

HISTORICAL workflow in the assistant summary (S16): Dispatcharr PostgreSQL VOD data feeds STRM exports for Emby through shared Proxmox/LXC storage. Named files include `vod_export_vars.sh` and `vod_export_reset.sh`; proposed schedules are exporter 02:00 and Emby refresh 04:00. No live cron output, timezone or script files were recovered. Host `/mnt/pve/Share-VOD` and container `/mnt/Share-VOD/{XC_NAME}/` both appear; exact mount mappings and ownership remain unverified.

The user reports a Movies scan became faster up to 90% and then stalled again (S16). Metadata/artwork was the assistant's diagnosis, not a verified root cause or successful fix. Preserve this as an unresolved experiment; do not record the suggested Emby settings as current.

S15 contains user-supplied installer helpers for PostgreSQL, source deployment, Node.js and uv. S18 discusses Nginx, Gunicorn, Celery, Celery Beat, Daphne and PostgreSQL, but it does not establish which services currently run or their ports/IPs. S17's `DDD`/`UUU`/`PPP` are provider placeholders, not local DNS or computer names.

S21 preserves a user correction: missing persistent folders belong under `/data`, not `/opt/dispatcharr/data`; `/opt/dispatcharr/app/*` is the application path in that discussion. Reported missing directories: `/data/logos`, `/data/recordings`, `/data/uploads/m3us`, `/data/uploads/epgs`, `/data/m3us`, `/data/epgs`, `/data/plugins`, `/data/db`, plus `$APP_DIR/logo_cache` and `$APP_DIR/media`. The proposed libpcre3 removal/test and directory fixes have no returned completion evidence. Do not turn old package-availability claims into current Debian guidance.

S19 preserves the user's final helper requirement: `cddocker.sh` should print only the directory so the calling shell can change directory. Earlier generated variants tried to cd inside a child script and are superseded by that requirement. Deployment and installed location are unknown; keep this as development history rather than a live service.

### Other infrastructure recovery leads (S9/S14/S20)

- S9 names printed `GarageSwitch` diagrams, including A4/A5/A6/A7 and combined/rotated PDF variants. The returned turns contain no port assignments or diagram bytes. Recover an original diagram before claiming the physical map is preserved.
- S14 records an LXC backup blocked by `config locked (mounted)`. The returned advice suggested investigating mounts before clearing a stale lock, but no actual CTID, fix or successful backup was returned. The example ID 123 is not a known container. Retain the incident and recover its outcome; do not run old unlock advice automatically.
- S20 records a printer factory reset changing its cloud ePrint identity and a user report that re-enrolment seemed complete. `HP Envy Photo 6230` is an assistant-supplied model candidate; `192.168.52.45` is explicitly an example IP. Printer hostname/MAC/address, actual model and local printing setup remain unknown. Cloud identifiers are not LAN hostnames; current identifiers should be held in the user's private inventory if needed.

### GarageSwitch diagram and device-name recovery (S9)

**HISTORICAL USER REQUIREMENTS, 21 August 2025:** the user requested an A4 landscape PDF for printing, then an A5 version to print and stick on the switch, A6/A7 versions to inspect, and A4 sheets containing two A5 or four A6 diagrams. The final returned request rotates each of the four diagrams by 90 degrees to increase its size while retaining four on A4.

The assistant supplied these exact artifact names: `GarageSwitch.pdf`, `GarageSwitch_A5.pdf`, `GarageSwitch_A6.pdf`, `GarageSwitch_A7.pdf`, `GarageSwitch_A4_with_2xA5.pdf`, `GarageSwitch_A4_with_4xA6.pdf` and `GarageSwitch_A4_with_4xA6_rotated.pdf`. These names are recovery/search identifiers; the files themselves were not recovered or inspected, and no claim of successful printing is implied. An eight-A7 sheet and combined multi-page PDF were offered, without a returned user request or delivered file.

`GarageSwitch` is the historical diagram label. Its current management hostname, correspondence to the TP-Link TL-SG1218MPE, port assignments, uplink, PoE consumers and connected device names remain unverified. The assistant proposed a title mentioning that model; this alone does not prove the diagram's device mapping. Preserve the confirmed switch model and released-record address separately.

### WDL-Flight-01 recovery lead

The user supplied `WDL-Flight-01` as a device/chat search target on 4 October 2026. A case-insensitive search including separator variants found no match in the retrieved portions of 75 listed ChatGPT chats or the returned summaries/text of 25 readable listed Codex chats. Two further listed Codex chats could not be read. Available Codex older-page cursors were followed to the end; older ChatGPT turns remain unavailable, so this is not complete account-history coverage.

The name alone does not establish Raspberry Pi hardware, an ADS-B/Flightradar role, an address, a garage-switch port or active/retired status. Keep those details UNKNOWN until original user evidence is recovered. Do not infer relationships from the word Flight or merge it with another device.

### Additional LXC: CarFinder (S25/S26)

**HISTORICAL USER EVIDENCE, 3 October 2026:** shell prompts show `root@carfinder:/opt/carfinder` and `.venv` use. User test output records successful external Ford API responses. This is evidence of an application host/path and outbound access at that time, not proof of its current network address or container ID.

The user explicitly identifies the CarFinder LXC update command as `cd /opt/carfinder && bash admin/update_lxc.sh` (S26). It is preserved as the named project workflow, not executed by this audit.

Assistant summaries name `carfinder-streamlit.service`, app endpoint `http://10.83.59.181:8501`, and Laptop 1 `INV-LAP-01` with repository folder `D:\Git\Repos\Blarm1959`. These are specific recovery candidates, not freshly verified values. The endpoint is outside the confirmed main LAN `10.59.0.0/16`; its date does not justify replacing the current baseline or assuming another active subnet. Verify where this LXC runs, its actual address/CTID, service/listener, routes and current version. Do not convert the endpoint into a new address-group recommendation.

### Explicit device/service keyword gaps

The 75-chat returned-text search found Heatmiser/NeoHub, Pi-hole/pihole, Unbound, Proxmox/LXC, Emby, Dispatcharr, Synology, Garage Switch and TP-Link/TL-SG1218MPE references. It found **no matches for Netgear, Raspberry Pi/RPi, Flightradar/FR24 or ADS-B/dump1090/readsb** within those retrieved portions.

These are evidence gaps, not proof that the devices/services are absent or decommissioned. Do not assume Pi-hole runs on Raspberry Pi: its confirmed current host is an LXC. Recover original chats/attachments for any Netgear switch/router, Raspberry Pi receiver or ADS-B/Flightradar feeder before assigning model, name, IP, service, location, backup or retirement status.

## 7. Verification and recovery backlog

All items below are OPEN. Record observation date, source, actual values and user confirmation when closing an item. Old chats can supply context, but exact current equipment settings need current evidence.

| ID | Priority | Area | Evidence needed / completion condition |
|---|---|---|---|
| V1 | First | Router DNS | Exact firmware build; DNS Director enable/mode/custom resolver/client list, WAN DNS and LAN DHCP DNS. Resolve section 3 contradictions. |
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

## 8. Change control and chat retirement

1. GitHub holds the long-term released record. Current confirmed settings remain authoritative while investigations proceed.
2. Keep experiments out of the confirmed section. Record goal, starting state, exact change, test/result and rollback separately.
3. Promote a change only after the user confirms it works; record the date and evidence. Rejected and superseded work remains visible.
4. A material firmware/hardware change permits evaluating whether a rejected limitation has changed; it does not automatically overturn the decision.
5. Add source references for recovered chat details and distinguish user observations from assistant proposals.
6. Retire an old networking chat only after its unique decisions, failure reasons and useful files are preserved and reviewed by the user. None of the audited networking chats is cleared for deletion: older turns, attachments, some complete code and original test evidence remain missing. Use the coverage ledger rather than equating a returned page with a complete conversation.

### Repository workflow

- Established project: BlandingsNetwork, `Blarm1959/BlandingsNetwork`; released baseline v1.0.4 verified in local metadata and release history for this revision.
- PowerShellTools released baseline supplied by the user: v2.7.4 (S1/S3).
- Change Package name: `BlandingsNetwork-Changes-v<version>.zip`; filename is the intended release version, not an applied version change.
- Include only changed files. Normally exclude `release.json`, `build-info.json`, `package-lock.json` and release-history-only README changes. PSTP owns versioning, commits, tags and pushes.
- After review, place the package in Windows Downloads and run from the existing project:

```powershell
cd C:\WDL\GitHub\BlandingsNetwork
.\PSTP.ps1 Release -Zip
```

This review does not run a release or edit GitHub. For a genuinely new project, the separate creation standard is `ProjectCreate.ps1 ProjectName` from the PowerShellTools folder; do not recreate this existing project.

## 9. Future-chat starter

```text
BlandingsNetwork – continue from the released master record.
Repository: Blarm1959/BlandingsNetwork
Read BlandingsNetwork.md before making recommendations.
Treat confirmed architecture as authoritative: flat 10.59.0.0/16 LAN, no VLANs.
Do not reopen rejected items unless I ask or material firmware/hardware change addresses the limitation.
Keep remembered settings, historical proposals and experiments separate from confirmed state.
Only promote changes after I confirm they work; record evidence and dates.
Start with the open verification backlog. Exact DNS Director values still need live evidence.
Use Change Packages and PSTP; do not edit GitHub directly unless I explicitly ask.
```

## 10. Release history

### v1.0.1

Initial master documentation established core architecture and addressing, Guest Network Pro, Pi-hole/Unbound and WireGuard baseline; preserved VLAN rejection and superseded designs; added verification gaps.

### v1.0.2

Released documentation added evidence/status distinctions, explicit contradictions, five archived ASUS/Merlin sources, verification/recovery criteria and chat-retirement rules. Release verified in local metadata and tag during the broader audit.

### v1.0.3

Released broader audit added NAS/laptop/Restic, heating automation, media-service and infrastructure recovery leads plus a coverage ledger. Local metadata and Git history confirm the release.

### v1.0.4

Released keyword audit searched all 75 listed ChatGPT returned portions, added CarFinder LXC evidence and an address conflict, and recorded explicit device/service gaps. Local metadata and Git history confirm the release.

The subsequent WDL-Flight-01/GarageSwitch name search and recovered printable-diagram requirements are unreleased documentation changes. They do not establish newly tested network behaviour.
