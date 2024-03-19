import sys
import utilities


def main():
    # Read document from standard input
    template = sys.stdin.read()

    master = utilities.csv_to_table(sys.argv[1])
    selected = utilities.filter_by_key(master, "tag", sys.argv[2])

    # Define replacements
    replacements = selected[0]

    # Replace placeholders
    modified_document = utilities.replace_placeholders(template, replacements)

    # Output modified document to standard output
    sys.stdout.write(modified_document)


if __name__ == "__main__":
    main()
