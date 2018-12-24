# osrsbox-python

A collection of Python scripts authored to parse and process certain OSRS data from a variety of sources.

## osrs_hiscores

A simple Python wrapper/API for fetching OSRS player hiscores from the official OSRS Hiscores web site and API.

## osrs_worlds

A simple python script named `scrape_worlds.py` that extracts all world (server) metadata from the official OSRS website and produces a structured JSON file, named `worlds.json`. The contents of the JSON file are listed below, with world 301 as an example.

```
{
    "301": {
    "country": "US",
    "members": false,
    "activity": "Trade - Free"
    }
}
```

## playerscraper_tools

The tools authored to process the output from my RuneLite plugin named playerscraper. Comprised of a simple Python class to handle each player (`PlayerScraper.py`) and a caller program (`parse_playerscraper.py`). The script will output CSV to standard output, as well as some basic statistics. Note: You will need a variety of files to run this script:

1. `summary.json`: OSBuddy's summary.json file about item prices
1. `worlds.json`: Output from my osrs_worlds Python tools
1. `items_itemscraper.json`: Item database filde from my osrsbox-db project

