import urllib.request
import json

url = "https://rsbuddy.com/exchange/summary.json"

page = urllib.request.urlopen(url).read().decode("utf-8")
page = json.loads(page)

out_fn = "summary_" + "2017-03-31" + ".json"
with open(out_fn, 'w') as outfile:
    json.dump(page, outfile)