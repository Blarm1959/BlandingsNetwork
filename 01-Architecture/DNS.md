# DNS design, remembered settings and contradictions

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## 3. Candidate exact settings and reconciliation

**REMEMBERED / VERIFY — this table is not an instruction to configure the router.**

| Field / rule | Latest remembered design (S1) | Evidence needed |
|---|---|---|
| DNS Director Global Mode | Router | Current GUI page, enable state and installed firmware build |
| User defined 1 IPv4 | `10.59.20.102` | Current GUI value and relevant script logic |
| Pi-hole exception | No redirect | Exact client/rule entry and address or MAC match |
| Guest SSID DNS | Quad9 | Guest Network Pro DNS fields and effective resolver |
| DHCP DNS Server 1 / Server 2 | UNKNOWN | Current LAN DHCP fields, router-advertisement options and client lease evidence |
| WAN DNS entries / automatic DNS | UNKNOWN | Current WAN GUI fields |

### Contradictions requiring resolution

1. **Pi-hole exception:** S1 remembers No redirect. S4 contains older assistant advice that 3006 Router mode did not need the Pi-hole in the client list. That reply is not a verified firmware fix or a current setting. Preserve S1 as the latest candidate and inspect the live rule; do not remove the exception based on S4.
2. **Failover target:** S4 proposed switching WAN DNS between Pi-hole and public resolvers. S2 mentions `dnsfilter_custom1`; S1 remembers User defined 1. These are different possible mechanisms. Current scripts and GUI values must establish which is active; do not combine them into a new design.
3. **DNS Director OFF:** S2 records a temporary OFF state during the February 2026 migration. The latest remembered design is Router mode. OFF belongs in history until live inspection resolves the exact current state.
4. **Guest resolver addresses:** S1 confirms Quad9 use, but not the exact guest pair. Older scripts used `9.9.9.9` and `149.112.112.112`; the current fallback is `9.9.9.11`. Do not substitute one set for another without evidence.
5. **IPv6:** S2 records removal during earlier work; current router state is UNKNOWN. Do not treat historical removal as a fresh live inspection or add IPv6-specific rules without deliberate re-enablement and testing.
6. **Old topology and VPN:** S5/S6/S8 contain different LAN/Pi-hole/VPN values and VLAN port descriptions. They are superseded historical context, not alternate current configurations.
## HomeNetwork DNS design conflict (S27)

The older DNS page specifies WAN Quad9 `9.9.9.11` and `149.112.112.11`, automatic DNS disabled; DHCP DNS1 `10.59.20.102`, DNS2 `10.59.0.1`, additional router advertisement disabled; DNS Director enabled with Global **User Defined 1**, custom1 Pi-hole, custom2 `9.9.9.11`, and guest redirection User Defined 2. It explicitly avoids Router mode. This conflicts with S1's latest remembered **Global Router** design. Preserve both candidates and inspect the current GUI; the older page's operational claim does not settle this.

The dated NVRAM export has custom1 `10.59.20.102`, custom2 `9.9.9.11`, a blank `dnsfilter_enable`, and rule string `<>BC:24:11:B3:11:2B>0`. That MAC belongs to a name-only old Pi-hole label rather than the reserved Pi-hole MAC. Blank fields do not prove enabled or disabled mode, and the rule string is not a verified current exception.

Recovered failover source changes `dnsfilter_custom1`, not WAN DNS, but its copied common_vars uses `10.83.59.102`. See [RouterScripts.md](RouterScripts.md) for source behaviour and implementation limits. No script deployment or GUI change is authorised by this recovery.
