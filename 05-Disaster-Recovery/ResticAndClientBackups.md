# Restic, Syncrify and client-backup history

[Master overview](../BlandingsNetwork.md) · [Archived-chat review](../07-Evidence/ArchivedChatReview.md)

## Evidence status

S32–S35 recover historical user statements, supplied workflow code and limited restore output. They do not establish current backup coverage or authorise cleanup. Historical tagging is user-reported complete (S32); current files, schedules, credentials and repository integrity remain to be inventoried. No code was installed or executed by this review.

## Historical data flow and paths

User-backed names: VPS INV-IONOS-01 → Syncrify data on laptop INV-LAP-01 → Synology NAS INV-NAS-01 (S32/S35). This strengthens those names beyond earlier assistant examples. Do not map INV-NAS-01 to a particular current IP/model without evidence. INV-VPS-Syncrify is a snapshot host label, not necessarily a DNS hostname.

| Item | Historical value | Status |
|---|---|---|
| Windows source | D:\Syncrify\syncrify@inventive.co.uk | Supplied script input, S32 |
| Windows helper | sync_syncrify_to_nas.cmd; access.log mtime versus access_last_run.txt | Supplied workflow; deployed version unknown |
| Mirror destination | \\INV-NAS-01\Share-01\Inventive_Backup\L and \Z; access.log at root | Supplied script; uses robocopy /MIR, which propagates deletions |
| NAS source | /volume1/Share-01/Inventive_Backup | Supplied script input |
| Repository | /volume1/restic_repos/inventive | Historical repository lead, S32/S35 |
| NAS helper | /volume1/Share-01/Backup/syncrify_restic_backup.sh | Proposed routine path |
| State | /volume1/Share-01/Backup/.syncrify_last_access_ts | Proposed marker; stored too early in supplied code |
| Private password file location | /volume1/Share-01/Backup/.restic_inventive_pass | Historical path only; no password contents recovered or included |
| NAS logs | /volume1/Share-01/Backup/logs/syncrify_restic_YYYYMMDD-HHMMSS.log | Proposed output |
| Schedule candidates | Laptop Mon–Fri16:30; NAS `0 18 * * *` | Supplied design, not observed scheduler exports; timezone unknown |

The change detector only watches access.log mtime; this alone does not prove source trees are complete or unchanged. Windows and NAS code record the marker before copy/backup success; failed work can therefore be skipped on the next run. Capture actual installed files before adopting the design as a reliable current pipeline. Preserve the existing paths privately before changing anything.

## Tagging decision and superseded work

Latest historical user requirement (S32): always use the snapshot host label and date tag YYYY-MM-DD; add year-YYYY if absent and month-YYYY-MM if absent. Historical retagging/host rewriting is user-reported finished and should not be rerun merely because old Stage1/Stage2 helper text survives. Check the INV-VPS-SYncrify versus INV-VPS-Syncrify case discrepancy against actual snapshot metadata.

First-of-year/month existence checks were intended to avoid rerunning the old historical process. The proposed code does not distinguish failed repository queries from empty results or scope them to the expected host, and lacks an overlap lock. The earlier Python/heredoc input error is documented in the review. None is provided as executable installation code by this package. No deployed pruning/retention policy is established.

## Historical restore-comparison evidence (S34)

User ran restic_check.sh from /volume1/Share-01/NASTidy and corrected RESTORED="$TAGDIR". Comparison root: /volume1/Share-01/Restic_Test/<date-tag>. The older extra path prefix was wrong for these restores.

| Date tag | Original tree | Reported total size (bytes) |
|---|---|---|
| 2018-01-01 | /volume1/Share-01/Backup/BackNASY/2018 | 17,301,299,233 |
| 2025-06-01 | /volume1/Share-01/Backup/BackNASM/2025-06 | 8,238,234,012 |
| 2025-09-16 | /volume1/Share-01/Backup/BackNASD/16 | 4,409,480,585 |
| 2025-12-02 | /volume1/Share-01/Backup/BackNASD/02 | 4,427,385,288 |

Historical method: bidirectional `rsync -aniv --delete --checksum`, a dry run. Both directions show only root-directory `.d..tpog...` metadata changes, no per-file change/deletion lines. These are four useful comparisons, not universal restore validation; no process exit codes or restic integrity check are included. The captures retain the output. No deletion of BackNASY/M/D is approved or recorded as completed.

## Macrium and USB history (S33/S35)

User identifies a D: folder backup to USB F: with weekday incrementals/30 backups at that time, plus a separate D:\WDL/D:\WDLPhotos job. Later G/F/S changes and “Macrium sorted” are user statements, but exact final retention/schedules are absent. Do not copy assistant-proposed schedules as installed settings.

Historical helper names: D:\Backup\RunToUSB.cmd, CopyImagesToUSB.ps1, CopyDGFSToUSB.ps1, WeeklyBackupHealthHtml.ps1 and BackupHealthReport.html. Assistant source/destination candidates: \\inv-nas-01\Share-INV-LAP-01\MacriumReflect\Image and \D-GFS → F:\MacriumReflect\Image and \D-GFS. CopyDGFSToUSB.log is the proposed D:\Backup log. Current script content and successful copy/deletion are unknown.

Observed failures: Unicode/mojibake output; Substring/null-index errors; completion banner despite exceptions; Macrium Image Guardian blocking scripted deletion. User then disabled MIG for F: because folder-level selection was unavailable. Preserve that historical reason; do not assume current protection on F: or other stores. Copy-only was an interim suggestion. File counts/latest timestamps in the proposed dashboard do not prove content equality or restoreability. Missing-source handling in the proposed mirror code is insufficient for a tested deletion workflow.

## Current recovery checks

V9/V10/V12 stay open. Inventory current private repository access, paths, scripts, schedules/timezone, success/failed-run markers, locking, retention, NAS-to-USB completeness and recoverable Macrium chains. Record actual tested restore scope and dates. Preserve history before considering old-copy cleanup; this review makes no cleanup change.
