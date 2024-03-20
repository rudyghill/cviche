import re
import sys
import csv


# TODO: make test function
# takes a csv and returns the csv reader, list of objects
# input filename: name of csv file to read
# output csv_reader: list of objects
def csv_to_table(filename):

    with open(filename, "r") as fin:
        csv_reader = csv.DictReader(fin, delimiter=",")
        table = list(csv_reader)
    return table


def replace_placeholders(document, replacements):
    """
    Replaces placeholders in a document string with corresponding values.

    Args:
        document (str): The document string containing placeholders.
        replacements (dict): A dictionary where keys are placeholders and values are replacements.

    Returns:
        str: The document string with placeholders replaced by their corresponding values.

    Example:
        >>> document = "Hello {{name}}, today is {{day}}"
        >>> replacements = {"name": "Alice", "day": "Monday"}
        >>> replace_placeholders(document, replacements)
        'Hello Alice, today is Monday'
    """
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
    return [
        {**line, key: [item.strip() for item in line[key].split(",")]} for line in table
    ]


# function that takes an list of objects and filters them by a specific key
# input table: the list of objects
# input key: the key to filter by
# input value: the value to filter by
# output filterd_table: the filtered table
def filter_by_key(table, key, value):
    return [obj for obj in table if key in obj and obj[key] == value]


# function that makes a list of items when tags are found
# input table: the list of objects
# input select: the field to make a list of
# input key: the field the key to check
# input tag: the string to search for in key
# output selected: list of selected items
def select_values_with_tag(table, select, key, tag):
    return [item[select] for item in table if tag in item[key].lower()]


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
