import argparse
import utilities

# import json
# print(json.dumps(master)) #can dump into a json file later


def experience():
    return


def education():
    return


def skills(filename, tag):
    master = utilities.csv_to_table(filename)
    return utilities.select_values_with_tag(master, "skill", "tags", tag)


def main():
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
    args = parser.parse_args()

    if args.mode == "exp":
        experience()
    elif args.mode == "edu":
        education()
    elif args.mode == "skl":
        selected = skills(args.csv, args.tag)
        print(*selected, sep=", ")
    else:
        ("Invalid argument")


if __name__ == "__main__":
    main()
