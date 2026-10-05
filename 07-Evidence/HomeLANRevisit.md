# Home LAN Revisit — recovered visible chat text (S29)

[Master overview](../BlandingsNetwork.md) · [Source register](Sources.md)

## Capture and limits

The user identifies this as **Home LAN Revisit** and supplied a Ctrl-A/Ctrl-C copy on 5 October 2026. The [unaltered pasted text](HomeLANRevisit-Pasted.txt) is preserved alongside this review: 31,175 bytes; SHA256 `c9bb3572fb8a2e9bc3d883aae337da77661ae907bd7bd364005fc6b28553ebd1`.

The text starts “Loading older messages…”. This is a capture of visible text, not evidence of the whole conversation. Original message dates, structured speaker labels and original attachments are absent. User requests and assistant replies are distinguished from context; standalone lines near the end cannot be reliably attributed. Referenced attachment names do not recover their contents. Do not treat “all systems working” text as direct user confirmation.

## Useful recovered details

| Topic | Evidence and treatment |
|---|---|
| Router diagnostic export | User requests `router_nvram_show.sh`, a script-relative `output` folder, labelled NVRAM text and a CSV combining reservations, names/MACs/IPs and unreserved connections. User explicitly does not want Python installed on the router. Assistant adds `router_lists_raw.txt` as the third output. Preserve as historical requirements. |
| Script generations | An initial BusyBox shell/awk proposal is visible. User later says a fully developed script was created in another chat and attached with outputs. Those attachments are absent from this capture; the initial proposal is not the final script. S27 supplies separate historical source evidence. |
| DNS document | User supplied `04-dns-and-pihole.md` for reference and explicitly asked not to change it in that historical task. Its content is absent here; it cannot establish exact DNS Director fields. |
| Migration/topology | Assistant drafts describe 192.168.1.0/24 to 10.59.0.0/16, garage TP-Link feeding room Cat6 and loft Netgear GS308E, NAS/PVE/FR24 in the loft, and wired neoHub. These largely overlap S27. No new port numbering is present. |
| Addressing and inventory | Drafts use IoT140 and repeat the 10.59 reservations, including unnamed .100, WDL-RPI3-FLIGHT-01 .171 and neoHub .172. They corroborate an earlier 140 generation, without resolving S27's later210/230 conflict. No new current device or CTID is established. |
| Wi-Fi | Assistant drafts name ASUS-BT and ASUS-BT-G2, both bands, one guest network and claimed guest isolation. These remain historical candidates requiring current GUI/behaviour evidence. |
| NAS/services | Draft claims NFS use, remounts working, updated LXC gateways/DNS, DNS stability and 900+Mbps performance. No command output or direct user test confirmation accompanies these claims. Preserve as recovery leads, not test results. |
| IoT next phase | User explicitly asks to start another chat to decide whether/how to separate IoT or use three-bit logic. Assistant offers options and says to design before writing rules. This is discussion intent, not an implemented policy or a rejected/tested three-bit design. |

## DNS Director reminder tail

The final portion repeats conditional reminders to re-enable DNS Director, then unconditional working-state claims, later inability-to-verify statements and advice to keep it disabled. It ends with an automation-paused notice. The capture does not establish message roles, dates, actual router changes or current automation state for that tail.

Public search results concerning unrelated 10.59 addresses cannot establish this private network's status. None of these reminders resolves the OFF/ON contradiction or supersedes S1's remembered Global Router design. Record exact GUI fields and effective DNS behaviour under V1/V4 before declaring them authoritative. No automation or network setting was changed during this recovery.

## CSV interpretation safeguard

The draft calls status O “offline” and status Y “online and correct”. A lease snapshot cannot establish reachability: O only means reservation without a matching observed lease; Y means reservation and observed lease IP match. Static-addressed devices or other lease-file limitations can explain missing leases. Use the narrower definitions already in [DeviceInventory.md](../01-Architecture/DeviceInventory.md).

## Retirement status

This supplied capture is preserved and reviewed; the whole chat is not cleared for deletion. Earlier messages, original final script/outputs and the referenced DNS attachment remain missing. V15 stays open. Preserve the separately started IoT discussion if it contains unique decisions or tests.
