import argparse
import utilities
import sys

from pathlib import Path
from enum import Enum, auto

class Modes(Enum):
   exp = auto()
   edu = auto()
   skl = auto()
# import json
# print(json.dumps(master)) #can dump into a json file later


def experience(template: Path, csv: Path, tag) -> str:
    master = utilities.csv_to_table(csv)
    selected = utilities.filter_by_key(master, "tag", tag)
    replacements = selected[0]
    return utilities.replace_placeholders(template, replacements)


def education():
    return


def skills(filename, tag):
    master = utilities.csv_to_table(filename)
    return utilities.select_values_with_tag(master, "skill", "tags", tag)

def _get_arg_parser():
    parser = argparse.ArgumentParser(description="generate a resume")
    parser.add_argument(
        "-m",
        "--mode",
        help="mode to change behavior",
        choices=["exp", "edu", "skl"],
        required=True,
    )
    parser.add_argument("-c", "--csv", help="csv file to read", required=True)
    parser.add_argument("-t", "--tag", help="tag to filter on", required=True)
    return parser

def from_args(args: dict):
    pass

def main():
    parser = _get_arg_parser()
    args = parser.parse_args()

    if args.mode is Modes.exp:
        template = sys.stdin.read()
        modified_document = experience(template, args.csv, args.tag)
        sys.stdout.write(modified_document)
    elif args.mode == "edu":
        education()
    elif args.mode == "skl":
        selected = skills(args.csv, args.tag)
        print(*selected, sep=", ")
    else:
        ("Invalid argument")


if __name__ == "__main__":
    main()
