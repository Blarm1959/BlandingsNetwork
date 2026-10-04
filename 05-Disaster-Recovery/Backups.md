# Backup evidence and restore readiness

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Historical router backups recovered (S27)

HomeNetwork contains these labelled directories, each with Settings_RT-AX86U Pro.CFG and backup_jffs_RT-AX86U Pro.tar:

| Directory label | Intended historical generation |
|---|---|
| router/backup/20260216_192 | Earlier192.168 generation; includes nvram_full_backup_pre_10_change.txt |
| router/backup/20260216_10x_stable | Earlier10x generation; includes nvram_full_backup_10x_stable.txt |
| router/backup/20260219_10.59_stable |10.59 generation candidate |
| router/backup/20260222_10.83 |10.83 generation candidate |

Labels and filenames are evidence of stored artifacts, not current authority, integrity, completeness, firmware compatibility or successful restoration. The inspected10.59 JFFS archive member list includes certificate/account keys and SSH host keys; raw archives/NVRAM/config binaries are not copied into this documentation Change Package. Preserve access to the originals privately before retiring HomeNetwork.

Router backup availability does not establish Pi-hole/Unbound, PVE/LXC, NAS or switch backup coverage. Recover those methods and private locations separately. Keep the old Restic lead in NASAndClients.md distinct until mapped to actual protected components.

### Selected non-secret archived-variable comparison

Read-only inspection of `./blarm/common/common_vars` inside the 19 February 10.59 and 22 February 10.83 JFFS archives shows different generations. The 10.59 archive has router `10.59.0.1`, mask `255.255.0.0`, DHCP `10.59.250.201–250`, Pi-hole `10.59.20.102` and fallback `9.9.9.11`. The 10.83 archive has router `10.83.0.1`, DHCP `10.83.99.201–250`, Pi-hole `10.83.59.102` and the same fallback. This corroborates that the root copied common_vars is from the later historical generation, without proving either backup was restored successfully or is current. Only named non-secret keys were reported; archive members were not deployed.

For every backup record: coverage, collection date/build, private location, hash/integrity check, prerequisites, dependency order, restore instructions, rollback, test date/result and user confirmation. This is not yet a complete disaster-recovery reference; V9/V10 stay open.
