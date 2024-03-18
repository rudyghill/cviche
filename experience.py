import sys
import csv
import utilities


def experience(filename, tag):
    selected = []
    with open(filename, "r") as fin:
        csv_reader = csv.DictReader(fin, delimiter=",")
        for line in csv_reader:
            skills = line["skills"].split(",")
            line["skills"] = list(map(lambda x: x.strip(), skills))
            if tag == line["tag"]:
                selected.append(line)
    return csv_reader, selected


def main():
    # Read document from standard input
    template = sys.stdin.read()

    master, selected = experience(sys.argv[1], sys.argv[2])

    # Define replacements
    replacements = selected[0]

    # Replace placeholders
    modified_document = utilities.replace_placeholders(template, replacements)

    # Output modified document to standard output
    sys.stdout.write(modified_document)


if __name__ == "__main__":
    main()
