from config import DATE_PATTERNS
import re
def extract_date(filename):
    for pattern in DATE_PATTERNS:
       match = re.search(pattern, filename)
       if match:
           return match.group(1)
    return None
