# Recovered device names, reservations and MACs

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Historical router export (S27) — not current configuration

All rows below are preserved from `router/jffs/blarm/scripts/output/router_dhcp.csv` in the reviewed HomeNetwork commit. The adjacent NVRAM output is timestamped 21 February 2026, 23:20:13 UTC; the CSV itself has no independent date. Names may be friendly labels rather than DNS hostnames. Blank fields remain unknown; `*` is an unresolved lease name. No row establishes a Proxmox CTID, room, physical port or present-day activity.

`Y`: reservation and lease match; `N`: reservation/lease mismatch; `O`: reservation without lease; `R`: lease without reservation; `X`: name-only. These describe the historical export, not today's devices.

| Code | Name/label in export | MAC | Reserved address | Lease address in snapshot |
|---|---|---|---|---|
| O | pve-01_LXC_PiHole | `BC:24:11:91:31:0A` | 10.59.20.102 | — |
| O | Synology_NAS | `00:11:32:2B:6A:AF` | 10.59.40.131 | — |
| Y | HP_Printer-6230 | `80:CE:62:74:94:AE` | 10.59.60.11 | 10.59.60.11 |
| O | pve-01 | `18:66:DA:42:A6:AD` | 10.59.60.99 | — |
| O | UNKNOWN | `BC:24:11:F3:4E:3F` | 10.59.60.100 | — |
| O | pve-01_LXC_Podman-HomeAssistant | `BC:24:11:E3:83:6A` | 10.59.60.101 | — |
| O | pve-01_LXC_Navidrome | `BC:24:11:5F:8E:1C` | 10.59.60.103 | — |
| O | pve-01_LXC_Audiobookshelf | `BC:24:11:A0:77:E1` | 10.59.60.104 | — |
| Y | HDHR-126172A6 | `00:18:DD:26:17:2A` | 10.59.60.121 | 10.59.60.121 |
| O | pve-01_LXC_Emby | `BC:24:11:33:DD:CE` | 10.59.60.122 | — |
| O | pve-01_LXC_Emby-IPTV | `BC:24:11:00:A5:5C` | 10.59.60.123 | — |
| O | pve-0_LXC_Dispatcharr | `BC:24:11:98:5F:47` | 10.59.60.129 | — |
| O | TP-Link_TL-SG1218MPE | `9C:A2:F4:71:70:41` | 10.59.60.136 | — |
| O | WDL-RPI3-FLIGHT-01 | `B8:27:EB:9A:DB:C8` | 10.59.60.171 | — |
| Y | Neo-hub | `FC:0F:E7:39:BB:EC` | 10.59.60.172 | 10.59.60.172 |
| Y | INV-LAP-01-LAN | `B0:5C:DA:85:86:E7` | 10.59.120.51 | 10.59.120.51 |
| O | INV-LAP-01-WiFi | `CC:F9:E4:CA:BA:CA` | 10.59.120.52 | — |
| Y | DKL-01 | `00:A5:54:DD:4F:19` | 10.59.120.56 | 10.59.120.56 |
| O | Amazon_FireStick | `0C:43:F9:A1:13:47` | 10.59.230.20 | — |
| O | Samsung_TV_LED_22 | `BC:14:85:2A:62:51` | 10.59.230.21 | — |
| Y | LG_TV_OLED_48_LAN | `58:96:0A:15:AB:98` | 10.59.230.23 | 10.59.230.23 |
| Y | LG_TV_OLED_48_WiFi | `E0:85:4D:41:DC:7E` | 10.59.230.24 | 10.59.230.24 |
| Y | Ring_LLC | `90:48:6C:ED:5E:9E` | 10.59.230.173 | 10.59.230.173 |
| R | Echo_Dot_Bedroom | `00:F3:61:9A:D9:8C` | — | 10.59.250.202 |
| R | Galaxy-A13 | `4E:55:EB:F5:79:E1` | — | 10.59.250.216 |
| R | * | `6C:55:B1:A5:2B:5F` | — | 10.59.250.220 |
| R | Debra-s-S23 | `66:8A:70:AE:9D:10` | — | 10.59.250.226 |
| R | Bill-s-S23 | `BE:0C:5B:E2:E2:0C` | — | 10.59.250.228 |
| R | iPhone | `0E:9A:B4:61:C5:88` | — | 10.59.250.231 |
| R | Echo_Snug | `FC:A1:83:15:79:89` | — | 10.59.250.234 |
| R | Echo_Dot_Kitchen | `00:F3:61:54:28:2F` | — | 10.59.250.236 |
| R | * | `50:99:5A:45:CF:B9` | — | 10.59.250.237 |
| R | Echo_Dot_Study | `00:71:47:B4:66:84` | — | 10.59.250.239 |
| R | Samsung | `C0:48:E6:4E:32:D2` | — | 10.59.250.240 |
| R | OCTO-CADLITE | `38:18:2B:B5:B1:D0` | — | 10.59.250.242 |
| X | pve-01_VM_HAOS | `02:C4:FC:24:F4:41` | — | — |
| X | DKL_Work_Laptop | `08:D2:3E:59:72:16` | — | — |
| X | DKL-S7 | `2C:0E:3D:90:C1:9B` | — | — |
| X | Bill-s-S23 | `5A:74:FF:87:FB:8A` | — | — |
| X | Matts | `60:A5:E2:BD:E0:98` | — | — |
| X | Amazon | `74:C2:46:3F:3E:8F` | — | — |
| X | TL-WPA4220 | `84:D8:1B:21:0D:2E` | — | — |
| X | DKL-Work-J5 | `88:75:98:7D:43:45` | — | — |
| X | HUMAX_DTRT4000_BT_YouView | `A0:72:2C:A0:76:89` | — | — |
| X | WDL-RPI3-PI-HOLE | `B8:27:EB:98:E2:C4` | — | — |
| X | WDL-RPI3-FLIGHT-01 | `B8:27:EB:CF:8E:9D` | — | — |
| X | DKL-Tab-S6 | `BA:04:0C:68:BB:66` | — | — |
| X | pve-01_LXC_Plex | `BC:24:11:34:21:6F` | — | — |
| X | pve-01_LXC_OpenHAB | `BC:24:11:6A:B6:83` | — | — |
| X | pve-01_LXC_PiHole | `BC:24:11:B3:11:2B` | — | — |
| X | pve-01_LXC_Wireguard | `BC:24:11:B3:BA:3E` | — | — |
| X | pve-01_LXC_Caddy | `BC:24:11:E8:B3:B4` | — | — |
| X | WDL-S10e | `C2:03:93:C8:16:FB` | — | — |
| X | Samsung_TV_43 | `CC:6E:A4:C6:24:0C` | — | — |

