# Heatmiser NeoHub and automation

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

### NeoHub, automation and zones (S13/S22)

S13 contains user logs showing openHAB NeoHub socket traffic and device discovery on 25 November 2025. Thing identifier `neohub:neohub:192_168_1_172` is historical naming evidence; it does not by itself prove the configured socket address. S22 later recalls `10.0.7.172` only in assistant text. Both are historical and must not replace the released-record address `10.59.60.172`.

The assistant interpreted September 2026 screenshots as **neoHub Gen 2, firmware 2218** (S22). The images were not available in this audit, so retain this as a candidate model/build pending verification. An earlier assistant summary also describes Gen 2 with Legacy API enabled (S13).

User logs expose these historical Neo device names: `1st_Floor_Rads`, `Lounge`, `Dining`, `Snug`, `Utility`, `Kitchen`, `Hall_and_WC`, `Hot_Water`, `EnSuite`, `Bathroom`. They are zone names, not independently addressed LAN hosts. Item prefixes in user code include `Rads1F`, `HallWC`, `HW` and the matching room names, with `_Temp`, `_Setpoint` and `_TPS` items. Preserve the distinction between Thing IDs, Item names, zone names and hostnames.

The assistant summary describes a custom openHAB binding adding `timeClockMode`, `awayMode` and `holidayMode`, publishing UNDEF for meaningless hot-water/time-clock temperatures, built using Maven/Java 21 and deployed to `/usr/share/openhab/addons/`. This is a recovery lead, not a preserved build. Capture the source revision, exact JAR, openHAB version, Items/Things/rules and current deployment before declaring it recoverable.

**Recorded failure:** user logs show `Could not cast UNDEF to ... QuantityType` in `heatmiser_summary.rules`, followed by `Parse Error in heatmiser_summary` after attempted replacements. A later assistant summary claims resolution, but no returned user log/test confirms the final fix. Preserve the failure and verify the working rule; do not deploy an old generated replacement automatically.

S22 describes Home Assistant integration, whereas S13 directly evidences openHAB. Whether both were used, whether there was a migration, and what remains current are UNKNOWN. The neoFlo/G3/RF Switch V2 discussion records contemplated purchases/upgrades only; no installation was confirmed. This audit does not validate compatibility or wiring advice.
## HomeNetwork evidence (S27)

Historical NeoHub label `Neo-hub`, MAC `FC:0F:E7:39:BB:EC`, reserved and leased `10.59.60.172` in the snapshot. Overview shows it wired from the garage switch. Model/build/API mode and actual garage port remain unverified; the dedicated heating page is empty. Podman Home Assistant .101 and a name-only OpenHAB LXC both appear; this does not decide which currently controls heating or establish that they are mutually exclusive.
