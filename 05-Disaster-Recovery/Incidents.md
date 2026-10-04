# Incident records and diagnostic evidence

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

HomeNetwork's internet-down, DNS-issues, Pi-hole-down, router-failure and locked-out playbooks are empty. The following are evidence-collection outlines, not tested fixes.

| Symptom | Evidence to collect before deciding on a change |
|---|---|
| Internet down | Router reachability, WAN/link state, ISP status and whether DNS versus connectivity is failing. |
| DNS issues/Pi-hole down | Current GUI DNS fields, Pi-hole/Unbound service state, direct DNS results, historical-script status versus actual resolver key and client behaviour. |
| Router failure/locked out | Physical access/link, current management address, verified backup/build and a user-agreed recovery/rollback path. |
| PVE backup locked mounted | Actual CTID/task/mount state and backup logs; earlier incident has no recovered successful resolution. |
| Emby scan stalls | Actual library paths/mounts, permissions and logs; old metadata diagnosis was not verified. |

Preserve observed results and decisions. Do not execute an old unlock, factory reset, policy script or DNS switch merely because it was suggested in historical material. Relevant implementation/history lives in the architecture and service pages; V4/V10 specify the user-confirmed validation needed.
