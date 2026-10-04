# BlandingsNetwork

**Authoritative master record for the Blandings home network**

Documentation review: **4 October 2026**. Released baseline: **v1.0.1**.
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

The review used local released files and available recent turns from named chats. No router, switch, Pi-hole, Proxmox or NAS was inspected. Chat modification dates are not test dates. Old assistant claims are evidence of a proposal or discussion, not proof of successful operation.

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

Suggested first evidence batch: current DNS Director, WAN DNS, LAN DHCP and Guest Network Pro pages, followed by the current script files and `cru l`. Capture existing state before considering edits. Keep credentials, VPN private keys and tokens outside this record; document where the user can retrieve them privately.

### Backup/restore record template

For each component record: backup method; contents covered; private storage location; date/version; integrity check; required hardware/software/access; restore steps; dependency order; rollback; test date/result and user confirmation. Until V9/V10 are completed, this file is **not a complete disaster-recovery reference**.

## 8. Change control and chat retirement

1. GitHub holds the long-term released record. Current confirmed settings remain authoritative while investigations proceed.
2. Keep experiments out of the confirmed section. Record goal, starting state, exact change, test/result and rollback separately.
3. Promote a change only after the user confirms it works; record the date and evidence. Rejected and superseded work remains visible.
4. A material firmware/hardware change permits evaluating whether a rejected limitation has changed; it does not automatically overturn the decision.
5. Add source references for recovered chat details and distinguish user observations from assistant proposals.
6. Retire an old networking chat only after its unique decisions, failure reasons and useful files are preserved and reviewed by the user. The five historical chats examined here are not yet cleared for deletion: attachments, truncated code and original test evidence remain missing.

### Repository workflow

- Established project: BlandingsNetwork, `Blarm1959/BlandingsNetwork`; baseline v1.0.1.
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

The 4 October 2026 review adds evidence/status distinctions, explicit contradictions, recovered historical context, verification/recovery criteria and chat-retirement rules. It does not assert a new release or newly tested network behaviour.
