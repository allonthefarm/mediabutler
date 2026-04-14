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
| 1 | Rename files using date from filename (MM-DD-YYYY format) | Not Started |
| 2 | Configurable filename parsing (patterns defined in config or labeled section) | Not Started |
| 3 | Metadata fallback if date not in filename | Not Started |
| 4 | Preserve original filename in metadata (no overwrite on re-run) | Not Started |
| 5 | Sort files into year folders | Not Started |
| 6 | Handle duplicate dates (subfolders, Part 1/2, Part A1/B1 sequencing) | Not Started |
| 7 | Optional prefix/suffix text in final filename | Not Started |

---

## Decisions Log
| Date | Decision | Reason |
|------|----------|--------|
| 04-13-2026 | Python chosen as language | Beginner-friendly, excellent file/metadata library support, large community | 
|04-13-2026| VS Code chosen as editor | Lightweight, great Python/Git support |
|04-13-2026| Libraries planned: mutagen, os, shutil, pathlib, re | Best fit for file ops and metadata |

---

## Current Sub-Session
> None active.

---

## Next Steps
- Choose a programming language
- Set up project folder structure and GitHub repo
- Begin Sub-Session 1: Filename parsing and date extraction
