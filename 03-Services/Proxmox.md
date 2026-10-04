# Proxmox host and containers

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

Confirmed: Proxmox PVE host with LXCs at `10.59.60.99` (S1). S27 identifies the machine as **Dell Optiplex 3040M**, hostname/label **pve-01**, MAC `18:66:DA:42:A6:AD`. These are recovered historical details needing current confirmation.

S27 overview lists Pi-hole/Unbound, Podman Home Assistant, Emby, Navidrome, Audiobookshelf, Dispatcharr and Photostidy; CCTV is explicitly planned. Export reservations provide HA .101, Navidrome .103, Audiobookshelf .104, Emby .122, Emby-IPTV .123 and Dispatcharr .129 in 10.59.60.x. No CTIDs, versions or live service states follow from those suffixes. Name-only Plex, OpenHAB, Wireguard, Caddy and HAOS do not prove deployment or retirement.

The older overview claims gateway/DNS migration and NAS NFS remounts completed, without underlying logs. Verify bridges, storage/mounts, startup order, config backups and current service inventory. S14 records backup blocked by config locked (mounted); actual CTID and resolution remain unknown. Example ID123 is not inventory.
