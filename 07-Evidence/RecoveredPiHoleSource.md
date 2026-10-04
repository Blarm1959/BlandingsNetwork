# Recovered Pi-hole router source

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## Historical source copies — reference only

The three Pi-hole script bodies below also match the selected copies inside `20260219_10.59_stable/backup_jffs_RT-AX86U Pro.tar`, after normalising line endings and trailing whitespace. The common_vars body below is the root copied 10.83 generation; selected keys from the archived 10.59 version are recorded separately in [Backups.md](../05-Disaster-Recovery/Backups.md). Matching stored copies corroborates historical source preservation, not current deployment or successful operation.

S27 commit `e70900c801e1056a86e23c50150322d4d01fec2d`. These are the exact decoded source contents, with line endings normalised for Markdown. Do not run or deploy them from this record. common_vars contains superseded 10.83/VLAN constants; source behaviour is documented separately. Live copies must be compared before promotion.

## router/jffs/blarm/common/common_vars

```sh
#!/bin/sh
# /jffs/blarm/common/common_vars
#
# Common variables for Blarm's ASUS-Merlin scripts.
# Source this file from all /jffs/blarm/scripts/*

# -------------------------
# Core network
# -------------------------
ROUTER_IP="10.83.0.1"
ROUTER_NETMASK="255.255.0.0"
ROUTER_DHCP_START="10.83.99.201"
ROUTER_DHCP_END="10.83.99.250"
ROUTER_DHCP_LEASE="86400"

MEDIA_CIDR="10.56.0.0/24"

PIHOLE_IP="10.83.59.102"

# -------------------------
# Pi-hole outage failover (DNS Director User Defined 1)
# -------------------------
# When Pi-hole is DOWN (including full LXC outage), DNS Director "User defined DNS 1 (IPv4)"
# will be set to this public resolver so clients still have DNS.
PIHOLE_OUTAGE_FALLBACK_IP="9.9.9.11"

# Domain to test resolution against via Pi-hole
PIHOLE_FAILOVER_CHECK_DOMAIN="example.com"

# Hysteresis counters for cru cadence (*/15 minutes):
# - FAILS=1  -> switch to fallback after 15 minutes of failure
# - FAILS=2  -> switch to fallback after 30 minutes of failure
# - SUCCESSES=1 -> switch back after 15 minutes of success
PIHOLE_FAILOVER_FAILS="1"
PIHOLE_FAILOVER_SUCCESSES="1"

# Oct3 Bit Flags
BIT_CROSS=1
BIT_PIHOLE=2
BIT_MEDIA=4


# -------------------------
# NG policy zones (VLAN + MAIN)
# -------------------------
MAIN_CIDR="10.83.0.0/16"
INFRA_CIDR="10.83.59.0/24"
TRUSTED_CIDR="10.83.62.0/24"
UNKNOWN_CIDR="10.83.99.0/24"
GUEST_CIDR="10.52.0.0/24"
IOT_CIDR="10.53.0.0/24"
STREAM_CIDR="10.54.0.0/24"
IOTS_CIDR="10.55.0.0/24"
MEDIA_CIDR="10.56.0.0/24"
IOTM_CIDR="10.57.0.0/24"
IOTSM_CIDR="10.58.0.0/24"

# Gateways for VLANs (router IP on each VLAN)
GUEST_GW_IP="10.52.0.1"
IOT_GW_IP="10.53.0.1"
STREAM_GW_IP="10.54.0.1"
IOTS_GW_IP="10.55.0.1"
MEDIA_GW_IP="10.56.0.1"
IOTM_GW_IP="10.57.0.1"
IOTSM_GW_IP="10.58.0.1"

```

## router/jffs/blarm/scripts/pihole_failover.sh

