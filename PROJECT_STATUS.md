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
| 6 | Handle duplicate dates | Complete |
| 7 | Optional prefix/suffix text in final filename | Complete (runtime override deferred) |

**🎉 All 7 original features complete — program runs end-to-end!**

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
| 04-22-2026 | Destination structure: target_folder/output/year/date/new_name | Keeps files organized hierarchically |
| 04-22-2026 | file.get("part") used for safe access | Handles files that didn't receive part numbers |
| 04-22-2026 | Year folder bug fixed — anchored to target_folder explicitly | Previously used Path(filepath).parent, now uses target path |
| 04-30-2026 | Extensions normalized to lowercase in scan_files | Fixes case-sensitivity bug (.wav vs .WAV grouping) |
| 04-30-2026 | output/ wrapper folder added for year folders and unknown/ | Cleaner separation between source and processed files |
| 04-30-2026 | DJI sub-sequence letters deferred — not confirmed as needed yet | Wait for evidence the issue actually appears in real files |

---

## Known Gaps / Flags
- Claire's cam files have no filename date AND no metadata date — needs a third date source (next priority)
- End-of-program summary not yet built (stats already collected in move_dated_files)
- Runtime override for prefix/suffix deferred — config defaults work for now
- Feature 3 still untested with real embedded tag data
- May want to add an MP3 with embedded tags later to verify TDRC works correctly
- normalize_date() may need updating if new date formats are discovered
- Stray MEDI tag left on sample file from early testing — harmless but noted
- If DJI sub-sequence handling becomes needed: two-function approach (detect + assign), detection via `_` splitting, check first segment for DJI case-insensitive

---

## Current Sub-Session
> None active.

---

## Next Steps
- Sub-Session 8: Add a date source for Claire's cam (likely folder name or file modification time)
- Future: End-of-program summary report
- Future: Runtime override for prefix/suffix
- Future: Test Feature 3 with a real tagged MP3 file
- Future: Investigate Canon folder name 665_1212 for partial date extraction