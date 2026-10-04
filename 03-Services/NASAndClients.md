# Synology NAS, clients and naming

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### NAS, laptops and backup/name candidates (S10/S11/S23/S24)

- **HISTORICAL USER EVIDENCE:** two laptops running Windows 11 Pro (S10); user changed a laptop screen timeout to 15 minutes. Sleep/hibernate Never was discussed, but the returned evidence does not prove the actual power plan, RDP enable state, successful connection or laptop names.
- **HISTORICAL USER EVIDENCE:** Synology Drive Client on a laptop (S11). Task direction, source/target folders, NAS endpoint and retention remain unknown; do not assume two-way sync or backup is configured.
- **HISTORICAL USER RECOLLECTION:** ABAAS may exist in Restic backups from earlier years (S23). Repository location, snapshot IDs, backup scripts, retention and restore outcome were not recovered.
- **CANDIDATE NAME:** `INV-NAS-012` appears only in conditional assistant advice in S23. It is not a confirmed name for the Synology at `10.59.40.131`, and must not be mapped to it without evidence.
- **HISTORICAL ARTIFACT NAME:** `INV-IONOS-01` appears as a chat and VHDX/split-download name (S24). User confirms split parts reached OneDrive. The assistant describes an 83 GB VHDX, ten split parts, `INV-IONOS-01-Hyper-V-Setup.pdf` and `Join-INV-IONOS-01.zip`; files were not inspected. This does not establish a live home host or IP.
- **EXCLUDE FROM CONFIRMED INVENTORY:** `INV-LAP-01`, `192.168.1.120`, `.150` and `.132` in S10 are explicitly assistant examples. Later S25/S26 summaries use `INV-LAP-01` as a specific Laptop 1 candidate, but no returned user evidence verifies that mapping. Preserve the later candidate separately; do not assign the example IPs to either laptop.
## HomeNetwork evidence (S27)

Historical NAS label `Synology_NAS`, MAC `00:11:32:2B:6A:AF`, address `10.59.40.131`, shown in the loft. NFS shares are documented as used by PVE/LXCs, with remounts claimed working in the older overview. Actual NAS model, share/export names, permissions, mount options and restore evidence remain unknown.

Repository-backed laptop candidates: INV-LAP-01-LAN 10.59.120.51 and INV-LAP-01-WiFi 10.59.120.52; historical lease name INV-LAP-01 on LAN. DKL-01 is reserved .56. These strengthen the name/address evidence beyond earlier examples, without changing confirmed current inventory. See the full device export for printers, powerline TL-WPA4220, TVs, phones and other labels. The HP6230 label/reservation is stronger than the prior assistant model suggestion but remains a historical friendly label.
