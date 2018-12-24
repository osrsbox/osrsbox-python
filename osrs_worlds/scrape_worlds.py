# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/12/25

Description:
Scrape the OSRS Worlds web page: http://www.runescape.com/slu and
output a file in JSON format.

Copyright (c) 2018, PH01L

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

>>> CHANGELOG:
    1.0.0       Base functionality
"""

__version__ = "1.0.0"

import os
import sys
import json
import collections
import urllib.request
import lxml.html

url = "http://www.runescape.com/slu"
print("URL: %r" % url)

# data = urllib.request.urlopen(url).read()
request = urllib.request.urlopen(url)
data = request.read()
doc = lxml.html.fromstring(data)

table = doc.xpath("//tbody")

worlds = list()

# Fetch all the tr elements and loop through them
trs = table[0].xpath("tr")
for tr in trs:    
    tds = tr.xpath("td")
    for td in tds:
        text = td.text_content()
        text = text.strip()
        worlds.append(text)

# Print the raw, scraped output:
# for world, players, country, members, activity in zip(*[iter(worlds)]*5):
#     print(world, players, country, members, activity)

# Clean the world information (name, country, members)
cleaned_worlds = dict()
for world, players, country, members, activity in zip(*[iter(worlds)]*5):
    world = world.replace("Old School", "")
    world = world.replace("OldSchool", "")
    world = int(world) + 300
    country = country.replace("United States", "US")
    country = country.replace("Germany", "DE")
    country = country.replace("United Kingdom", "UK")
    country = country.replace("Australia", "AU")
    if members == "Members":
        members = True
    elif members == "Free":
        members = False
    if activity == "-":
        activity = False
    cleaned_worlds[world] = {"country" : country, "members" : members, "activity" : activity }

# Create an ordered dict
ordered_worlds = collections.OrderedDict()
for world in sorted(cleaned_worlds.items()):
    ordered_worlds[world[0]] = world[1]

# Write ordered worlds to a JSON file
with open("worlds.json", "w") as f:
    json.dump(ordered_worlds, f, indent=4)

# Example of a tr element
# <tr class='server-list__row'>
#     <td class='server-list__row-cell'>
#             <a id='slu-world-385' class='server-list__world-link' href='http://oldschool.runescape.com/game?world=385'>Old School 85</a>
#     </td>
#     <td class='server-list__row-cell'>239 players</td>
#     <td class='server-list__row-cell server-list__row-cell--country server-list__row-cell--US'>United States</td>
#     <td class='server-list__row-cell server-list__row-cell--type'>Free</td>
#     <td class='server-list__row-cell'>750 skill total</td>
# </tr>
