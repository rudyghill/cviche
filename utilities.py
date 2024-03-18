import re
import sys


def replace_placeholders(document, replacements):
    for placeholder, value in replacements.items():
        pattern = re.compile(re.escape("{{" + placeholder + "}}"))
        if type(value) == str:
            document = re.sub(pattern, value, document)
    return document


# TODO: make testing function
# converts the string value of an object to a python list
# input table: array of objects where object = {..., "key","string"}
# input key: see above, key to change
# output : transformed array of objects
def reformat_object_string(table, key):
    reformatted_table = []
    for line in table:
        value = line[key].split(",")
        reformatted_table.append(list(map(lambda x: x.strip(), value)))
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
