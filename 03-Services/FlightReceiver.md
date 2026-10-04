# Flight Raspberry Pi and FR24 recovery

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Historical repository evidence (S27)

Architecture overview labels a **Raspberry Pi (FR24)** downstream of the loft Netgear switch. Addressing lists FR24 Raspberry Pi `10.59.60.171`. Reservations/CSV use the fuller name **WDL-RPI3-FLIGHT-01**, MAC `B8:27:EB:9A:DB:C8`, reserved address `10.59.60.171`, no lease in that snapshot. A second name-only MAC `B8:27:EB:CF:8E:9D` has the same name.

This is a candidate match for the user's **WDL-Flight-01** search target. RPI3 is part of the recorded label; exact board/model/interfaces and whether the duplicate represents an old device or another interface are unverified. The FR24 label is evidence of a historical flight-feeder role, not proof of current Flightradar service, ADS-B receiver hardware, antenna, decoder, port 1090, software or feed identity. No ADS-B configuration or deployment source was recovered.

Verify current device identity, MACs, IP/gateway/DNS, garage-to-loft path and numbered ports, hardware/OS, feeder/decoder/services, backup/update method and active/retired status. Preserve sensitive feed credentials outside the documentation. The earlier chat search's no-match result remains valid for retrieved chat portions; repository evidence now fills part of that gap.
