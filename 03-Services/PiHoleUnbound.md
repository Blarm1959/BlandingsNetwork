# Pi-hole and Unbound service

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

Confirmed service: Pi-hole + local Unbound LXC at `10.59.20.102` (S1). S27 historical reserved label `pve-01_LXC_PiHole`, MAC `BC:24:11:91:31:0A`. An older name-only LXC MAC and Raspberry Pi label also appear; these are identity/history leads, not a change to the confirmed host.

Unbound listen address/port, configuration, package versions, backup coverage and PVE CTID remain unknown. HomeNetwork's dedicated service page is empty. Router source and DNS conflicts are recorded in [DNS.md](../01-Architecture/DNS.md) and [RouterScripts.md](../01-Architecture/RouterScripts.md). Recover actual Pi-hole export and Unbound configuration; only user-confirmed tests can establish normal, fallback and recovery operation.