```sh
#!/bin/sh
#
# /jffs/blarm/scripts/pihole_failover.sh
#
# Single-shot Pi-hole health check for use with cru (cron).
# - If Pi-hole is healthy -> set DNS Director UserDefined1 IPv4 to PIHOLE_IP (up)
# - If Pi-hole is unhealthy -> set DNS Director UserDefined1 IPv4 to PIHOLE_OUTAGE_FALLBACK_IP (down)
#
# Recommended cru example (every 15 minutes):
#   cru a pihole_failover "*/15 * * * * /jffs/blarm/scripts/pihole_failover.sh"
#

set -eu

VARS="/jffs/blarm/common/common_vars"
[ -f "$VARS" ] || { echo "ERROR: missing $VARS" >&2; exit 1; }
# shellcheck disable=SC1090
. "$VARS"

: "${PIHOLE_IP:?missing PIHOLE_IP}"
: "${PIHOLE_OUTAGE_FALLBACK_IP:?missing PIHOLE_OUTAGE_FALLBACK_IP}"
: "${PIHOLE_FAILOVER_CHECK_DOMAIN:=example.com}"
: "${PIHOLE_FAILOVER_FAILS:=1}"
: "${PIHOLE_FAILOVER_SUCCESSES:=1}"

STATE_DIR="/jffs/blarm/state"
STATE_FILE="$STATE_DIR/pihole_outage_state"
FAIL_FILE="$STATE_DIR/pihole_outage_fails"
SUCC_FILE="$STATE_DIR/pihole_outage_succ"
mkdir -p "$STATE_DIR"

STATE="$(cat "$STATE_FILE" 2>/dev/null || echo "UP")"
FAILS="$(cat "$FAIL_FILE" 2>/dev/null || echo 0)"
SUCC="$(cat "$SUCC_FILE" 2>/dev/null || echo 0)"

NSLOOKUP_BIN="/usr/bin/nslookup"
NC_BIN="/usr/bin/nc"

pihole_ok() {
  if [ -x "$NSLOOKUP_BIN" ]; then
    "$NSLOOKUP_BIN" "$PIHOLE_FAILOVER_CHECK_DOMAIN" "$PIHOLE_IP" >/dev/null 2>&1
    return $?
  fi

  if [ -x "$NC_BIN" ]; then
    echo | "$NC_BIN" -w 1 -u "$PIHOLE_IP" 53 >/dev/null 2>&1
    return $?
  fi

  return 1
}

switch_up() {
  /jffs/blarm/scripts/pihole_updown.sh up || true
  echo "UP" > "$STATE_FILE"
  echo 0 > "$FAIL_FILE"
  echo 0 > "$SUCC_FILE"
  logger -t pihole_outage "Pi-hole healthy → DNS Director UserDefined1 back to Pi-hole (${PIHOLE_IP})"
}

switch_down() {
  /jffs/blarm/scripts/pihole_updown.sh down || true
  echo "DOWN" > "$STATE_FILE"
  echo 0 > "$FAIL_FILE"
  echo 0 > "$SUCC_FILE"
  logger -t pihole_outage "Pi-hole unhealthy → DNS Director UserDefined1 to fallback (${PIHOLE_OUTAGE_FALLBACK_IP})"
}

if pihole_ok; then
  SUCC=$((SUCC + 1))
  FAILS=0
  echo "$FAILS" > "$FAIL_FILE"
  echo "$SUCC" > "$SUCC_FILE"

  if [ "$STATE" = "DOWN" ] && [ "$SUCC" -ge "$PIHOLE_FAILOVER_SUCCESSES" ]; then
    switch_up
  fi
else
  FAILS=$((FAILS + 1))
  SUCC=0
  echo "$FAILS" > "$FAIL_FILE"
  echo "$SUCC" > "$SUCC_FILE"

  if [ "$STATE" = "UP" ] && [ "$FAILS" -ge "$PIHOLE_FAILOVER_FAILS" ]; then
    switch_down
  fi
fi

exit 0

```

## router/jffs/blarm/scripts/pihole_updown.sh

