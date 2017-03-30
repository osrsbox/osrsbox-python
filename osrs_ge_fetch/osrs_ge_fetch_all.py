import os
import urllib.request
import json
import string
import time
import requests

# Specify all split URLs to later built URL to fetch
# start = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1&alpha=a&page=1"
base_url = "http://services.runescape.com/m=itemdb_oldschool/api/catalogue/items.json?category=1"
alpha_url = "&alpha="
page_url = "&page="

# Make a list of lowercase letters to iterate
alpha = string.ascii_lowercase

# Specify URL components (used to iterate)
alpha_req = 0
page_req = 1

# Build GET request suffix (end)
url_suffix = alpha_url + alpha[alpha_req] + page_url + str(page_req)

# Build the URL
url = (base_url + url_suffix)

# Set the total count to the total count number
# that is provided by the OSRS GE API
# This is in the first JSON file       
total = 0

# This first request is processed again later,
# so there is no need to add to our dict
page = urllib.request.urlopen(url).read().decode("utf-8")
page = json.loads(page)

# Parse the total number of items from the first 
# OSRS GE page and add to our "total" variable
total = int(page['total'])

print(">>> Total number of items in the OSRS GE: ", total)

done = 0 # Count of how many items have been processed

# Loop while we have processed less than the total number
# of items in the OSRS GE
while done <= total:
    
    # Build GET request suffix (end)
    url_suffix = alpha_url + alpha[alpha_req] + page_url + str(page_req)

    # Build the URL
    url = (base_url + url_suffix)
    
    # Print the URL, to let user see process
    print("  >  Current URL:", url_suffix)           
           
    # Fetch the URL from the OSRS GE API
    page = requests.get(url).json()
    
    # Increase done count by 12
    # This is becuase each JSON from each page
    # has a total of 12 items
    done += len(page['items'])

    # Print a process indicator
    print("  >  Processed: %d out of %d items, %.2f%% done" % (done, total, done/total))
    
    # For each item in the list of items:
    # Add item to "all_items" dict
    for item in page['items']:
        #all_items[item["id"]] = item # Save to a dict?
        out_fn = "json_dump_2017-03-31" + os.sep + str(item["id"]) + ".json"
        with open(out_fn, 'w') as outfile:
            json.dump(item, outfile)
        
    # Handle next page
    if len(page['items']) < 12:
        # Increase alpha counter for next letter
        alpha_req += 1
        # Reset page counter to 1, for new letter
        page_req = 1
    else:
        # Increase category page interator
        page_req += 1
    
    # Sleep for 8 seconds, to limit requests
    time.sleep(8)
    