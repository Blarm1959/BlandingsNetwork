# Change control, releases and future-chat starter

[Master overview](../BlandingsNetwork.md) · [Evidence and sources](../07-Evidence/Sources.md)

## 8. Change control and chat retirement

1. GitHub holds the long-term released record. Current confirmed settings remain authoritative while investigations proceed.
2. Keep experiments out of the confirmed section. Record goal, starting state, exact change, test/result and rollback separately.
3. Promote a change only after the user confirms it works; record the date and evidence. Rejected and superseded work remains visible.
4. A material firmware/hardware change permits evaluating whether a rejected limitation has changed; it does not automatically overturn the decision.
5. Add source references for recovered chat details and distinguish user observations from assistant proposals.
6. Retire an old networking chat only after its unique decisions, failure reasons and useful files are preserved and reviewed by the user. None of the audited networking chats is cleared for deletion: older turns, attachments, some complete code and original test evidence remain missing. Use the coverage ledger rather than equating a returned page with a complete conversation.

### Repository workflow

- Established project: BlandingsNetwork, `Blarm1959/BlandingsNetwork`; released baseline v2.0.2 verified in local release metadata for this revision.
- PowerShellTools released baseline supplied by the user: v2.7.4 (S1/S3).
- Change Package name: `BlandingsNetwork-Changes-v<version>.zip`; filename is the intended release version, not an applied version change.
- Include only changed files. Normally exclude `release.json`, `build-info.json`, `package-lock.json` and release-history-only README changes. PSTP owns versioning, commits, tags and pushes.
- Provide a clickable Change Package download link. The user downloads it to Windows Downloads; do not write there or request Downloads permission. After review, run from the existing project:

```powershell
cd C:\WDL\GitHub\BlandingsNetwork
.\PSTP.ps1 Release -Zip
```

This review does not run a release or edit GitHub. For a genuinely new project, the separate creation standard is `ProjectCreate.ps1 ProjectName` from the PowerShellTools folder; do not recreate this existing project.

## 9. Future-chat starter

```text
BlandingsNetwork – continue from the released master record.
Repository: Blarm1959/BlandingsNetwork
Read BlandingsNetwork.md before making recommendations.
Treat confirmed architecture as authoritative: flat 10.59.0.0/16 LAN, no VLANs.
Do not reopen rejected items unless I ask or material firmware/hardware change addresses the limitation.
Keep remembered settings, historical proposals and experiments separate from confirmed state.
Only promote changes after I confirm they work; record evidence and dates.
Start with the open verification backlog. Exact DNS Director values still need live evidence.
Use Change Packages and PSTP; do not edit GitHub directly unless I explicitly ask.
```