```sh
#!/bin/sh
#
# /jffs/blarm/scripts/pihole_updown.sh
#
# Purpose:
#   Switch DNS Director "User defined DNS 1 (IPv4)" between:
#     - Pi-hole IP (up)
#     - Fallback public DNS (down) e.g. Quad9
#
# Uses fixed, confirmed NVRAM keys on your Merlin build:
#   dnsfilter_custom1 = User defined DNS 1 (IPv4)
#
# Usage:
#   /jffs/blarm/scripts/pihole_updown.sh {up|down}
#

set -eu

VARS="/jffs/blarm/common/common_vars"
[ -f "$VARS" ] || { echo "ERROR: missing $VARS" >&2; exit 1; }
# shellcheck disable=SC1090
. "$VARS"

: "${PIHOLE_IP:?missing PIHOLE_IP}"
: "${PIHOLE_OUTAGE_FALLBACK_IP:?missing PIHOLE_OUTAGE_FALLBACK_IP}"

MODE="${1:-}"
case "$MODE" in
  up)   WANT="$PIHOLE_IP" ;;
  down) WANT="$PIHOLE_OUTAGE_FALLBACK_IP" ;;
  *)    echo "Usage: $0 {up|down}" >&2; exit 1 ;;
esac

KEY="dnsfilter_custom1"

CUR="$(nvram get "$KEY" 2>/dev/null || true)"

# Normalize whitespace (just in case)
norm() { echo "$1" | tr -s ' ' | sed 's/[[:space:]]\+$//'; }

CUR_N="$(norm "$CUR")"
WANT_N="$(norm "$WANT")"

if [ "$CUR_N" = "$WANT_N" ]; then
  echo "DNS Director $KEY unchanged: '$WANT_N'"
  exit 0
fi

nvram set "$KEY=$WANT_N"
nvram commit

# Best-effort restart of dnsfilter + dnsmasq
if command -v service >/dev/null 2>&1; then
  service restart_dnsfilter >/dev/null 2>&1 || true
  service restart_dnsmasq   >/dev/null 2>&1 || true
fi

logger -t pihole_updown "DNS Director $KEY changed: '$CUR_N' -> '$WANT_N' (mode=$MODE)"
echo "DNS Director $KEY changed: '$CUR_N' -> '$WANT_N' (mode=$MODE)"

```

## router/jffs/blarm/scripts/pihole_status.sh

```sh
#!/bin/sh
#
# /jffs/blarm/scripts/pihole_status.sh
#
# Displays current Pi-hole DNS Director status and failover state.
#

set -eu

VARS="/jffs/blarm/common/common_vars"
[ -f "$VARS" ] || { echo "ERROR: missing $VARS" >&2; exit 1; }
# shellcheck disable=SC1090
. "$VARS"

STATE_DIR="/jffs/blarm/state"
STATE_FILE="$STATE_DIR/pihole_outage_state"
FAIL_FILE="$STATE_DIR/pihole_outage_fails"
SUCC_FILE="$STATE_DIR/pihole_outage_succ"

CURRENT_DNS="$(nvram get dnsfilter_custom1 2>/dev/null || echo "unknown")"
STATE="$(cat "$STATE_FILE" 2>/dev/null || echo "UP")"
FAILS="$(cat "$FAIL_FILE" 2>/dev/null || echo 0)"
SUCC="$(cat "$SUCC_FILE" 2>/dev/null || echo 0)"

echo "-----------------------------------------"
echo " Pi-hole DNS Director Status"
echo "-----------------------------------------"
echo "Router IP:                $ROUTER_IP"
echo "Pi-hole IP:               $PIHOLE_IP"
echo "Fallback DNS:             $PIHOLE_OUTAGE_FALLBACK_IP"
echo
echo "dnsfilter_custom1:        $CURRENT_DNS"
echo "Recorded state:           $STATE"
echo "Failure counter:          $FAILS"
echo "Success counter:          $SUCC"
echo

if [ "$CURRENT_DNS" = "$PIHOLE_IP" ]; then
  echo "Mode:                     ACTIVE (Using Pi-hole)"
elif [ "$CURRENT_DNS" = "$PIHOLE_OUTAGE_FALLBACK_IP" ]; then
  echo "Mode:                     FALLBACK (Using public DNS)"
else
  echo "Mode:                     UNKNOWN (Value unexpected)"
fi

echo

NSLOOKUP_BIN="/usr/bin/nslookup"
NC_BIN="/usr/bin/nc"

echo "Live health test against Pi-hole ($PIHOLE_FAILOVER_CHECK_DOMAIN)..."

if [ -x "$NSLOOKUP_BIN" ]; then
  if "$NSLOOKUP_BIN" "$PIHOLE_FAILOVER_CHECK_DOMAIN" "$PIHOLE_IP" >/dev/null 2>&1; then
    echo "Health check:             OK (Pi-hole resolving)"
  else
    echo "Health check:             FAILED (No DNS response from Pi-hole)"
  fi
elif [ -x "$NC_BIN" ]; then
  if echo | "$NC_BIN" -w 1 -u "$PIHOLE_IP" 53 >/dev/null 2>&1; then
    echo "Health check:             OK (UDP/53 reachable)"
  else
    echo "Health check:             FAILED (UDP/53 not reachable)"
  fi
else
  echo "Health check:             No nslookup/nc available on router"
  echo "                           (Expected at $NSLOOKUP_BIN or $NC_BIN)"
fi

echo "-----------------------------------------"

```
