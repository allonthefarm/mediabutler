from config import DATE_PATTERNS
from mutagen import File
import re
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