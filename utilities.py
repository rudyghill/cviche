import re
import sys


# TODO: write test and function description
def replace_placeholders(document, replacements):
    for placeholder, value in replacements.items():
        pattern = re.compile(re.escape("{{" + placeholder + "}}"))
        if type(value) == str:
            document = re.sub(pattern, value, document)
    return document


# converts the string value of an object to a python list
# input table: array of objects where object = {..., "key":"string"}
# input key: see above, key to change
# output : transformed array of objects
def expand_to_list(table, key):
    reformatted_table = table
    for line in table:
        value = [item.strip() for item in line[key].split(",")]
        line[key] = value
    return reformatted_table


def main():
    # Read document from standard input
    document = sys.stdin.read()

    # Define replacements
    replacements = {
        "NAME": "John Doe",
        # Add more placeholders and their corresponding values here
    }

    # Replace placeholders
    modified_document = replace_placeholders(document, replacements)

    # Output modified document to standard output
    sys.stdout.write(modified_document)


if __name__ == "__main__":
    main()
