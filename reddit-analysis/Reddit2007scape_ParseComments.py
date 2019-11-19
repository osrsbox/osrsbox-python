"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Parse extracted comments from 2007Scape subreddit.

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

file_in = "comments.json"

count = 0

# Structures
comments_counter = collections.defaultdict(int)  # Group on year/month posted
comments_author = collections.defaultdict(int)  # Find top 20 authors

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
        comments_counter[key] += 1

        # BLOCK: Find top 20 authors
        # Determine the comments author
        author = json_obj["author"]
        # Increment author count
        comments_author[author] += 1

        count += 1
        sys.stdout.write(">>> Processed: %d\r" % count)

print()

# Loop comments_counter dict with YYYY-MM -> Count
for k, v in comments_counter.items():
    print(k, v)

comments_author_list = sorted(comments_author.items(),
                              key=lambda x: x[1],
                              reverse=True)

print("%s,%s,%s" % ("Rank", "Author", "Count"))
# Loop comments_author dict with enumerator and
# tuple of (author name, comments count)
for i, author in enumerate(comments_author_list):
    if i > 25:
        break
    print("%d,%s,%s" % (i, author[0], author[1]))

# EXAMPLE OUTPUT:
# python3.5 Reddit2007scape_ParseComments.py
# >>> Processing data...
# >>> Processing: 9262574
# 2013-03 32877
# 2017-06 284863
# 2014-02 23296
# 2014-01 24722
# 2013-04 28184
# 2013-05 18938
# 2016-03 147367
# 2015-02 93178
# 2015-10 112313
# 2018-05 196619
# 2017-10 170146
# 2014-04 29250
# 2014-09 54711
# 2014-12 56418
# 2017-09 170401
# 2015-07 121075
# 2014-11 58688
# 2016-08 167991
# 2014-05 42780
# 2018-08 212725
# 2019-01 272341
# 2018-04 171509
# 2015-05 142454
# 2013-02 11810
# 2013-09 12304
# 2017-02 187758
# 2015-03 133992
# 2018-01 188233
# 2019-02 121415
# 2018-12 218026
# 2016-06 184168
# 2016-07 178409
# 2018-03 203058
# 2016-09 144384
# 2015-09 124882
# 2017-01 223124
# 2014-10 62530
# 2013-07 14826
# 2014-07 58584
# 2014-08 65141
# 2016-11 143152
# 2017-03 193117
# 2018-09 193594
# 2015-12 116094
# 2015-08 121980
# 2013-10 13507
# 2016-05 202256
# 2016-04 146329
# 2013-06 15559
# 2015-06 119770
# 2015-11 115074
# 2013-11 14009
# 2013-08 14378
# 2016-12 156059
# 2015-04 137607
# 2018-06 195177
# 2017-08 173218
# 2018-11 257791
# 2014-03 25148
# 2015-01 95172
# 2018-07 226219
# 2013-12 18623
# 2017-11 187484
# 2018-02 180595
# 2014-06 46129
# 2016-10 158843
# 2016-02 126933
# 2017-07 197437
# 2016-01 150516
# 2017-05 176847
# 2018-10 234855
# 2017-04 181432
# 2017-12 162180
# Rank,Author,Count
# 0,[deleted],632274
# 1,AutoModerator,33905
# 2,BioMasterZap,29623
# 3,Shortdood,24166
# 4,_Serene_,18996
# 5,S7EFEN,17445
# 6,EdHicks,16969
# 7,tom2727,14570
# 8,threw_it_up,13792
# 9,Purge2202,11696
# 10,DivineInsanityReveng,11093
# 11,OSRS_HELL,10973
# 12,celery_under,10097
# 13,zekerman,9256
# 14,Tyler_OSRS2002,9043
# 15,mogotrevo,8929
# 16,PttB_Viper,8915
# 17,BasicFail,8847
# 18,Faladorable,8740
# 19,Supergigala,8595
# 20,Kupopallo,8449
# 21,SharkBrew,8431
# 22,yunnbelttab,8409
# 23,Someone9339,8351
# 24,demon306,8297
# 25,IkWhatUDidLastSummer,8280
