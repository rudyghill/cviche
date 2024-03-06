import sys
import csv


def skills_csv(filename, tag):
    selected = []
    with open(filename, "r") as fin:
        csv_reader = csv.DictReader(fin, delimiter=",")
        for line in csv_reader:
            tags = line["tags"].split(",")
            line["tags"] = list(map(lambda x: x.strip().lower(), tags))
            if tag in line["tags"]:
                selected.append(line["skill"])
    return csv_reader, selected


def skills(filename, tag):
    return skills_csv(filename, tag)


# TODO: safegaurd against no filename
if __name__ == "__main__":
    master, selected = skills(sys.argv[1], sys.argv[2])
    print(*selected, sep=", ")
# import json
# print(json.dumps(master)) #can dump into a json file later
