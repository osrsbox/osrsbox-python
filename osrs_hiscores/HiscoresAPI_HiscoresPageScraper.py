# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2018/10/10

Description:
Example of how to scrape the overall hiscores using the HiscoreAPI class

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
import argparse

# Import HiscoresAPI class
sys.path.append(os.getcwd())
import HiscoresAPI

################################################################################
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='''
HiscoresAPI_HiscoresPageScraper.py is a simple Python program that queries the 
Old School RuneScape (OSRS) Hiscores for a specific account type (overall, 
ironman, ultimate ironman, or hardcore ironman).''')
    parser.add_argument("-t", action="store", help="Account type")
    args = parser.parse_args()
    
    if args.t:
        account_type = args.t
    else:
        print(">>> You didn't enter an account type with the -t option")
        print("  > So using the 'overall' hiscores...")
        account_type = "overall"

    # Create object for using Player Scraper Lite, then start scraping
    hps = HiscoresAPI.HiscoresPageScraper(account_type, False)
    hps.process_all_hiscore_pages(1)
