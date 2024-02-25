# initialize json
# TODO: normalize input including case
master = []
selected = []
import sys

# TODO: safegaurd against no filename
filename = sys.argv[1]
tag = sys.argv[2]
with open(filename, "r") as fin:
    for line in fin:
        skill, *tags = line.replace(" ", "").strip().split(",")
        master.append(dict(skill=skill, tags=tags))
        if tag in tags:
            selected.append(skill)

print(*selected, sep=",")
# import json
# print(json.dumps(master)) #can dump into a json file later
