# Other implementation and integrity history

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### Old script/package integrity (S5/S6/S8)

S5 names an old seven-file set: `nvram_setup_vars`, `nvram_setup.sh`, `nvram_dhcp_res`, `nvram_firewall.add`, `nvram_pihole_updown.sh`, `nvram_pihole_failover.sh` under `asus_merlin/3006/`, plus `firewall-start` under the system hook directory. This is a historical inventory only.

The user reported empty packages and packages whose comments/formatting differed from locked copies. S6 includes assistant-reported unused variables, but the uploaded files are unavailable for independent checking. S8's earlier lock-in does not make that design current.

Preserve actual live files and any original locked copies byte-for-byte. Record hashes and compare archive contents before calling them a backup. Regenerated chat code is not a recovered original. Expired sandbox download links and missing uploaded contents were not recovered in this review. Do not reconstruct deployment scripts from truncated replies.

### Other infrastructure recovery leads (S9/S14/S20)

- S9 names printed `GarageSwitch` diagrams, including A4/A5/A6/A7 and combined/rotated PDF variants. The returned turns contain no port assignments or diagram bytes. Recover an original diagram before claiming the physical map is preserved.
- S14 records an LXC backup blocked by `config locked (mounted)`. The returned advice suggested investigating mounts before clearing a stale lock, but no actual CTID, fix or successful backup was returned. The example ID 123 is not a known container. Retain the incident and recover its outcome; do not run old unlock advice automatically.
- S20 records a printer factory reset changing its cloud ePrint identity and a user report that re-enrolment seemed complete. `HP Envy Photo 6230` is an assistant-supplied model candidate; `192.168.52.45` is explicitly an example IP. Printer hostname/MAC/address, actual model and local printing setup remain unknown. Cloud identifiers are not LAN hostnames; current identifiers should be held in the user's private inventory if needed.
