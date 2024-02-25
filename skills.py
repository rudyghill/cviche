# initialize json
master = []
selected = []
import sys

# TODO: safegaurd against no filename
filename = sys.argv[1]
tag = sys.argv[2]
with open(filename, "r") as fin:
    for line in fin:
        skill, *tags = line.strip().split(",")
        skill = skill.strip()
        tags = list(map(lambda x:x.strip().lower(),tags))
        master.append(dict(skill=skill, tags=tags))
        if tag in tags:
            selected.append(skill)

print(*selected, sep=",")
# import json
# print(json.dumps(master)) #can dump into a json file later
