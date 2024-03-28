import re
import sys
import csv
from pathlib import Path
import yaml


# TODO: make test function
# takes a csv and returns the csv reader, list of objects
# input filename: name of csv file to read
# output csv_reader: list of objects
def csv_to_table(filename: Path):
    with open(filename, "r") as fin:
        csv_reader = csv.DictReader(fin, delimiter=",")
        table = list(csv_reader)
    return table


def read_file(filename: Path) -> str:
    with open(filename, "r") as fin:
        contents = fin.read()
    return contents


def write_file(filename: Path, contents: str):
    with open(filename, "w") as fin:
        fin.write(contents)


def process_config(filename: Path) -> dict:
    with open(filename, "r") as file:
        data = yaml.safe_load(file)
    data["template"] = read_file(data["template"])
    sections = data["sections"]
    expanded_sections = {
        key: {
            **value,
            "template": read_file(value["template"]),
            "csv": csv_to_table(value["csv"]),
        }
        for key, value in sections.items()
    }
    data["sections"] = expanded_sections
    return data


def replace_placeholders(document: str, replacements: dict[str, str]) -> str:
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
        else:
            raise RuntimeError(f"Unexpected {value=}!!")
    return document


def expand_to_list(table: list[dict], key: str) -> list[dict]:
    """
    Converts the string value of a specified key in each object of the input table to a Python list.

    Args:
        table (list[dict]): An array of objects (dictionaries) where each object contains the specified key.
        key (str): The key in each object dictionary whose string value will be converted to a Python list.
                   Each string value is assumed to be a comma-separated list of items.

    Returns:
        list[dict]: A transformed array of objects where each object's specified key now contains a Python list
                    obtained by splitting the original string value by commas and stripping whitespace from each item.

    Example:
        Suppose we have a list of dictionaries representing items:
        table = [
            {'id': 1, 'tags': 'apple, banana, orange'},
            {'id': 2, 'tags': 'grape, pear'},
            {'id': 3, 'tags': 'melon'}
        ]

        To convert the 'tags' key of each item into a list of tags:
        expanded_table = expand_to_list(table, 'tags')

        The resulting expanded_table would be:
        [
            {'id': 1, 'tags': ['apple', 'banana', 'orange']},
            {'id': 2, 'tags': ['grape', 'pear']},
            {'id': 3, 'tags': ['melon']}
        ]
    """
    return [
        {**line, key: [item.strip() for item in line[key].split(",")]} for line in table
    ]


def filter_by_key(table: list[dict], key: str, value: str) -> list[dict]:
    """
    Filters a list of objects based on a specific key and value.

    Args:
        table (list[dict]): The list of objects (dictionaries) to filter.
        key (str): The key in each object dictionary to filter by.
        value (str): The value to filter by within the specified key.

    Returns:
        list[dict]: A filtered list of objects where each object has the specified key
                    and the value associated with that key matches the given value.

    Example:
        Suppose we have a list of dictionaries representing items:
        table = [
            {'name': 'apple', 'color': 'red'},
            {'name': 'banana', 'color': 'yellow'},
            {'name': 'orange', 'color': 'orange'}
        ]

        To filter the table by the key 'color' and value 'red':
        filtered_table = filter_by_key(table, 'color', 'red')

        The resulting filtered_table would be:
        [{'name': 'apple', 'color': 'red'}]
    """
    return [obj for obj in table if key in obj and value in obj[key]]


def select_values_with_tag(
    table: list[dict], select: str, key: str, tag: str
) -> list[str]:
    """
    Creates a list of selected values from objects in the input table where a specified tag is found in a specified key.

    Args:
        table (list[dict]): The list of objects (dictionaries) to filter.
        select (str): The field (key) in each object from which to extract values for the resulting list.
        key (str): The field (key) in each object where the specified tag will be searched.
        tag (str): The string to search for (case-insensitive) within each object's `key`.

    Returns:
        list: A list of selected values (`select`) from objects where `tag` is found in `key` (case-insensitive).

    Example:
        Suppose we have a list of dictionaries representing items:
        table = [
            {'name': 'apple', 'tags': 'fruit, red, delicious'},
            {'name': 'banana', 'tags': 'fruit, yellow, tropical'},
            {'name': 'orange', 'tags': 'fruit, orange, citrus'}
        ]

        To select the 'name' values from objects where the 'tags' contain the tag 'citrus':
        selected_items = select_values_with_tag(table, 'name', 'tags', 'citrus')

        The resulting selected_items would be:
        ['orange']
    """
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
