"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Determine the popular day of the week for 2007scape posts/comments.

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
import datetime
import collections

count = 0

# Structures
dayofweek_sub = collections.defaultdict(int)  # Group on weekday posted
dayofweek_com = collections.defaultdict(int)  # Group on weekday posted

print(">>> Processing data...")
with open("submissions.json") as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        # BLOCK: Group on year/month posted
        # Fetch the "created_utc" epoch timestamp and convert to datetime
        date = datetime.datetime.fromtimestamp(json_obj["created_utc"])

        key = date.strftime("%Y_%A_%H")
        dayofweek_sub[key] += 1

        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)

print()

print(">>> Processing data...")
with open("comments.json") as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        # BLOCK: Group on year/month posted
        # Fetch the "created_utc" epoch timestamp and convert to datetime
        date = datetime.datetime.fromtimestamp(json_obj["created_utc"])

        key = date.strftime("%Y_%A_%H")
        dayofweek_sub[key] += 1

        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)

print()

dayofweek_sub = collections.OrderedDict(sorted(dayofweek_sub.items()))

# Loop dayofweek dict
for k, v in dayofweek_sub.items():
    year = k.split("_")[0]
    day = k.split("_")[1]
    time = k.split("_")[2]
    print("%s,%s,%s,%s" % (year, day, time, v))
