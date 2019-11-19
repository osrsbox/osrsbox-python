"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Extract data (submissions or comments) from 2007Scape subreddit.
Comment/Uncomment parts to dump submissions or comments.

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
import time
import requests

PUSHSHIFT_REDDIT_URL = "http://api.pushshift.io/reddit"


def fetchObjects(**kwargs):
    # Default params values
    params = {"sort_type": "created_utc", "sort": "asc", "size": 1000}
    for key, value in kwargs.items():
        params[key] = value
    print(params)
    type = "comment"
    if 'type' in kwargs and kwargs['type'].lower() == "submission":
        type = "submission"
    r = requests.get(PUSHSHIFT_REDDIT_URL + "/" + type + "/search/",
                     params=params,
                     timeout=30)
    if r.status_code == 200:
        response = json.loads(r.text)
        data = response['data']
        sorted_data_by_id = sorted(data, key=lambda x: int(x['id'], 36))
        return sorted_data_by_id


def process(**kwargs):
    # max_created_utc = 1356998400  # 01/01/2013 @ 12:00am (UTC)
    max_created_utc = 1549146733  # Update epoch time here if script crashes
    # If script crashes, use tail <filename> to find last created_utc timestamp
    max_id = 0
    # file = open("submissions.json","a")  # For submissions
    file = open("comments.json", "a")  # For comments
    while 1:
        nothing_processed = True
        objects = fetchObjects(**kwargs, after=max_created_utc)
        for object in objects:
            id = int(object['id'], 36)
            if id > max_id:
                nothing_processed = False
                created_utc = object['created_utc']
                max_id = id
                if created_utc > max_created_utc: max_created_utc = created_utc
                print(json.dumps(object, sort_keys=True, ensure_ascii=True), file=file)
        if nothing_processed: return
        max_created_utc -= 1
        time.sleep(.5)


# process(subreddit="2007scape",type="submission")
process(subreddit="2007scape", type="comments")
