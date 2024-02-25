import sys

def skills(filename, tag):
    master = []
    selected = []
    with open(filename, "r") as fin:
        for line in fin:
            skill, *tags = line.strip().split(",")
            skill = skill.strip()
            tags = list(map(lambda x:x.strip().lower(),tags))
            master.append(dict(skill=skill, tags=tags))
            if tag in tags:
                selected.append(skill)
    return master, selected

# TODO: safegaurd against no filename
master, selected = skills(sys.argv[1], sys.argv[2])

print(*selected, sep=",")
# import json
# print(json.dumps(master)) #can dump into a json file later
