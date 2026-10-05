# Five recovered legacy Merlin task summaries

[Master overview](../BlandingsNetwork.md) · [Thirteen-chat checklist](ArchivedChatReview.md)

## Source and status

On 5 October 2026 the user supplied copied request/summary/testing excerpts for all five previously unlocated tasks. Titles below are matched to the user's earlier list by content; the paste does not include per-task title headers, dates, commit IDs or structured speaker roles. [Supplied text](ArchivedChatCaptures/S36-S40-Pasted.txt) retains the copied wording, spacing/encoding artifacts and reported test results. SHA256 `030c19299cd93bd0e2ba805ad4e84ea68abd1a8fbea9c39fc1dba0dd0be7e420` fingerprints this saved text representation, not an original attachment or full chat export.

The supplied link `codex://threads/task_e_68a3bea37dd0832aa84a895e73e7e563` was rejected by the reader as “Invalid conversation”, including with the durable host. Its associated first excerpt concerns DNS rules; linkage is contextual rather than verified task metadata. No original code, patches, test logs or downloadable files were recovered. No script or test was executed during this documentation review. Reported passes below remain task-summary claims; they do not demonstrate a live router result.

## S36 — Update iptables in nvram_setup.sh for DNS

- Goal: permit TCP/UDP destination port53 only for PIHOLE_IP and PIHOLE_NON_PIHOLE_DNS, blocking other port53 destinations. The request's “YCP” is interpreted as TCP from its following wording.
- Reported change: nvram_setup.sh generates an NVRAM_DNS chain in nvram_firewall.add; sample firewall file updated with allowed/blocked DNS examples.
- Reported passes: replace_marked_block_test.sh, validate_dhcp_res_file_test.sh, validate_ssid_consistency_test.sh and validate_vlan_sequence_test.sh, all invoked with Bash under tests/.
- Limits: variable values, exact rules, jump placement, interfaces, rule order, persistence and DNS Director interaction are absent. Do not equate PIHOLE_NON_PIHOLE_DNS with today's fallback without its actual definition. The listed tests do not themselves establish packet-path enforcement. This targets port53 only; no claim about other DNS transports or effective guest behaviour follows.
- Current treatment: historical DNS-enforcement design, not current deployed rules or a reason to reinstall superseded VLAN-era scripts.

## S37 — Add tests for SSID and DHCP validation

- Goal: source nvram_setup.sh with stubbed helpers and test valid/invalid configuration using temporary/sample data.
- Reported change: validate_ssid_consistency_test.sh rejects empty SSIDs and too-short WPA2 passwords, accepts valid SSID/WPA settings; validate_dhcp_res_file_test.sh rejects bad MAC entries and accepts well-formed reservations. README gains test instructions.
- Reported passes: both new tests plus validate_vlan_sequence_test.sh, invoked with Bash.
- Limits: test/source bodies, expected boundary cases, actual output and deployed configuration are absent. The summary does not recover a current SSID, password or reservation list. No credentials are included.

## S38 — Add validate_vlan_sequence test

- Goal: source nvram_setup.sh, stub helpers, supply a VLAN_LIST missing53 and assert nonzero; corrected sequence should return zero.
- Reported change: tests/validate_vlan_sequence_test.sh added; README run instruction uses Bash.
- Reported result: **FAIL — expected broken VLAN list to fail**, because validate_vlan_sequence returned success for the broken sequence.
- Reason retained: validation accepted invalid input at that task's stage. This is a software-test failure, not the established root cause of the live ASUS VLAN instability.
- Current treatment: preserve the failed result even though other summaries report this test passing. No task dates or commit linkage establish the exact order or tested source versions. It does not reopen rejected VLAN design/testing.

## S39 — Edit nvram_pihole_failover.sh path

- Goal/reported change: correct the cron example and accompanying installation comment to `/jffs/asus_merlin/3006/nvram_pihole_failover.sh`.
- Reported pass: `bash -n nvram_pihole_failover.sh`.
- Limits: syntax check and documentation path correction do not prove installation, cron registration, failover operation or a renamed current script. S1's current names/common_vars and S30's historical /jffs/blarm cron evidence remain separate.

## S40 — Update nvram_setup.sh for loop handling

- Goal: avoid piped validation loops losing changes to the outer errs variable; make the function return nonzero on accumulated errors.
- Reported change: feed VLAN_LIST through a here-document in validate_vlan_sequence so the loop runs in the current shell; apply the same pattern to check_ssid_consistency for SSID/PSK validation.
- Reported passes: `bash -n nvram_setup.sh`; `NVRAM_VARS_FILE=./nvram_setup_vars bash nvram_setup.sh --help`.
- Uncompleted checks: shellcheck unavailable (“command not found”); apt-get update blocked by an unsigned repository. Neither is a passing lint/install check.
- Limits: the reported fix addresses a plausible cause of S38's lost validation errors, but this excerpt contains no regression-test run proving S38 passed on that exact fixed revision. Other summaries' passing reports stay separate. Bash syntax/help checks do not prove BusyBox/router compatibility or packet behaviour.

## Tested decisions versus historical proposals

The five summaries preserve useful engineering intent, a failing validation test, proposed fixes and claimed checks. They do not change the current flat10.59 LAN, remembered DNS Director design, guest Quad9 independence or current script inventory. The user-confirmed rejection of main-LAN VLANs remains locked: **DO NOT RECOMMEND AGAIN unless material firmware/hardware change addresses the limitation, or the user explicitly asks.** Do not infer that the validator defect caused the hardware/firmware limitation.

## Removal checklist

All five requested tasks now have supplied summaries captured and reviewed. They are no longer wholly unlocated evidence gaps. Full task histories and original code/test artifacts remain unrecovered. The thirteen-chat checklist records this distinction. Release this package through PSTP and review any unique missing artifacts before deciding to remove originals; these excerpts alone do not certify complete preservation of each task.
