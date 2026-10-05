# HomeNetwork recovery and reconciliation

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Scope, authority and layout

Reviewed the clean local HomeNetwork checkout on 5 October 2026, commit `e70900c801e1056a86e23c50150322d4d01fec2d`, dated 23 February 2026. GitHub connector returned 404, so freshness against the remote is unverified. Read all Markdown/Mermaid pages and the router source/scripts relevant to addressing, DNS, exports, policy and setup. Router backup member names were inspected for recovery scope; binary configs/full secret-bearing NVRAM and archive contents were not imported.

Recovered section organisation: architecture, hardware, services, rebuild, disaster recovery. Added separate history/evidence sections so historical designs do not compete with confirmed configuration. BlandingsNetwork.md is the entry point; focused pages hold details. Existing chat audits remain in docs/. The prior released master is frozen as evidence, preserving all its previous text.

## Material recovered

- Netgear GS308E loft switch; Dell Optiplex 3040M/pve-01; garage-to-loft/rooms cabling narrative; no numbered switch-port list.
- Full router reservation/lease/name-only export, MACs, service labels, laptops, printer, HDHomeRun, media players/TVs, phones, powerline and older container/device labels.
- WDL-RPI3-FLIGHT-01/FR24 at historical 10.59.60.171, with a second same-name MAC; historical WDL-RPI3-PI-HOLE label.
- Exact historical Pi-hole failover/updown/status source and common_vars, fixed DNS Director key, counters, health probes, restarts, logger/state paths; router exporter and policy logging helper details.
- Timestamped21 February2026 router export, historical DNS GUI design and labelled configuration/JFFS backups.

## Contradictions and incomplete implementation

| Source conflict | Treatment |
|---|---|
| README10.0/8/media 10.52.253; architecture10.59/16; common_vars10.83/multi-subnet | Preserve generations; S1's10.59 baseline remains authoritative. |
| S1 IoT 140 vs old IOTM 210/cloud IoT 230/unknown 250 | No address migration; verify actual inventory/policy. |
| Latest rememberedGlobalRouter vs old DNS pageGlobal Custom1/no Router | Record candidate fields separately and inspect current GUI. |
| DNS page“enabled/operational” vs blank exported dnsfilter_enable | No enable/mode inference; export is historical. |
| Pi-hole rule uses old name-only MAC vs reserved MAC | Verify current client exception and identity. |
| Root MAC-allowlist/bit policy vs newer semantic policy vs VLAN-aware source | Preserve experiment intent; no enforcement claim. |
| net-policy-apply.sh starts with helper calls and later stray case terminator | Incomplete source; do not deploy. |
| Setup DHCP_* variables vs common_vars ROUTER_DHCP_* | Mismatched rebuild inputs; no tested rebuild claim. |
| Duplicate Flight/Pi-hole names and inconsistent prose/CSV status | Preserve records separately; no inferred replacement/interface relationship. |

The hardware/service/rebuild/recovery pages and all three Mermaid files in HomeNetwork are empty; names indicate intended sections, not recovered implementation. NumberedGarageSwitch ports remain unavailable. No current network setting was promoted from historical evidence and no chats/repository are cleared for deletion.

## Source-file fingerprints

SHA256 fingerprints identify reviewed local contents. They are not signed attestations or proof of remote freshness.

