# Media services, storage and failed experiments

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### Media services and implementation history (S15–S19/S21)

HISTORICAL workflow in the assistant summary (S16): Dispatcharr PostgreSQL VOD data feeds STRM exports for Emby through shared Proxmox/LXC storage. Named files include `vod_export_vars.sh` and `vod_export_reset.sh`; proposed schedules are exporter 02:00 and Emby refresh 04:00. No live cron output, timezone or script files were recovered. Host `/mnt/pve/Share-VOD` and container `/mnt/Share-VOD/{XC_NAME}/` both appear; exact mount mappings and ownership remain unverified.

The user reports a Movies scan became faster up to 90% and then stalled again (S16). Metadata/artwork was the assistant's diagnosis, not a verified root cause or successful fix. Preserve this as an unresolved experiment; do not record the suggested Emby settings as current.

S15 contains user-supplied installer helpers for PostgreSQL, source deployment, Node.js and uv. S18 discusses Nginx, Gunicorn, Celery, Celery Beat, Daphne and PostgreSQL, but it does not establish which services currently run or their ports/IPs. S17's `DDD`/`UUU`/`PPP` are provider placeholders, not local DNS or computer names.

S21 preserves a user correction: missing persistent folders belong under `/data`, not `/opt/dispatcharr/data`; `/opt/dispatcharr/app/*` is the application path in that discussion. Reported missing directories: `/data/logos`, `/data/recordings`, `/data/uploads/m3us`, `/data/uploads/epgs`, `/data/m3us`, `/data/epgs`, `/data/plugins`, `/data/db`, plus `$APP_DIR/logo_cache` and `$APP_DIR/media`. The proposed libpcre3 removal/test and directory fixes have no returned completion evidence. Do not turn old package-availability claims into current Debian guidance.

S19 preserves the user's final helper requirement: `cddocker.sh` should print only the directory so the calling shell can change directory. Earlier generated variants tried to cd inside a child script and are superseded by that requirement. Deployment and installed location are unknown; keep this as development history rather than a live service.
## HomeNetwork evidence (S27)

Historical HDHomeRun label `HDHR-126172A6` at 10.59.60.121; Emby .122, Emby-IPTV .123, Dispatcharr .129. Navidrome .103 and Audiobookshelf .104 also appear. Photostidy is listed in overview only, and Plex is name-only. Future CCTV is planned. Verify actual running services, versions, host/container IDs, mounts, exports, schedules and backup dependencies; no port or state follows from a label.
