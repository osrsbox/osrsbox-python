
# !/usr/bin/python

"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: osrsbox.com
Date:    2017/06/03

Description:
osrs_ge_fetch_all.py is a simple Python program that queries the Old School
RuneScape (OSRS) Grand Exchange (GE) for every currently tradeable item.
All GE pages (containing JSON formatted information) are queried and items
are processed and saved as a single JSON file for each item ID number.

Copyright (c) 2017, PH01L
###############################################################################
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/
###############################################################################
"""

import os
import sys
import urllib.request
import json
import string
import time
import requests
import argparse
import logging

def fetch_page(url):
    page = requests.get(url)
    if page.status_code != requests.codes.ok:
        logging.info("  > ERROR fetching page. Status code: &s" % page.status_code)
        time.sleep(8)
        fetch_page(url)
    else:
        json_obj = page.json()
        return json_obj

def query_osrs_ge(verbose):
    # Specify all split URLs to later built URL to fetch
    # base_url is the start of the URL for the OSRS GE for all pages
    base_url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1"
    # The OSRS GE API splits data into categories (letters then page numbers)
    # alpha_url should be followed by a letter from a-z
    alpha_url = "&alpha="
    # page_url is a number, size depends on the number of items
    # in a specific alpha category
    page_url = "&page="

    # Make a list of lowercase letters to iterate alpha_url
    alpha = string.ascii_lowercase

    # Specify URL components (used to iterate)
    alpha_req = 0
    page_req = 1

    # Build GET request suffix (end), to append to base_url
    url_suffix = alpha_url + alpha[alpha_req] + page_url + str(page_req)

    # Build the URL
    url = (base_url + url_suffix)

    # Set up a total count. The total count of unique items is 
    # provided by the OSRS GE API in the first JSON file       
    total = 0

    # This first request is processed again later,
    # so there is no need to add to our dict of data
    page = urllib.request.urlopen(url).read().decode("utf-8")
    page = json.loads(page)

    # Parse the total number of items from the first 
    # OSRS GE page and add to our "total" variable
    total = int(page['total'])

    print(">>> Total number of items in the OSRS GE: ", total)
    if verbose: logging.info(">>> Total number of items in the OSRS GE: %d" % total)

    done = 0 # Count of how many items have been processed
    saved = 0 # Count of how many items have been saved

    # Loop while we have processed less than the total number
    # of items in the OSRS GE
    while done <= total:
        
        # Build GET request suffix (end)
        url_suffix = alpha_url + alpha[alpha_req] + page_url + str(page_req)

        # Build the URL
        url = (base_url + url_suffix)
        
        # If verbose mode, log entire URL
        if verbose: logging.info("  > Current URL: %s" % url)

        # Fetch the URL from the OSRS GE API
        page = fetch_page(url)
                 
        # Increase done count by length of items that page returns
        done += len(page['items'])
        # If verbose mode, log how many items are to be processed
        if verbose: logging.info("  > Number of items on page: %d" % len(page['items']))

        # Print a process indicator
        percentage = float(done/total)*100
        print("  > Processed: %d out of %d items, %.2f%% done" % (done, total, percentage))
        logging.info("  > Processed: %d out of %d items, %.2f%% done" % (done, total, percentage))
        
        # For each item in the list of items:
        # Add item to "all_items" dict
        for item in page['items']:
            # Save the entire JSON for one item into a local JSON file
            out_fn = str(item["id"])[:1] + os.sep + str(item["id"]) + ".json"
            with open(out_fn, 'w') as outfile:
                json.dump(item, outfile)
            saved += 1
        
        # Print how many items have been saved
        percentage = float(saved/total)*100
          
        # Handle next page
        if len(page['items']) < 12:
            # Increase alpha counter for next letter
            alpha_req += 1
            if alpha_req >= 26:
                print(">>> Finished grabbing all items...")
                print(">>> Looks like we fetched less items then reported by OSRS GE.")
                print(">>> Exiting...")
                quit()
            # Reset page counter to 1, for new letter
            page_req = 1
        else:
            # Increase category page interator
            page_req += 1
        
        # Sleep for 8 seconds, to limit requests
        time.sleep(8)
    
################################################################################
if __name__=="__main__":
    parser = argparse.ArgumentParser(description='''
osrs_ge_fetch_all.py is a simple Python program that queries the Old School
RuneScape (OSRS) Grand Exchange (GE) for every currently tradeable item.
All GE pages (containing JSON formatted information) are queried and items
are processed and saved as a single JSON file for each item ID number.''')
    parser.add_argument("-v", action="store_true", help = "Verbose")
    args = parser.parse_args()
    
    # First make output directories
    directories = list(range(10))
    for directory in directories:
        directory = str(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)
    
    if args.v: verbose = True
    
    if verbose:
        log = "osrs_ge_fetch_all.log"
        logging.basicConfig(filename = log,
                            level=logging.DEBUG,
                            format = '%(message)s')
        logging.info("Starting processing ...")

    query_osrs_ge(verbose)
    