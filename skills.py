# initialize json
# TODO: normalize input including case
# TODO: create an example.csv
master = []
with open("skills.csv", "r") as fin:
    for line in fin:
        skill, score, *tags = line.replace(" ", "").strip().split(",")
        master.append(dict(skill=skill, score=int(score), tags=tags))

# import json
# print(json.dumps(master)) #can dump into a json file later

# print skills with certain tags
tag = "security"
for item in master:
    if tag in item["tags"]:
        print(item["skill"])
