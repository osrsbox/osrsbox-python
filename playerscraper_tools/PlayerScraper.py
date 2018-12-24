# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/12/25

Description:
PlayerScraper.py is an API to help process JSON files from the RuneLite 
Player Scraper plugin. Example JSON provided below:

{
  "player":"NoNameSteve",
  "combat":3,
  "world":307,
  "head":{
    "name":"Zamorak halo",
    "id":12638
  },
  "weapon":{
    "name":"Mouse toy",
    "id":6541
  },
  "shield":{
    "name":"Lit bug lantern",
    "id":7053
  },
  "hands":{
    "name":"Graceful gloves",
    "id":13676
  },
  "torso":{
    "name":"Banshee top",
    "id":20775
  },
  "legs":{
    "name":"Anti-panties",
    "id":13288
  },
  "boots":{
    "name":"Mime boots",
    "id":3061
  },
  "cape":{
    "name":"Thieving cape(t)",
    "id":9778
  },
  "amulet":{
    "name":"Gnome scarf",
    "id":9470
  }
}

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

import json

###############################################################################
# Helper methods
def _strcast(val):
    """ Convert value to string. """
    if val is None:
        return None
    return str(val)

def _intcast(val):
    """ Convert input to integer. """
    if val is None:
        return None
    if isinstance(val, int):
        return val
    if isinstance(val, str):
        return int(val)

###############################################################################
class PlayerScraper(object):
    def __init__(self):
        # Dict of all ItemDefinition properties
        self.properties = {
            "player" : None,
            "world" : None,
            "combat" : None,
            "head" : None,
            "cape" : None,
            "amulet" : None,
            "weapon" : None,
            "torso" : None,
            "shield" : None,
            "legs" : None,
            "hands" : None,
            "boots" : None}

        # Below are lists to help automate parsing of JSON file
        # Some items are nested in the JSON structure
        self.not_nested = [
            "player", 
            "world", 
            "combat"]

        self.nested = [
            "head", 
            "cape", 
            "amulet", 
            "weapon", 
            "torso", 
            "shield", 
            "legs", 
            "hands",
            "boots"]

        self.nested_cost = [
            "cost_head", 
            "cost_cape", 
            "cost_amulet", 
            "cost_weapon", 
            "cost_torso", 
            "cost_shield", 
            "cost_legs", 
            "cost_hands",
            "cost_boots"]       

    ###############################################################################
    # Setters and Getters
    @property
    def player(self):
        return self._player
    @player.setter
    def player(self, value):
        self._player = _strcast(value)

    @property
    def world(self):
        return self._world
    @world.setter
    def world(self, value): 
        self._world = _intcast(value) 

    @property
    def combat(self):
        return self._combat
    @combat.setter
    def combat(self, value):
        self._combat = _intcast(value)                

    # Equipment slots
    @property
    def head(self):
        return self._head
    @head.setter
    def head(self, value):
        self._head = _intcast(value)	  

    @property
    def cape(self):
        return self._cape
    @cape.setter
    def cape(self, value):
        self._cape = _intcast(value)	

    @property
    def amulet(self):
        return self._amulet
    @amulet.setter
    def amulet(self, value):
        self._amulet = _intcast(value)	

    @property
    def weapon(self):
        return self._weapon
    @weapon.setter
    def weapon(self, value):
        self._weapon = _intcast(value)

    @property
    def torso(self):
        return self._torso
    @torso.setter
    def torso(self, value):
        self._torso = _intcast(value)                       

    @property
    def shield(self):
        return self._shield
    @shield.setter
    def shield(self, value):
        self._shield = _intcast(value)  

    @property
    def legs(self):
        return self._legs
    @legs.setter
    def legs(self, value):
        self._legs = _intcast(value) 

    @property
    def hands(self):
        return self._hands
    @hands.setter
    def hands(self, value):
        self._hands = _intcast(value)         

    @property
    def boots(self):
        return self._boots
    @boots.setter
    def boots(self, value):
        self._boots = _intcast(value) 

    # Equipment slot costs
    @property
    def cost_head(self):
        return self._cost_head
    @cost_head.setter
    def cost_head(self, value):
        self._cost_head = _intcast(value)	  

    @property
    def cost_cape(self):
        return self._cost_cape
    @cost_cape.setter
    def cost_cape(self, value):
        self._cost_cape = _intcast(value)	

    @property
    def cost_amulet(self):
        return self._cost_amulet
    @cost_amulet.setter
    def cost_amulet(self, value):
        self._cost_amulet = _intcast(value)	

    @property
    def cost_weapon(self):
        return self._cost_weapon
    @cost_weapon.setter
    def cost_weapon(self, value):
        self._cost_weapon = _intcast(value)

    @property
    def cost_torso(self):
        return self._cost_torso
    @cost_torso.setter
    def cost_torso(self, value):
        self._cost_torso = _intcast(value)                       

    @property
    def cost_shield(self):
        return self._cost_shield
    @cost_shield.setter
    def cost_shield(self, value):
        self._cost_shield = _intcast(value)  

    @property
    def cost_legs(self):
        return self._cost_legs
    @cost_legs.setter
    def cost_legs(self, value):
        self._cost_legs = _intcast(value) 

    @property
    def cost_hands(self):
        return self._cost_hands
    @cost_hands.setter
    def cost_hands(self, value):
        self._cost_hands = _intcast(value)         

    @property
    def cost_boots(self):
        return self._cost_boots
    @cost_boots.setter
    def cost_boots(self, value):
        self._cost_boots = _intcast(value)         

    ###########################################################################
    # Processing functions
    def load(self, fi):
        # print(">>> Loading player file...")
        with open(fi) as f:
            input = json.load(f)
        
        # print(">>> Populating player, combat and world...")
        for prop in self.not_nested:
            setattr(self, prop, input[prop]) 

        # print(">>> Populating player equipment...")
        for prop in self.nested:
            try:
                setattr(self, prop, input[prop]["id"])
            except KeyError:
                setattr(self, prop, None)

        self.is_naked = False
        equiped_count = 0
        for prop in self.nested:
            attr = getattr(self, prop)
            if attr is not None:
                equiped_count += 1
        if equiped_count == 0:
            self.is_naked = True

        return self    

    def calc_wealth(self, summary, allitems):        
        # Determine the total wealth of player equipment items
        # Also determine the cost for each slot
      
        # Determine total wealth (sum all item slots)
        current_wealth = 0
        for prop in self.nested:
            id = str(getattr(self, prop))
            if id is None:
                continue
            
            try:
                item_wealth = summary[id]["overall_average"]
            except KeyError:
                item_wealth = 0

            if item_wealth == 0:
                try:
                    item_wealth = allitems[id]["cost"]
                except KeyError:
                    item_wealth = 0

            # Put item wealth into cost_"prop"
            new_prop = "cost_" + prop
            setattr(self, new_prop, item_wealth)
            current_wealth += item_wealth

        self.wealth = current_wealth

    def determine_world(self, worlds):         
        # Grab the metadata about the players world (from worlds.json)
        self.world_country = worlds[str(self.world)]["country"]
        self.world_members = worlds[str(self.world)]["members"]
        self.world_activity = worlds[str(self.world)]["activity"]
        
        # Determine if world is restricted by total level
        total_level_worlds = ["2200", "2000", "1750", "1500", "1250"]
        self.world_requirement = False
        if self.world_activity:
            for world in total_level_worlds:
                if world in self.world_activity:
                    self.world_requirement = True
