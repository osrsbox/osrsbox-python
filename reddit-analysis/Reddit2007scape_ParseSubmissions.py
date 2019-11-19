"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Parse extracted submissions (posts) from 2007Scape subreddit.

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

# Input file
file_in = "submissions.json"

count = 0

# Structures
submissions_counter = collections.defaultdict(int)  # Group on year/month
submissions_author = collections.defaultdict(int)  # Find top 20 authors

print(">>> Processing data...")
with open(file_in) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        # BLOCK: Group on year/month posted
        # Fetch the "created_utc" epoch timestamp and convert to datetime
        date = datetime.datetime.fromtimestamp(json_obj["created_utc"])
        month = "%02d" % date.month  # Pad single digit months
        year = date.year
        # Make dict key YYYY-MM, e.g., 2018-11
        key = str(year) + "-" + str(month)
        # if key == "2019-02":
        #     continue
        submissions_counter[key] += 1

        # BLOCK: Find top 20 authors
        # Determine the submission author
        author = json_obj["author"]
        # Increment author count
        submissions_author[author] += 1

        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)

print()

# Loop submissions_counter dict with YYYY-MM -> Count
for k, v in submissions_counter.items():
    print(k, v)

submissions_author_list = sorted(submissions_author.items(),
                                 key=lambda x: x[1],
                                 reverse=True)
print("%s,%s,%s" % ("Rank", "Author", "Count"))
# Loop submissions_author dict with enumerator and
# tuple of (author name, submission count)
for i, author in enumerate(submissions_author_list):
    if i > 25:
        break
    print("%d,%s,%s" % (i, author[0], author[1]))

# EXAMPLE OUTPUT:
# python3.5 Reddit2007scape_ParseSubmissions.py
# >>> Processing data...
# >>> Processing: 808291
# 2017-09 16316
# 2015-11 11296
# 2014-11 5146
# 2018-07 18160
# 2014-09 4929
# 2013-08 1609
# 2013-02 1749
# 2013-10 1670
# 2018-09 14810
# 2013-12 1995
# 2019-01 20429
# 2016-03 13812
# 2018-10 17425
# 2016-10 13914
# 2014-02 2309
# 2015-06 9888
# 2018-03 15614
# 2013-07 1807
# 2014-05 4059
# 2015-07 9950
# 2017-03 18706
# 2015-01 8352
# 2018-02 14674
# 2014-07 5837
# 2016-02 11267
# 2018-04 13064
# 2018-08 15638
# 2015-02 9688
# 2016-06 16810
# 2019-02 8516
# 2017-11 15086
# 2016-09 12478
# 2017-08 15137
# 2017-10 14383
# 2013-04 2780
# 2015-04 12745
# 2017-12 14679
# 2016-07 18008
# 2018-06 14555
# 2017-05 16473
# 2015-03 13193
# 2017-07 18184
# 2015-12 10128
# 2016-05 17937
# 2014-03 2670
# 2017-06 25619
# 2015-05 13306
# 2013-09 1437
# 2018-11 20399
# 2013-05 2008
# 2015-08 10193
# 2017-02 18086
# 2016-01 13659
# 2015-09 10069
# 2017-04 17011
# 2017-01 19622
# 2013-06 2079
# 2014-06 5177
# 2014-12 5359
# 2014-08 6260
# 2014-01 2599
# 2013-11 1475
# 2018-01 16024
# 2013-03 3813
# 2014-04 2752
# 2018-12 16043
# 2014-10 5505
# 2015-10 9921
# 2016-12 14541
# 2018-05 15899
# 2016-04 14026
# 2016-08 13993
# 2016-11 13541
# Rank,Author,Count
# 0,[deleted],143817
# 1,AutoModerator,1344
# 2,rawktail,667
# 3,Beratho,619
# 4,Gameboto4,583
# 5,deanzynut,498
# 6,OsrsNeedsF2P,473
# 7,Herb_Quest,438
# 8,Avnas,437
# 9,Lnfinite_god,434
# 10,IkWhatUDidLastSummer,428
# 11,alstablieft,427
# 12,Pops_rustafied,403
# 13,rudyv8,400
# 14,ProktosRS,396
# 15,BoulderFalcon,392
# 16,rank_1_glad,385
# 17,Shortdood,381
# 18,TheNote7,380
# 19,EdHicks,377
# 20,RNGreed,374
# 21,OSRS_HELL,361
# 22,iAmNotSharky,355
# 23,WeededDragon1,341
# 24,vannoD,340
# 25,Espret,339
