# BlandingsNetwork

**Authoritative master record for the Blandings home network**

Version target: **v1.0.1**

This file is intended to be the single current reference for the Blandings home network.  
Where an older design conflicts with a later tested design, the later confirmed design wins.

> **Important:** Do not replace a confirmed design with a theoretically preferable alternative unless new evidence, firmware, hardware, or an explicit decision justifies reopening it.

---

## 1. Current confirmed architecture

### Internet and router
- ISP: **EE Full Fibre 900**
- Router: **ASUS RT-AX86U Pro**
- Firmware: **Asuswrt-Merlin 3006**
- Router LAN address: **10.59.0.1**
- Main LAN: **10.59.0.0/16**
- Network design: **flat LAN; no VLANs**

The flat LAN is deliberate. VLAN-based designs were tested and rejected because the ASUS/Merlin implementation did not prove sufficiently usable/stable for this network.

### DHCP
- DHCP pool: **10.59.250.201 – 10.59.250.250**

### Logical address groups
The LAN remains a single `/16`, but devices are grouped by third octet for clarity.

| Purpose | Range / address |
|---|---|
| Infrastructure | `10.59.60.x` |
| Trusted devices | `10.59.120.x` |
| IoT | `10.59.140.x` |
| Pi-hole LXC | `10.59.20.102` |
| Synology NAS | `10.59.40.131` |
| Proxmox host | `10.59.60.99` |
| TP-Link switch | `10.59.60.136` |
| Heatmiser NeoHub | `10.59.60.172` |

### Guest network
- ASUS Guest Network Pro subnet: **10.52.0.0/24**
- Guest network is separate from the main `10.59.0.0/16` LAN.
- Guests must **not** depend on the Blandings Pi-hole.
- Guest DNS uses public DNS (Quad9 design).

### DNS
- Pi-hole + Unbound LXC: **10.59.20.102**
- Public fallback family used in the design: **Quad9**
- Confirmed public resolver used as a fallback in the later design: **9.9.9.11**

There have been multiple DNS Director configurations during development.  
The final DNS Director state should be rechecked against the live router before this section is promoted to an exact-settings reference.

### WireGuard
- Router WireGuard network: **10.6.0.0/24**
- Router tunnel address: **10.6.0.1/24**
- UDP port: **443**
- Split tunnel design
- Main LAN route: **10.59.0.0/16**
- Current design should not create an unnecessary dependency on Pi-hole for basic WireGuard connectivity.

---

## 2. Pi-hole and Merlin automation

### Pi-hole
- Pi-hole runs in an LXC at **10.59.20.102**
- Unbound is used locally with Pi-hole.

### Merlin script paths
Current known script layout:

```text
/jffs/blarm/common/common_vars
/jffs/blarm/scripts/pihole_failover.sh
/jffs/blarm/scripts/pihole_status.sh
/jffs/blarm/scripts/pihole_updown.sh
/jffs/blarm/state
```

### Pi-hole failover cron
Known schedule:

```cron
*/15 * * * * /jffs/blarm/scripts/pihole_failover.sh
```

The failover design has used the Merlin DNS Director/NVRAM setting:

```text
dnsfilter_custom1
```

Exact current behaviour and values should be copied from the live router before being treated as immutable documentation.

---

## 3. Physical / infrastructure components

Known core components:

- ASUS RT-AX86U Pro router
- TP-Link TL-SG1218MPE PoE switch
- Proxmox PVE host
- Pi-hole + Unbound LXC
- Synology NAS
- Heatmiser NeoHub
- Samsung S23 and other trusted client devices

---

## 4. Tested and rejected

### 4.1 ASUS VLAN design
**Status: REJECTED**

**Goal:**  
Segment infrastructure, trusted devices and IoT devices into separate VLANs.

**Result:**  
The VLAN approach was tested thoroughly with the ASUS/Merlin environment and proved unsuitable/unreliable for the Blandings network.

**Current decision:**  
Remain on the flat `10.59.0.0/16` LAN and use logical IP grouping instead.

**Do not recommend again unless:**  
There is a material firmware/hardware change or the user explicitly asks to reopen VLAN testing.