| Source relative path | Bytes | SHA256 |
|---|---:|---|
| `.gitattributes` | 1025 | `D053612E198FBB3CF2020DE7AD656AD510E5DB6424A0EBF9805E9CB81BFC6F41` |
| `.gitignore` | 156 | `C93C095AB7CDDD86BB0757CF8853C7AF10D141BF448EE64F9155D91E1514300C` |
| `CHANGELOG.md` | 42 | `992CE02BD4A6EEF41D87A40663C48DCA374783E73AEA50BD6EA7C156364150E7` |
| `create_homenetwork_repo.ps1` | 4333 | `5CF49609D71F89F0FADCBC4BAF622FDF80433F50FAE51774CB4A518DEC9B234B` |
| `README.md` | 820 | `C1A1E06B10E049A387E5546084625E859CC693F780DEB05F02A29DAF3EF9847D` |
| `01-Architecture/01-network-overview.md` | 3340 | `0CD6C9352BF27A399048703F1E58F03B8E3FA452808F4A10B9C13A15F0EA1C82` |
| `01-Architecture/02-ip-addressing.md` | 2654 | `EDABD2CA046B6B00CB116E476303378E6419B08F1CA4554DBA091E322D9345D9` |
| `01-Architecture/03-dhcp-reservations.md` | 3446 | `601A883FD2F11072C0263639A4E038E797D22DBE230BFAC1EF31B7CB32F1EDE8` |
| `01-Architecture/04-dns-and-pihole.md` | 4260 | `9C76E6C4209F8EE6561F06CFAF4C7F5FDFD9AA327A766CA223D3A2F9CF0D765A` |
| `01-Architecture/05-firewall-policy.md` | 4043 | `6E92EDAFEAEA534971E09F174B9423091261A944ABE5B799378600C026CD7BD2` |
| `02-Hardware/cabling-layout.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `02-Hardware/garage-switch-tl-sg1218mpe.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `02-Hardware/loft-switch-gs308e.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `02-Hardware/router-rt-ax86u-pro.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `03-Services/heatmiser-neohub.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `03-Services/media-storage.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `03-Services/pihole-unbound.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `03-Services/proxmox.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `04-Rebuild-Guide/01-factory-reset-router.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `04-Rebuild-Guide/02-configure-lan-and-dhcp.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `04-Rebuild-Guide/03-configure-dnsmasq-reservations.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `04-Rebuild-Guide/04-configure-firewall-policy.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `04-Rebuild-Guide/05-verify-and-test.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `05-Disaster-Recovery/dr-dns-issues.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `05-Disaster-Recovery/dr-internet-down.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `05-Disaster-Recovery/dr-locked-out.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `05-Disaster-Recovery/dr-pihole-down.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `05-Disaster-Recovery/dr-router-failure.md` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `diagrams/logical-topology.mmd` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `diagrams/physical-topology.mmd` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `diagrams/policy-flow.mmd` | 0 | `E3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855` |
| `router/jffs/blarm/common/common_vars` | 1755 | `2E6ED4E7824061B77327A699D2446F55E9583D212DAE0DA35C5F2610B6CCECEF` |
| `router/jffs/blarm/common/dhcp_res` | 1747 | `61047806B6371AC71395FC867DCCE4391038EC618002485729EC4B3B71DFF0DE` |
| `router/jffs/blarm/scripts/net-policy-apply.sh` | 13196 | `64C88D7E9EACE360C1C177762CD45352F0B1FA1B780FC94554A3237D6FB7424F` |
| `router/jffs/blarm/scripts/ng-syslog-siphon.sh` | 1460 | `C7CD69CF006032C29AB5642EA4FC26EA64DC83F02F7168C3003E78AC250545F0` |
| `router/jffs/blarm/scripts/pihole_failover.sh` | 2399 | `3096341EADD9C430E9F33A220C8F4244448C99C93BF47A438FEDE10577E2C131` |
| `router/jffs/blarm/scripts/pihole_status.sh` | 2256 | `FD7FC40810786C02D0A24CDBACF414F2A0CA7CB304FEAE6F7A99975A1D86FB47` |
| `router/jffs/blarm/scripts/pihole_updown.sh` | 1492 | `86E5513719CAC964F818AB085FBFFD5E8A501589294929F9220898E0CB36CEDA` |
| `router/jffs/blarm/scripts/router_nvram_show.sh` | 8800 | `65C142A7AD59AE3B352A2F07F95BCFAE0DDE0DF122A3000F0AACF95FE4155398` |
| `router/jffs/blarm/scripts/output/router_dhcp.csv` | 5675 | `9846B7C7813B27573050E92990EB1F48B8B90BC59B82A7489D0BEE1474FCFC6E` |
| `router/jffs/blarm/scripts/output/router_lists_raw.txt` | 4177 | `E16079A151E8EBF6333AA46C98F01B7D4C50855C1DF56ED27B888632356E4321` |
| `router/jffs/blarm/scripts/output/router_nvram.txt` | 6399 | `F55BD0428D120175DB08847CB686641CDD2561C85DDE23D87241A52BE74D75F3` |
| `router/jffs/blarm/setup/homenetwork-apply.sh` | 704 | `21F63CDF02EB99CA1285F54F2929985D02736164485EE18762CA9CEA5EC5A296` |
| `router/jffs/blarm/state/ng_phase` | 2 | `53C234E5E8472B6AC51C1AE1CAB3FE06FAD053BEB8EBFD8977B010655BFDD3C3` |
| `router/jffs/blarm/state/pihole_outage_fails` | 2 | `06E9D52C1720FCA412803E3B07C4B228FF113E303F4C7AB94665319D832BBFB7` |
| `router/jffs/blarm/state/pihole_outage_state` | 5 | `C03338E8AA80E1A06AD8ED97CCCB4102773C4CE79C32839FD13F2F1B1A94ADA1` |
| `router/jffs/blarm/state/pihole_outage_succ` | 2 | `9A271F2A916B0B6EE6CECB2426F0B3206EF074578BE55D9BC94F6F3FE3AB86AA` |
| `router/jffs/scripts/firewall-start` | 735 | `494B46A6CF1596A1CEFA4B4A91BC98F0DD3860D7915E2264CEDE5B608F612439` |
| `router/legacy/nvram_dhcp_res` | 886 | `FC772638F3854CC08AE9A0FCFB317580549F77D68DF93FE42838B7447C4055F1` |
| `router/legacy/nvram_firewall.add` | 743 | `50FAEA1953CB826811DC1D1E218270BD9B975764D6584734503AF47B6618B3AA` |
| `router/legacy/nvram_pihole_failover.sh` | 2008 | `D9872EAA422CD62B7E6C27CF2BA7B5B7D52154B8B667EC33BF188A541BA13657` |
| `router/legacy/nvram_pihole_updown.sh` | 2794 | `BE6AA6FCF41D8C6C4FE307CC8A1180A787BDDEB2B4BCCA52E8BCED33DB640D1E` |
| `router/legacy/nvram_setup_vars` | 5383 | `92F10970FE348DCB66CD0CD468194CB7C23838BA09CD2FE42F7AB49572914C4B` |
| `router/legacy/nvram_setup.sh` | 32001 | `355331254D030C652C7685870D8141ABEB4CB0674002945F29A8B5B438FA1760` |
| `router/legacy/scripts/firewall-start` | 582 | `BA32EC4A904E3781DE48C281BC36696440493FD6B86FEA85334A4B45A37FA822` |


## Later recovery and coverage update

S28 subsequently recovered the original garage-switch numbered map from user text; see [GarageSwitch](../02-Hardware/GarageSwitch.md). The lost PDF is no longer needed to preserve those destinations. The [section-coverage audit](SectionCoverage.md) maps all 18 zero-length HomeNetwork Markdown pages to populated records here, and [diagram regeneration](../diagrams/README.md) preserves data, renderer and outputs. The older repository's empty files remain historical placeholders; new development is kept in BlandingsNetwork.
