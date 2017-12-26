import urllib.request
import json
import requests
import collections

base_url = "http://services.runescape.com/m=hiscore_oldschool/index_lite.ws?player="
player_name = input("Enter your player name:")

url = base_url + player_name

print(">>> %s" % url)

page = urllib.request.urlopen(url).read().decode("utf-8")

page = page.split("\n")

skills = ["Overall",
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
         
hiscores = list()         
Skill = collections.namedtuple('Skill', 'name rank level xp')         
         
for i, skill in enumerate(skills):
    line = page[i].split(",")
    parse_skill = Skill(name=skill, rank=int(line[0]), level=int(line[1]), xp=int(line[2]))
    hiscores.append(parse_skill)

hiscores.sort(key=lambda x:x.xp)
    
for skill in hiscores:
    print(skill.name, skill.xp)