---

### 4.2 Older 192.168.x.x LAN designs
**Status: SUPERSEDED**

Earlier network designs used `192.168.x.x` addressing.

**Current decision:**  
These are obsolete. The authoritative main LAN is now:

```text
10.59.0.0/16
```

---

### 4.3 Earlier guest-DNS interception designs
**Status: SUPERSEDED / PARTLY REJECTED**

Earlier experiments used custom `iptables` DNAT/forwarding rules to intercept guest DNS traffic and force public Quad9 resolvers.

These experiments are historical and should not be recreated automatically.  
The current Guest Network Pro configuration is the preferred basis for the guest network.

---

### 4.4 Earlier DNS Director OFF state
**Status: HISTORICAL / REQUIRES FINAL RECONCILIATION**

At one stage of the February 2026 migration, DNS Director was deliberately OFF while the new `10.59.0.0/16` network was stabilised.

Later work reintroduced DNS Director / Pi-hole failover concepts.

Before documenting the exact current DNS Director drop-down settings, verify them from the live ASUS configuration rather than assuming an older screenshot or chat is still current.

---

### 4.5 IPv6
**Status: REMOVED FROM AN EARLIER DESIGN**

IPv6 was explicitly removed during earlier firewall/DNS work.

Do not reintroduce IPv6-specific firewall or DNS-bypass rules unless IPv6 has subsequently been deliberately re-enabled and tested.

---

## 5. Superseded designs

These may have been valid at the time but are not the current Blandings design:

- old `192.168.x.x` addressing
- VLAN segmentation attempts
- early guest DNS DNAT/interception scripts
- transitional DNS Director OFF configuration during the `10.59` migration
- older Pi-hole addresses from pre-`10.59` designs
- any WireGuard design tied unnecessarily to the Pi-hole service

Git history and old chats may contain these configurations; they must not override the current master configuration.

---

## 6. Items still to verify from live equipment / old chats

These should be completed before BlandingsNetwork is considered a complete disaster-recovery reference:

- exact current ASUS WAN settings
- exact current DNS Director mode and entries
- exact DHCP DNS Server 1 / Server 2 settings
- current WAN Quad9 entries
- DDNS provider, hostname and settings
- exact Guest Network Pro DNS fields
- exact firewall rules still in use
- current IPv6 setting
- current Dual-WAN/failover state
- current WireGuard peer settings
- current Merlin script contents
- current `cru l` output
- router backup/export procedure
- Pi-hole backup/restore procedure
- Proxmox/LXC DNS settings
- switch management configuration
- any reserved/static DHCP assignments that should be documented

---

## 7. Rules for future changes

1. **GitHub is the authoritative long-term record.**
2. This chat or a future chat may investigate changes, but a setting is not promoted to the master configuration until it is confirmed working.
3. Failed experiments belong under **Tested and rejected**.
4. Replaced-but-valid designs belong under **Superseded**.
5. Do not remove a failed-design note if doing so could cause the same dead end to be suggested again.
6. For major network changes, record:
   - what changed,
   - why,
   - how it was tested,
   - whether rollback was required.
7. Use the normal **Change Package → PSTP Release** workflow for repo updates.

---

## 8. Future-chat starter

Use the following when starting a fresh BlandingsNetwork chat:

```text
BlandingsNetwork – continue from the master configuration.

Repository:
Blarm1959/BlandingsNetwork

Read BlandingsNetwork.md before making recommendations.

Treat the Current confirmed architecture as authoritative.

Important:
- Do not reopen items under Tested and rejected unless I explicitly ask or there has been a relevant firmware/hardware change.
- Distinguish experiments from confirmed changes.
- Only promote a change into the master configuration after I confirm it works.
- Use the normal PSTP Change Package workflow for repo changes.
```

---

## 9. Release history

### v1.0.1
Initial BlandingsNetwork master documentation:
- established current core network architecture
- recorded key IP addressing
- documented Guest Network Pro, Pi-hole/Unbound and WireGuard baseline
- recorded VLANs as a tested and rejected design
- separated superseded designs from current configuration
- added a verification list for settings that still need to be reconciled from live equipment and older chats
