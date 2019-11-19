"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Find the earliest (lastest) post from 2007Scape reddit.

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

import sys
import json

file_in_sub = "submissions.json"

total_count = 0

timestamp = list()
print(">>> Processing data...")
with open(file_in_sub) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)
        timestamp.append(json_obj["created_utc"])
        total_count += 1
        sys.stdout.write(">>> Processed: %d\r" % total_count)

earliest = min(timestamp)
print(earliest)
