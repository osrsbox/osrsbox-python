"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description: A simple script to download the summary.json file from the OSBuddy
GE service, compress it and save it to a data folder.

Automate using cron:
crontab -e
*/15 * * * * python3 /path/to/osrsbuddy_ge_fetch_summary.py > /dev/null 2>&1

Copyright (c) 2019, PH01L

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""

import datetime
import json
import zlib
import urllib.request
from pathlib import Path
from base64 import b64encode, b64decode

# URL of the file to download
url = "https://rsbuddy.com/exchange/summary.json"

# Download the file, and load into a JSON object
page = urllib.request.urlopen(url).read().decode("utf-8")
json_data = json.loads(page)

# Convert JSON data to a string, and encode to bytes object
json_bytes = json.dumps(json_data).encode("utf-8")
# Compress the JSON bytes object
json_compressed = zlib.compress(json_bytes)
# Shrink into base64 encoded bytes object, and convert to an ASCII string
json_out = b64encode(json_compressed).decode("ascii")

# Get the current timestamp, to append to file name
current_date = datetime.datetime.now()
current_date = current_date.strftime("%Y-%m-%d-%H-%M-%S")
filename =  current_date + "_summary.json"

# Export the compressed JSON file
out_fn = Path.home() / "osrsbox-python" / "osbuddy_ge_fetch" / "data" / filename
with open(str(out_fn), 'w') as outfile:
    json.dump(json_out, outfile)

