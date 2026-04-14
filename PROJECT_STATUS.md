# MediaButler Project Status Document

---

## Language & Tools
| Item | Decision | Notes |
|------|----------|-------|
| Language | TBD | |
| Editor | Visual Studio Code | |
| Version Control | GitHub | |
| Libraries | mutagen, os, shutil, pathlib, re | |

---

## Feature Checklist
| # | Feature | Status |
|---|---------|--------|
| 1 | Rename files using date from filename (MM-DD-YYYY) | Complete |
| 2 | Configurable filename parsing (patterns in config) | Complete |
| 3 | Metadata fallback if date not in filename | Not Started |
| 4 | Preserve original filename in metadata | Not Started |
| 5 | Sort files into year folders | Not Started |
| 6 | Handle duplicate dates | Not Started |
| 7 | Optional prefix/suffix text in final filename | Not Started |

---

## Decisions Log
| Date | Decision | Reason |
|------|----------|--------|
| 04-13-2026 | Python chosen as language | Beginner-friendly, excellent file/metadata library support, large community | 
|04-13-2026| VS Code chosen as editor | Lightweight, great Python/Git support |
|04-13-2026| Libraries planned: mutagen, os, shutil, pathlib, re | Best fit for file ops and metadata |
|04-13-2026| Canon VIXIA (MVI_XXXX) has no date — metadata fallback planned | 
|04-13-2026| Canon folder 665_1212 may have partial date — investigate later | 
|04-13-2026| All current devices use YYYYMMDD_HHMMSS — one pattern covers all |
|04-13-2026| Canon VIXIA (MVI_XXXX) has no date — metadata fallback planned | 

---

## Current Sub-Session
> None active.

---

## Next Steps
- Sub-Session 2: Feature 3 — Metadata fallback for Canon files
