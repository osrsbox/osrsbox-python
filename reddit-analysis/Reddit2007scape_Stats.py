"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Description:
Script that processes and analysis some simple stuff about the 2007Scape
data that has been extracted.

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
import collections

file_in_sub = "submissions.json"
file_in_com = "comments.json"

total_count = 0
sub_count = 0
com_count = 0

total_body_text_wc = 0
total_title_text_wc = 0
over_18_count = 0
thumbnail_count = 0

total_word_counter = collections.defaultdict(int)  # Count words
sub_word_counter = collections.defaultdict(int)  # Count words
title_word_counter = collections.defaultdict(int)  # Count words
com_word_counter = collections.defaultdict(int)  # Count words

print(">>> Processing submission data...")
with open(file_in_sub) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        try:
            body_text = json_obj["selftext"]
            words = body_text.split()
            total_body_text_wc += len(words)
            for w in words:
                total_word_counter[w] += 1
                sub_word_counter[w] += 1
        except KeyError:
            pass

        title_text = json_obj["title"]
        words = title_text.split()
        total_title_text_wc += len(words)
        for w in words:
            total_word_counter[w] += 1
            title_word_counter[w] += 1
            sub_word_counter[w] += 1

        # "over_18":false,
        if json_obj["over_18"]:
            over_18_count += 1

        # "thumbnail":"self",
        if json_obj["thumbnail"] == "self" or json_obj["thumbnail"] == "default":
            pass
        else:
            thumbnail_count += 1

        total_count += 1
        sub_count += 1
        sys.stdout.write(">>> Processed: %d\r" % sub_count)

print()

print(">>> Processing comments data...")
with open(file_in_com) as f:
    for json_data in f:
        json_data = json_data.strip()
        json_obj = json.loads(json_data)

        body_text = json_obj["body"]
        words = body_text.split()
        total_body_text_wc += len(words)
        for w in words:
            total_word_counter[w] += 1
            com_word_counter[w] += 1

        total_count += 1
        com_count += 1
        sys.stdout.write(">>> Processed: %d\r" % com_count)

print()

print("total_body_text_wc TOTAL:", total_body_text_wc)
print("total_body_text_wc AVERAGE:", total_body_text_wc/total_count)
print("total_title_text_wc TOTAL:", total_title_text_wc)
print("total_title_text_wc AVERAGE:", total_title_text_wc/sub_count)
print("over_18_count TOTAL:", over_18_count)
print("over_18_count AVERAGE:", over_18_count/sub_count)
print("thumbnail_count TOTAL:", thumbnail_count)
print("thumbnail_count AVERAGE:", thumbnail_count/sub_count)

# This works, but commenting it out
# total_word_counter_list = sorted(total_word_counter.items(),
#                                  key=lambda x:x[1],
#                                  reverse=True)
# print("%s,%s,%s" % ("Rank", "Author", "Count"))

# Loop comments_author dict with enumerator and
# tuple of (author name, comments count)
# for i, author in enumerate(total_word_counter_list):
#     if i > 19:
#         break
#     print("%d,%s,%s" % (i, author[0], author[1]))

# total_word_counter
with open('wc_total_word_counter.json', 'w') as fp:
    json.dump(total_word_counter, fp)
# title_word_counter
with open('wc_title_word_counter.json', 'w') as fp:
    json.dump(title_word_counter, fp)
# com_word_counter
with open('wc_com_word_counter.json', 'w') as fp:
    json.dump(com_word_counter, fp)
# sub_word_counter
with open('wc_sub_word_counter.json', 'w') as fp:
    json.dump(sub_word_counter, fp)

# # Loop comments_counter dict with YYYY-MM -> Count
# for k, v in comments_counter.items():
#     print(k, v)

# comments_author_list = sorted(comments_author.items(),
#                               key=lambda x:x[1],
#                               reverse=True)
# print("%s,%s,%s" % ("Rank", "Author", "Count"))

# Loop comments_author dict with enumerator
# and tuple of (author name, comments count)
# for i, author in enumerate(comments_author_list):
#     if i > 19:
#         break
#     print("%d,%s,%s" % (i, author[0], author[1]))

# EXAMPLE OUTPUT:
#
# >>> Processing submission data...
# >>> Processing: 755297
# >>> Processing comments data...
# >>> Processing: 8541236
# total_body_text_wc TOTAL: 198334692
# total_body_text_wc AVERAGE: 21.334264289708862
# total_title_text_wc TOTAL: 5979954
# total_title_text_wc AVERAGE: 7.917354365236457
# over_18_count TOTAL: 752597
# over_18_count AVERAGE: 0.9964252472868289
# thumbnail_count TOTAL: 755297
# thumbnail_count AVERAGE: 1.0
#
# >>> Processing: 808291
# >>> Processing comments data...
# >>> Processing: 9262574
# total_body_text_wc TOTAL: 214415698
# total_body_text_wc AVERAGE: 21.290693301915972
# total_title_text_wc TOTAL: 6437336
# total_title_text_wc AVERAGE: 7.964131729785437
# over_18_count TOTAL: 2957
# over_18_count AVERAGE: 0.0036583359210977237
# thumbnail_count TOTAL: 232142
# thumbnail_count AVERAGE: 0.2872010204245748
