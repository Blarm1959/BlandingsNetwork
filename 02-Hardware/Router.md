# ASUS router hardware and recovery leads

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### DDNS and certificates (S7)

Historical proposal: ASUS DDNS `blarm-home.asuscomm.com`; Cloudflare DNS-only CNAMEs `home.blarm.com` and `wg.blarm.com` pointing to it. The user stated an intention to use Let's Encrypt through Merlin's DDNS GUI. This establishes historical intent, not successful deployment or today's settings.

Verify the current provider, hostname, alias records, WireGuard endpoint, certificate setting, covered names and renewal status. Do not promote old assistant claims about certificate/NVRAM behaviour into an operational procedure.
## Confirmed hardware and historical repository leads

ASUS RT-AX86U Pro, Merlin 3006 family, LAN 10.59.0.1, EE Full Fibre900 are confirmed by S1. Exact firmware build, WAN connection details and IPv6 remain unverified. HomeNetwork's router hardware page is empty, but labelled config/JFFS backups exist; see [Backups.md](../05-Disaster-Recovery/Backups.md). Do not restore a backup merely because its directory says stable.
