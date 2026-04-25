from config import DATE_PATTERNS, PREFIX, SUFFIX
from mutagen import File
from pathlib import Path
import re
import shutil
import os

def normalize_date(raw):
    rawstr = str(raw)
    if "-" in rawstr:
        norm_date = (rawstr[0:10])
        return norm_date
    else: norm_date = (rawstr[0:4]+"-"+rawstr[4:6]+"-"+rawstr[6:8])
    return norm_date

def extract_date(filename):
    for pattern in DATE_PATTERNS:
       match = re.search(pattern, filename)
       if match:
           raw = match.group(1)
           formatted = normalize_date(raw)
           return formatted
    return None

def extract_date_from_metadata(filepath):
    audio = File(filepath)
    if audio is None:
        return None
    if audio.tags is None:
        return None
    # For MP3 files, the date tag key is "TDRC"
    # For MP4 files, the date tag key is "©day"
    # We'll handle both
    raw = audio.tags.get("TDRC") or audio.tags.get("©day")
    if raw is None:
        return None
    return normalize_date(raw)

def get_date(filepath, filename):
    date = extract_date(filename)
    if date is None:
        date = extract_date_from_metadata(filepath)
    # future sources would go here
    return date

def original_filename_to_metadata(filepath, filename):
    media = File(filepath)
    if media is None:
        return None
    if Path(filepath).suffix == ".mp4":
        key = "----:com.apple.iTunes:MEDIABUTLER_ORIGINAL"
    else: key = "MEDIABUTLER_ORIGINAL"  
    if media.tags is None:
        media.add_tags()
    tags = media.tags.get(key)
    if tags is not None:
        return None
    if Path(filepath).suffix == ".mp4":
        media.tags[key] = filename.encode("utf-8")
    else: 
        media.tags[key] = filename 
    media.save()

def scan_files(filepath):
    file_index = []
    for folder, subfolders, files in os.walk(filepath):
        for filename in files:
            file_index.append({"path": Path(folder) / filename, "date": get_date(Path(folder) / filename, filename), "extension": Path(filename).suffix.lower(), "source_folder": folder})
    return file_index

def media_file_sort(file_index):
    indexed_files = {}
    for file in file_index:
        key = file["date"] + "_" + file["extension"]
        if key in indexed_files:
            indexed_files[key].append(file)
        else:
            indexed_files[key] = [file]
    return indexed_files

def assign_part_numbers(group):
    unique_folders = sorted(set(f["source_folder"] for f in group))
    files = sorted(group, key=lambda f: f["source_folder"])
    folder_counts = {}
    for file in files:
        folder = file["source_folder"]
        position = unique_folders.index(folder)
        count = folder_counts.get(folder, 0)
        folder_counts[folder] = count + 1
        if len(unique_folders) > 1:
            file["part"] = "part " + chr(ord('a') + position) + str(count + 1) 
        else:
            file["part"] = "part " + str(count + 1)
    return group


def no_date_sort(file_index):
    dated_files = []
    undated_files = []
    for file in file_index:
        if file["date"] is None:
            undated_files.append(file)
        else:
            dated_files.append(file)
    return dated_files, undated_files

def build_filename(date, part, extension, prefix="", suffix=""):
    parts = []
    if prefix:
        parts.append(prefix)
    parts.append(date)
    if part:
        parts.append(part)
    if suffix:
        parts.append(suffix)
    # you add the rest...
    filename = " ".join(parts) + extension
    return filename

def process_files(target_folder):
    # path to all out put
    output_to_folder = Path(target_folder) / "output"
    #1. scan files
    file_index = scan_files(target_folder)
    #2. split dated and undated
    file_index_dated, file_index_undated = no_date_sort(file_index)
    #3 move undated to unknown/
    unknown_folder = output_to_folder / "unknown"
    unknown_folder.mkdir(parents=True, exist_ok=True)
    for file in file_index_undated:
        shutil.move(file["path"], unknown_folder)
    #4 group dated files
    grouped_files = media_file_sort(file_index_dated)
    #5for each group, assign part numbers if needed and rename and move files
    for key, group in grouped_files.items():
        if len(group) > 1:
            assign_part_numbers(group)
        for file in group:
            new_name = build_filename(file["date"],  file.get("part"), file["extension"], prefix=PREFIX, suffix=SUFFIX)
            dest_folder = output_to_folder / file["date"][0:4] / file["date"]
            dest_folder.mkdir(parents=True, exist_ok=True)
            shutil.move(file["path"], dest_folder /new_name)
    return None

if __name__ == "__main__":
    process_files(r"D:\Users\allon\Documents\Programing\mediabutler\Test")