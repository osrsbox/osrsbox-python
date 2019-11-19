"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Process all extracted 2007scape data and only grab the last six years.

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

# file_in = "submissions.json"
# file_out = "submissions_sixyears.json"
file_in = "comments.json"
file_out = "comments_sixyears.json"
f_out = open(file_out, 'a')
count = 0

# Set the date value for the newest data
# This will remove all posts after this date
newest_date = datetime.datetime.strptime('2019-02-15', "%Y-%m-%d")

print(">>> Processing data...")
with open(file_in) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        # BLOCK: Group on year/month posted
        # Fetch the "created_utc" epoch timestamp and convert to datetime
        date = datetime.datetime.fromtimestamp(json_obj["created_utc"])
        if date < newest_date:
            json.dump(json_obj, f_out)
            f_out.write("\n")
        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)
print()
