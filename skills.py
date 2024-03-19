import sys
import utilities


# TODO: delete function
def skills(filename, tag):
    master = utilities.csv_to_table(filename)
    selected = utilities.select_values_with_tag(master, "skill", "tags", tag)
    return master, selected


# TODO: safegaurd against no filename
if __name__ == "__main__":
    master = utilities.csv_to_table(sys.argv[1])
    selected = utilities.select_values_with_tag(master, "skill", "tags", sys.argv[2])
    # master, selected = skills(sys.argv[1], sys.argv[2])
    print(*selected, sep=", ")
# import json
# print(json.dumps(master)) #can dump into a json file later
