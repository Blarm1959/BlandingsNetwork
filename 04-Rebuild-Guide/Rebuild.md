# Rebuild guide and prerequisites

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Status: procedure outline awaiting verification

HomeNetwork's five rebuild pages are empty; its apply script is incompatible with the copied variables and older addressing. This record therefore does not assert a tested factory-reset or automated rebuild procedure.

Before any rebuild: preserve current router configuration/JFFS and local access details; verify exact hardware/build, approved baseline, private backup availability and rollback route. The expected dependency order to document and test is router/WAN and LAN access; switch/cabling and DHCP; Proxmox/NAS access; Pi-hole/Unbound and router DNS/failover; guest/WireGuard access; dependent heating/media services. Exact steps and validations require user confirmation and a deliberate test window.

Record desired values from [the master overview](../BlandingsNetwork.md), not from historical source scripts. Keep firmware-specific restore constraints and private credentials outside public Markdown. Completion requires documented checks and successful user-confirmed restoration; see [Verification.md](../07-Evidence/Verification.md), V9/V10/V20. No reset, restore, reservation import or policy application was performed in this review.
