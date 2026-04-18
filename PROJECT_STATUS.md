# MediaButler Project Status Document

---

## Language & Tools
| Item | Decision | Notes |
|------|----------|-------|
| Language | Python 3.14.4 | |
| Editor | Visual Studio Code | |
| Version Control | GitHub | |
| Libraries | mutagen, os, shutil, pathlib, re | mutagen installed |

---

## Feature Checklist
| # | Feature | Status |
|---|---------|--------|
| 1 | Rename files using date from filename (MM-DD-YYYY) | Complete |
| 2 | Configurable filename parsing (patterns in config) | Complete |
| 3 | Metadata fallback if date not in filename | Complete (untested with real tag data) |
| 4 | Preserve original filename in metadata | Complete |
| 5 | Sort files into year folders | Complete |
| 6 | Handle duplicate dates | In Progress |
| 7 | Optional prefix/suffix text in final filename | Not Started |

---

## Decisions Log
| Date | Decision | Reason |
|------|----------|--------|
| 04-13-2026 | Python chosen as language | Beginner-friendly, excellent file/metadata library support, large community |
| 04-13-2026 | VS Code chosen as editor | Lightweight, great Python/Git support |
| 04-13-2026 | Libraries planned: mutagen, os, shutil, pathlib, re | Best fit for file ops and metadata |
| 04-13-2026 | All current devices use YYYYMMDD_HHMMSS — one pattern covers all | Simplifies config.py for now |
| 04-13-2026 | Canon VIXIA (MVI_XXXX) has no date in filename — metadata fallback planned | No date info available in filename |
| 04-13-2026 | Canon folder name 665_1212 may contain partial date — investigate later | Flagged for future pattern work |
| 04-14-2026 | normalize_date() assumes YYYYMMDD for non-dashed formats | Other formats may need handling later |
| 04-14-2026 | Metadata tags handled: TDRC (MP3) and ©day (MP4) | Most common formats for our devices |
| 04-15-2026 | Used custom field MEDIABUTLER_ORIGINAL over comment field | Avoids clobbering user data |
| 04-15-2026 | MP4 key format: ----:com.apple.iTunes:MEDIABUTLER_ORIGINAL | Required format for custom MP4 tags |
| 04-15-2026 | MP4 values must be encoded as utf-8 bytes | mutagen MP4 requirement |
| 04-15-2026 | shutil.move() used to move files into year subfolders | Folder created with exist_ok=True to avoid crashes on duplicates |
| 04-18-2026 | Files from same source folder = same sequence | Logical grouping by recording session |
| 04-18-2026 | Multiple source folders on same date = different sequences (A, B, C...) | Distinguishes separate recording sessions |
| 04-18-2026 | Different file types on same date = no conflict, no part numbers needed | Extension included in grouping key |
| 04-18-2026 | Folder order determined alphabetically for predictability | Users can prefix folder names with numbers to force order |
| 04-18-2026 | None-date files moved to unknown/ folder for manual handling | Avoids silently dropping unprocessable files |

---

## Known Gaps / Flags
- Feature 6 not yet complete — still needed: call assign_part_numbers on duplicate groups, rename/move files into date subfolders, handle None-date files
- None-date files should be moved with their containing folder to an unknown/ folder
- Year folder location bug: year folders must be created inside the MediaButler main folder, not relative to script location — fix after Feature 6
- Feature 3 is untested with real embedded tag data — sample files had no tags
- May want to add an MP3 with embedded tags later to verify TDRC works correctly
- normalize_date() may need updating if new date formats are discovered
- Stray MEDI tag left on sample file from early testing — harmless but noted

---

## Current Sub-Session
> None active.

---

## Next Steps
- Sub-Session 6: Complete Feature 6 — wire up assign_part_numbers, rename/move files into date subfolders, handle None-date files
- Sub-Session 7 (after Feature 6): Fix year folder location bug
- Future: Feature 7 — optional prefix/suffix text in final filename
- Future: Test Feature 3 with a real tagged MP3 file
- Future: Investigate Canon folder name 665_1212 for partial date extraction