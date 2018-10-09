# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/10/10

Description:
HiscoresAPI.py is an API to help process OSRS Hiscores queries.

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
import urllib.request
import json
import string
import time
import requests
import argparse
import logging
from lxml import html

import collections

###############################################################################
class HiscoresPlayerScraperFull(object):
    def __init__(self, player_name, account_type):
        # Name of player to lookup
        self.player_name = player_name 

###############################################################################
class HiscoresPlayerScraperLite(object):
    def __init__(self, player_name, account_type):
        # Name of player to lookup
        self.player_name = player_name

        # The type of account
        self.account_type = account_type

        # Dict for personal hiscores
        self.hiscores = dict()

        self.base_urls = {
            "overall": "https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=",
            "ironman": "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player=",
            "ultimate": "https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.ws?player=",
            "hardcore": "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player="}

        # List of skills, in order as used by OSRS Hiscores page
        self.skills = [
            "Overall",
            "Attack",
            "Defence",
            "Strength",
            "Hitpoints",
            "Ranged",
            "Prayer",
            "Magic",
            "Cooking",
            "Woodcutting",
            "Fletching",
            "Fishing",
            "Firemaking",
            "Crafting",
            "Smithing",
            "Mining",
            "Herblore",
            "Agility",
            "Thieving",
            "Slayer",
            "Farming",
            "Runecraft",
            "Hunter",
            "Construction"]

    def get_players_hiscore_lite(self):
        print(">>> Processing player name: %s" % self.player_name)
        print(">>> Processing account type: %s" % self.account_type)

        if self.account_type not in self.base_urls:
            print(">>> Error: Not a correct account type...")
            print("  > Valid inputs: overall, ironman, ultimate, hardcore, deadman, seasonal")

        # Set the base URL, it only needs a player name appended
        base_url = self.base_urls[self.account_type]

        url = base_url + self.player_name

        print(">>> Target URL: %s" % url)

        page = urllib.request.urlopen(url).read().decode("utf-8")

        # Split Lite hiscores results into each line for one skill
        page = page.split("\n")   
                
        # Loop each skill containing (rank, level, xp)
        for i, skill in enumerate(self.skills):
            line = page[i].split(",")
            self.hiscores[skill] = {
                "rank" : int(line[0]),
                "level" : int(line[1]),
                "xp" : int(line[2])
            }

        return self.hiscores

    def print_players_hiscore_lite(self):
        # Print CSV style output
        print("%s,%s,%s,%s" % ("Skill", "Rank", "Level", "XP"))
        for k,v in self.hiscores.items():
            print("%s,%d,%d,%d" % (k, v["rank"], v["level"], v["xp"]))

    def json_players_hiscore_lite(self):
        # Save player hiscores to JSON format
        # File name is <player_name>.json
        f_name = self.player_name + ".json"
        with open(f_name, "w") as f:
            json.dump(self.hiscores, f)

    def json_pretty_players_hiscore_lite(self):
        # Save player hiscores to JSON format (indented/pretty)
        # File name is <player_name>.json
        f_name = self.player_name + ".json"
        with open(f_name, "w") as f:
            json.dump(self.hiscores, f, indent=4)        

###############################################################################
class HiscoresPageScraper(object):
    def __init__(self, account_type, lookup_player):
        # The type of overall hiscores to scrape
        self.account_type = account_type

        # Dict of all players: rank = Player(rank, name, level, xp)
        self.all_players = dict()

        # Object-wide page number
        self.page_number = 0

        # Boolean to determine if player hiscores should be saved
        self.lookup_player = lookup_player

        self.base_urls = {
            "overall": "https://secure.runescape.com/m=hiscore_oldschool/overall.ws?table=0&page=",
            "ironman": "https://secure.runescape.com/m=hiscore_oldschool_ironman/overall.ws?table=0&page=",
            "ultimate": "https://secure.runescape.com/m=hiscore_oldschool_ultimate/overall.ws?table=0&page=",
            "hardcore": "https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall.ws?table=0&page="}

    def process_all_hiscore_pages(self, page_number):
        # Determine the type of hiscores query
        print(">>> Extracting all players from: %s" % self.account_type)

        if self.account_type not in self.base_urls:
            print(">>> Error: Not a correct account type...")
            print("  > Valid inputs: overall, ironman, ultimate, hardcore, deadman, seasonal")
        
        # Create a dir for output
        if not os.path.exists(self.account_type):
            os.makedirs(self.account_type)

        # Set the base URL, it only needs a page number appended
        base_url = self.base_urls[self.account_type]

        self.page_number = page_number

        while True:
            # Print processing message
            sys.stdout.write(">>> Processing page %d\r" % self.page_number)
            
            # Construct a URL for the query
            url = base_url + str(self.page_number)

            # Call the method to process a single page
            full_page = self.process_single_hiscore_page(url)

            # Increment the page number
            self.page_number += 1

            if not full_page:
                break

    def process_single_hiscore_page(self, url):
        # Boolean to check if the page is full (25 players)
        full_page = False
        
        # Use the requests library to fetch the page content
        page = requests.get(url)

        # Convert the page content to an lxml html element
        tree = html.fromstring(page.content)

        # Parse all <tr><td>s
        players = tree.xpath('//tr/td//text()')

        # Clean the HTML table extracted entries
        # Remove line breaks (\n) in extracted table entries
        players = [p.strip() for p in players]
        # Remove empty items in list
        players = list(filter(None, players))

        # Each page should produce a list of 25 players * 4 entries
        # This means the list should be 100 entries long
        if len(players) == 100:
            full_page = True

        # Loop trough every 4 items for each player
        for rank, name, level, xp in zip(*[iter(players)]*4):
            name = name.replace("\xa0", " ")

            rank = rank.replace(",", "")
            rank = int(rank)

            level = level.replace(",", "")
            level = int(level)

            xp = xp.replace(",", "")
            xp = int(xp)

            if self.lookup_player:
                hpsl = HiscoresPlayerScraperLite(name, self.account_type)
                hiscores = hpsl.get_players_hiscore_lite()
                # Make a JSON output
                json_obj = { name : hiscores}
                json_out = self.account_type + os.sep + str(rank) + ".json"
                with open(json_out, "w") as f:
                    json.dump(json_obj, f, indent=4)
            else:
                # Make a JSON output
                json_out = self.account_type + os.sep + str(rank) + ".json"
                json_obj = {"rank": rank, "name": name, "level": level, "xp": xp}
                with open(json_out, "w") as f:
                    json.dump(json_obj, f, indent=4)

        # Return if the page was full
        # This means there is next page to process
        return full_page

    def print_output(self):
        for player in self.all_players:
            print(player, self.all_players[player])
