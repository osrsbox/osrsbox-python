# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/12/25

Description:
Parses a directory of JSON files from the RuneLite Player Scraper plugin.


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
import glob
import json
import collections
import operator

# Import PlayerScraper class
sys.path.append(os.getcwd())
import PlayerScraper

# Load all JSON files with player information into a list
fis = glob.glob("playerscraper/*")

# Open OSBuddy's summary.json file about item prices
with open("summary.json") as f:
    summary = json.load(f) 

# Open my worlds.json file (metadata about worlds)
with open("worlds.json") as f:
    worlds = json.load(f)   

# Open my items_itemscraper.json file (my file with cost and alch prices)
with open("items_itemscraper.json") as f:
    allitems = json.load(f)   

csv_out = list()
# Print CSV header
csv_out.append("%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ("player_name", "player_name_len", "combat_level", "world_number", "world_country", "world_members", "world_activity", "world_requirement", "total_wealth", "head", "cape", "amulet", "weapon", "torso", "shield", "legs", "hands", "boots", "cost_head", "cost_cape", "cost_amulet", "cost_weapon", "cost_torso", "cost_shield", "cost_legs", "cost_hands", "cost_boots", "is_naked"))


count = 1
players = list()

# Start looping through players JSON files
for fi in fis:
    # Create PlayerScaper object for each player
    ps = PlayerScraper.PlayerScraper()
    ps.load(fi) # Load the players JSON file
    ps.calc_wealth(summary, allitems) # Claculate players wealth
    ps.determine_world(worlds) # Determine metadata about the world

    # Print CSV row (one for each player!)
    # Change "Player" + str(count) to ps.player for name, not placeholder
    csv_out.append("%s;%d;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % ("Player" + str(count), len(ps.player), ps.combat, ps.world, ps.world_country, ps.world_members, ps.world_activity, ps.world_requirement, ps.wealth, ps.head, ps.cape, ps.amulet, ps.weapon, ps.torso, ps.shield, ps.legs, ps.hands, ps.boots, ps.cost_head, ps.cost_cape, ps.cost_amulet, ps.cost_weapon, ps.cost_torso, ps.cost_shield, ps.cost_legs, ps.cost_hands, ps.cost_boots, ps.is_naked))
    
    players.append(ps)

    count += 1 # Increase count
    
# now save the csv_out.list to a file
with open("playerscraper.csv", "w") as f:
    for l in csv_out:
        f.write(l)
        f.write("\n")
        
# quit() # Stop here to not process item slots
# Some very unelegant code to determine most popular 5 items that
# are worn in each slot. Not counting when nothing equipped.
head = collections.defaultdict(int)
for ps in players:
    if ps.head is not None:
        head[ps.head] += 1
shead = sorted(head.items(), key=operator.itemgetter(1),reverse=True)
print(">>> Head slot")
for s1,s2,s3,s4,s5 in zip(*[iter(shead)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break

cape = collections.defaultdict(int)
for ps in players:
    if ps.cape is not None:
        cape[ps.cape] += 1
scape = sorted(cape.items(), key=operator.itemgetter(1),reverse=True)
print(">>> cape slot")
for s1,s2,s3,s4,s5 in zip(*[iter(scape)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break   

amulet = collections.defaultdict(int)
for ps in players:
    if ps.amulet is not None:
        amulet[ps.amulet] += 1
samulet = sorted(amulet.items(), key=operator.itemgetter(1),reverse=True)
print(">>> amulet slot")
for s1,s2,s3,s4,s5 in zip(*[iter(samulet)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break       

weapon = collections.defaultdict(int)
for ps in players:
    if ps.weapon is not None:
        weapon[ps.weapon] += 1
sweapon = sorted(weapon.items(), key=operator.itemgetter(1),reverse=True)
print(">>> Weapon slot")
for s1,s2,s3,s4,s5 in zip(*[iter(sweapon)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break    

torso = collections.defaultdict(int)
for ps in players:
    if ps.torso is not None:
        torso[ps.torso] += 1
storso = sorted(torso.items(), key=operator.itemgetter(1),reverse=True)
print(">>> torso slot")
for s1,s2,s3,s4,s5 in zip(*[iter(storso)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break    

shield = collections.defaultdict(int)
for ps in players:
    if ps.shield is not None:
        shield[ps.shield] += 1
sshield = sorted(shield.items(), key=operator.itemgetter(1),reverse=True)
print(">>> shield slot")
for s1,s2,s3,s4,s5 in zip(*[iter(sshield)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break    

legs = collections.defaultdict(int)
for ps in players:
    if ps.legs is not None:
        legs[ps.legs] += 1
slegs = sorted(legs.items(), key=operator.itemgetter(1),reverse=True)
print(">>> legs slot")
for s1,s2,s3,s4,s5 in zip(*[iter(slegs)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break        

hands = collections.defaultdict(int)
for ps in players:
    if ps.hands is not None:
        hands[ps.hands] += 1
shands = sorted(hands.items(), key=operator.itemgetter(1),reverse=True)
print(">>> hands slot")
for s1,s2,s3,s4,s5 in zip(*[iter(shands)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break  

boots = collections.defaultdict(int)
for ps in players:
    if ps.boots is not None:
        boots[ps.boots] += 1
sboots = sorted(boots.items(), key=operator.itemgetter(1),reverse=True)
print(">>> boots slot")
for s1,s2,s3,s4,s5 in zip(*[iter(sboots)]*5):
    print(allitems[str(s1[0])]["name"], "| Count:", s1[1], "| Percentage:", s1[1]/200)
    print(allitems[str(s2[0])]["name"], "| Count:", s2[1], "| Percentage:", s2[1]/200)
    print(allitems[str(s3[0])]["name"], "| Count:", s3[1], "| Percentage:", s3[1]/200)
    print(allitems[str(s4[0])]["name"], "| Count:", s4[1], "| Percentage:", s4[1]/200)
    print(allitems[str(s5[0])]["name"], "| Count:", s5[1], "| Percentage:", s5[1]/200)
    break          

# Special check for the 5 wealthiest players
wealth = dict()
for ps in players:
    if ps.wealth is not None:
        wealth[ps.player] = ps.wealth
swealth = sorted(wealth.items(), key=operator.itemgetter(1),reverse=True) 
print(">>> wealthiest players")
count = 0
wealth = 0
for s1,s2,s3,s4,s5 in zip(*[iter(swealth)]*5):
    if count >= 200:
        break
    print(s1)
    print(s2)
    print(s3)
    print(s4)
    print(s5)
    count += 5
    w = s1[1] + s2[1] + s3[1] + s4[1] + s5[1]
    wealth += w

print(wealth)
