# Merlin scripts and implementation details

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

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

`dnsfilter_custom1` is a historical implementation clue from S2, not proof that the current script changes it. Inventory relevant `/jffs/scripts/` hooks and any persistent firewall additions. Historical script bodies and backup locations have now been recovered from S27; no live file inventory or restore verification has been performed.
## Recovered source behaviour (S27; historical copies)

| File | Observed source behaviour | Verification limits |
|---|---|---|
| pihole_failover.sh | Single-shot cron check; nslookup of configured domain directly against Pi-hole, otherwise nc UDP/53 probe; counters/state in /jffs/blarm/state; calls updown on state transition. | nc fallback does not demonstrate a successful DNS answer; switch errors are suppressed before state is written. Initial UP state does not independently reconcile a stale resolver key. |
| pihole_updown.sh | Sets fixed dnsfilter_custom1 only if changed, commits NVRAM, best-effort restart_dnsfilter/restart_dnsmasq, logs changes. | Successful live switching and service restarts are not verified. |
| pihole_status.sh | Displays key, state/counters, variables and direct Pi-hole health probe. | Historical source; output labels alone do not establish effective client DNS. |
| common_vars | Check domain example.com; fail/success thresholds 1/1; fallback 9.9.9.11; also contains 10.83 LAN/Pi-hole and rejected multi-subnet/VLAN constants. | Do not apply its addressing to the 10.59 baseline. |
| router_nvram_show.sh | Exports labelled NVRAM, raw lists and merged CSV, tries several lease-file locations, guest summary enabled BSSes. | Historical diagnostic helper; CSV has trailing/misaligned header and needs defensive parsing. |
| ng-syslog-siphon.sh | Copies matching NG probe/drop or ng_policy lines from /tmp/syslog.log using byte offset; default /jffs/blarm/logs/ng_policy.log, 256KiB rotation, five retained files. | No running schedule or current policy logging established. |
| homenetwork-apply.sh | Writes LAN NVRAM and dnsmasq.conf.add reservations, commits/restarts. | Uses DHCP_START/DHCP_END/DHCP_LEASE while copied common_vars names ROUTER_DHCP_*; set -u can stop execution. Overwrites the dnsmasq addition file. Historical incomplete rebuild input. |

Thresholds 1/1 on a 15-minute schedule are source settings, not a measured outage/recovery guarantee. The complete three Pi-hole script copies plus common_vars are preserved as code-fenced historical evidence in [RecoveredPiHoleSource.md](../07-Evidence/RecoveredPiHoleSource.md). No executable installation files are supplied by this change.

## Export helper requirements recovered from Home LAN Revisit (S29)

Historical user requirements: run on the router without installing Python; use a script-relative `output` folder; produce `router_nvram.txt` and `router_dhcp.csv`; combine reservations, friendly names, MACs/IPs and unreserved connections. The assistant proposal names `router_lists_raw.txt` as the third output. Main Wi-Fi and Guest Network Pro were requested alongside LAN, DHCP and DNS Director fields.

The visible initial shell/awk proposal predates the fully developed script the user says was attached from another chat. Do not substitute that proposal for the final helper or assume its guest NVRAM keys match the installed firmware. Referenced attachments are absent. The S27 source remains separate historical evidence. [S29 review](../07-Evidence/HomeLANRevisit.md) preserves the distinction. A missing lease is not proof that a device is offline.

## Historical installed cron evidence (S30)

User shell output dated 19 February 2026 reports:

```cron
*/15 * * * * /jffs/blarm/scripts/pihole_failover.sh #pihole_failover#
49 9 */7 * * service restart_letsencrypt #LetsEncrypt#
```

This recovers the historical full path/job label, not current boot registration or effective execution. Keep the second expression literal; do not call it an elapsed seven-day timer. The same output reports `logread: can't find syslogd buffer: No such file or directory`. Assistant `/tmp/syslog.log` and local logfile suggestions are unverified. [Captured source and findings](../07-Evidence/ArchivedChatReview.md#dns-director-configuration-s30).
