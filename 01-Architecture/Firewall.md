# Firewall policy history and current limits

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Confirmed design

Flat LAN, no main-LAN VLANs. The rejected VLAN decision remains locked unless the user asks or a material firmware/hardware change addresses its limitation. No currently effective isolation or MAC allowlist has been verified by this review.

## Historical policy generations in HomeNetwork (S27)

The root README claims a wired MAC allowlist and third-octet behaviour bits. The newer firewall specification instead proposes readable zones: DNS20, media40, infrastructure60, trusted120, IOTM210, cloud IoT230 and unknown 250. Trusted initiates control, IoT/unknown should have DNS/WAN only, IOTM should additionally reach media, and vulnerable groups >=200 should otherwise default-deny. The architecture overview calls this a next phase, while the policy document describes intended containment as if enforced. Neither is live rule evidence.

The copied `net-policy-apply.sh` is VLAN-aware, uses a different 10.83/multiple-subnet generation, and is visibly incomplete: commands precede helper definitions and a stray `;;` appears before the phase 4 branch. `firewall-start` would invoke it using stored phase 1–6. Do not deploy it or equate its presence/state file with effective enforcement. Phase descriptions progress from hooks, permissive DNS/WAN and probe logging to blocking and hardening; preserve those as experiment intent.

Read-only recovery requirements: current hook files, `iptables`/bridge rule exports, actual interfaces, counters and relevant logs, with user-confirmed behaviour. Do not claim the same-LAN device isolation goals were achieved merely from address groups or policy prose. No new segmentation design is proposed here.

## Home LAN Revisit discussion handoff (S29)

The user explicitly wanted a separate chat to decide how to handle IoT and whether to use three-bit logic. The supplied starter offers dedicated140 grouping, bit-based policy or a hybrid; it ends with designing before writing rules. This establishes future discussion, not working isolation or a tested/rejected three-bit decision. Keep the confirmed flat LAN and IoT140 baseline. Address grouping alone does not demonstrate effective isolation. [Captured evidence and limits](../07-Evidence/HomeLANRevisit.md).

## Historical user brief and proposed bit policy (S31)

The user starter on 17 February 2026 confirms the historical stable flat10.59 network and states VLANs were too unstable on ASUS; it calls three-bit segmentation **planned**. Proposed bits: bit0 cross-group access, bit1 Pi-hole, bit2 media, with infrastructure below100. The same starter reports DNS Director temporarily OFF and backups completed, without backup scope/restore output.

Assistant log-only/NG_LAN_SEG/ipset/bridge-netfilter code has no returned deployment or test result. It includes approximate /17, placeholder /22 and imprecise /16 source-range handling; downstream switch traffic traversal is unverified. Preserve it as an untested proposal, not working isolation. [Detailed review](../07-Evidence/ArchivedChatReview.md#firewall-segmentation-design-s31).
