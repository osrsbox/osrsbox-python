"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description: This script decompresses a compressed summary.json file that has
been scraped from the OSBuddy GE service, and compressed using zlib.

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

import json
import zlib
from pathlib import Path
from base64 import b64encode, b64decode


def decompress_file(data: str):
    # Decode the data from base64
    data = b64decode(data)
    # Decompress the decoded data
    data = zlib.decompress(data)
    # Decode te data to UTF8
    data = data.decode("utf-8")
    # Load the file into a dictionary
    data = json.loads(data)

    return data


# Fetch all the files
json_files_path = Path.cwd() / "data" 
json_files = json_files_path.glob("*.json")

# Loop all the files
for json_file in json_files:
    with open(str(json_file)) as compressed_json_file:
        file_data = compressed_json_file.read()
        json_dict = decompress_file(file_data)
        print(json_dict["2361"]["overall_average"])

