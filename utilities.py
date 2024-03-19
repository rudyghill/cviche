import re
import sys
import csv


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


# TODO: make test function
# takes a csv and returns the csv reader, list of objects
# input filename: name of csv file to read
# output csv_reader: list of objects
def csv_to_table(filename):

    with open(filename, "r") as fin:
        csv_reader = csv.DictReader(fin, delimiter=",")
        table = list(csv_reader)
    return table


# function that takes an list of objects and filters them by a specific key
# input table: the list of objects
# input key: the key to filter by
# input value: the value to filter by
# output filterd_table: the filtered table
def filter_by_key(table, key, value):
    filtered_table = [obj for obj in table if key in obj and obj[key] == value]
    return filtered_table


# function that makes a list of items when tags are found
# input table: the list of objects
# input select: the field to make a list of
# input key: the field the key to check
# input tag: the string to search for in key
# output selected: list of selected items
def select_values_with_tag(table, select, key, tag):
    selected = []
    for item in table:
        if tag in item[key].lower():
            selected.append(item[select])
    return selected


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
