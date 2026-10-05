# Rejected and superseded decisions

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

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
## HomeNetwork generations retained as history (S27)

The old 10.0.0.0/8 and 10.52.253.0/24 media design,10.83/multiple-subnet variables, bit-policy and VLAN-aware firewall source are historical/superseded candidates. The newer210/230/250 firewall specification remains an unconfirmed experiment/design document; its effectiveness and deployment are not established. Do not turn it into a newly rejected tested experiment without user evidence.

VLAN goal/testing/result/reason/reopening condition remains D1 above. **DO NOT RECOMMEND AGAIN unless material firmware/hardware change addresses limitation**, or the user explicitly asks. The section-folder layout is being recovered for documentation organisation, not to revive the older architecture.

## Legacy validation defect recovered (S38/S40)

One task reports validate_vlan_sequence wrongly accepting a list missing VLAN53. Another describes a here-document change to preserve errs in the current shell rather than a pipeline subshell, also applied to SSID validation. Exact revision order and regression output are missing. Preserve this software failure/fix history, without declaring it the cause of ASUS VLAN instability or reopening D1. [Five-task evidence](../07-Evidence/LegacyMerlinTasks.md).