## Conflicts and interpretation

- `WDL-RPI3-FLIGHT-01` appears at reserved `10.59.60.171` with MAC `B8:27:EB:9A:DB:C8`, and separately as name-only MAC `B8:27:EB:CF:8E:9D`. Do not infer wired/Wi-Fi interfaces, replacement hardware or current identity. It is a candidate match for the user's abbreviated WDL-Flight-01.
- `pve-01_LXC_PiHole` also has a different name-only MAC from the current-baseline reservation; `WDL-RPI3-PI-HOLE` is a separate older label. These do not move the confirmed Pi-hole service out of its LXC.
- `pve-0_LXC_Dispatcharr` is preserved exactly, including its apparent `pve-0` typo. IP suffixes are not container IDs.
- HP printer `10.59.60.11`, INV-LAP-01 LAN/Wi-Fi `10.59.120.51/.52`, and other labels are now repository-backed historical candidates, stronger than prior assistant examples but still unverified current settings.
- IoT `230.x` reservations conflict with the supplied `140.x` logical group. The Samsung TV and LG Wi-Fi status codes differ between the prose reservation table and CSV; preserve the CSV snapshot and verify live state.
- An unnamed reserved `10.59.60.100` needs identification. Name-only Plex, OpenHAB, Wireguard, Caddy and HAOS entries establish labels only, not deployed or retired services.
