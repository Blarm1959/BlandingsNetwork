# Diagram source and regeneration

Diagrams are part of the master record. Keep their source, evidence status, layout and builder in the repository so a lost PDF can be recreated without an old chat or working directory.

## Stored diagrams

| Diagram | Editable source of diagram facts | Generated outputs | Linked record |
|---|---|---|---|
| Garage switch | [source/GarageSwitch.json](source/GarageSwitch.json): all 18 ports, odd/even rows, null destinations, model, source/date and interpretation notes | [GarageSwitch.pdf](GarageSwitch.pdf), [GarageSwitch.svg](GarageSwitch.svg), marked Markdown table | [GarageSwitch record](../02-Hardware/GarageSwitch.md) |
| Physical topology | [source/PhysicalTopology.json](source/PhysicalTopology.json): named nodes, positions, historical connections, evidence references and known garage-port labels | [PhysicalTopology.pdf](PhysicalTopology.pdf), [PhysicalTopology.svg](PhysicalTopology.svg), [PhysicalTopology.mmd](PhysicalTopology.mmd), marked Mermaid block | [Topology record](../02-Hardware/Topology.md) |

The JSON files are the editable source for generated diagram/table content. They retain historical versus confirmed status; regeneration does not confirm wiring. The surrounding Markdown remains the authoritative explanation of limitations and verification requirements. Do not independently edit a generated table, Mermaid block, SVG or PDF; it will be overwritten by regeneration.

## Rebuild from the project folder

Python 3.10 or later and ReportLab are required. The builder is [tools/build_diagrams.py](../tools/build_diagrams.py); [tools/Build-Diagrams.ps1](../tools/Build-Diagrams.ps1) is the Windows launcher. Neither depends on paths from this chat or a particular drive letter.

The requirements file pins the tested ReportLab version (4.4.9). Keep that version when checking repeatable outputs. A deliberate renderer/dependency upgrade may require regenerating and visually reviewing every affected diagram.

With an existing Python installation:

```powershell
py -3 -m pip install -r .\tools\diagram-requirements.txt
.\tools\Build-Diagrams.ps1
```

If Python is elsewhere or the `py` launcher is unavailable, use its executable path:

```powershell
& 'C:\path\to\python.exe' -m pip install -r .\tools\diagram-requirements.txt
.\tools\Build-Diagrams.ps1 -PythonPath 'C:\path\to\python.exe'
```

The launcher uses its own repository location even when invoked from another directory. To rebuild just the garage diagram or check that all generated files match their sources:

```powershell
.\tools\Build-Diagrams.ps1 -Diagram garage-switch
.\tools\Build-Diagrams.ps1 -Check
```

`-Check` writes nothing and fails if a PDF/SVG/Mermaid file or a generated Markdown block is missing/outdated. It does not verify real equipment or judge visual layout. PDFs are A4 landscape with vector content. Their metadata uses a fixed creation timestamp to permit repeatable generation; the source/evidence dates in the visible document remain the meaningful dates.

## Change a diagram

1. Recover or confirm the new information and record its source/date/status. Preserve important previous wiring as history before replacing the original map.
2. Edit the relevant JSON. A null destination means unspecified, not unused. Keep the neoHub port-16 interpretation explicit until confirmed.
3. Run the builder. It updates only the marked table/Mermaid block and that diagram's output files; prose outside the markers remains intact.
4. Review the table and rendered PDF/SVG for correct labels, spacing and evidence status. Run `-Check`.
5. Include changed source, generated assets and record pages in the next PSTP Change Package. PSTP still owns release metadata.

Both selected sources are validated and rendered before any output is written. The current renderer supports a two-row port grid of up to nine ports per row, and a positioned topology. Invalid/duplicate ports, missing markers and unknown edge endpoints fail rather than silently generating incomplete diagrams.

## Other diagrams

Use the same source-and-builder approach for a future loft-switch map once numbered connections are supplied. Add a validated source JSON and register its outputs here. Unknown ports must stay unknown.

The old HomeNetwork logical-topology and policy-flow files were empty, with conflicting policy generations elsewhere. They are not current diagrams awaiting automatic regeneration. A future DNS/logical/policy diagram should be created only from explicitly labelled confirmed or historical evidence and registered with its source, renderer, output paths and regeneration command. Do not draw unverified firewall isolation as working behaviour.
