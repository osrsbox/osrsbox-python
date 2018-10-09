# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/10/10

Description:
Determine a players lowest skill (good for Tears of Guthix Minigame)

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

# Import HiscoresAPI class
sys.path.append(os.getcwd())
import HiscoresAPI

player_name = input(">>> Enter your player name: ")

# Create object for using Player Scraper Lite
hpsl = HiscoresAPI.HiscoresPlayerScraperLite(player_name, "overall")

# Determine the players hiscore (and return dict/json object)
hiscores = hpsl.get_players_hiscore_lite()

skill_list = dict()

for skill in hiscores:
    skill_list[skill] = hiscores[skill]["xp"]

sorted_skills = sorted(skill_list.items(), key=lambda x: int(x[1]))
    
for skill in sorted_skills:
    print(skill)
