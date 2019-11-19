"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Remove duplicates from 2007Scape extracted data. Or use to combine multiple
JSON files.

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

# SUBMISSIONS!
print(">>> Processing submissions...")
file_in = "submissions_old.json"
file_out = "submissions_new.json"
count = 0
known_sub_id = set()
f_out = open(file_out, 'a')
with open(file_in) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)
        if not json_obj["id"] in known_sub_id:
            json.dump(json_obj, f_out)
            f_out.write("\n")
        known_sub_id.add(json_obj["id"])
        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)
print()

# COMMENTS!
print(">>> Processing comments...")
file_in = "comments_old.json"
file_out = "comments_new.json"
count = 0
known_com_id = set()
f_out = open(file_out, 'a')
with open(file_in) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)
        if not json_obj["id"] in known_com_id:
            json.dump(json_obj, f_out)
            f_out.write("\n")
        known_com_id.add(json_obj["id"])
        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)
print()
