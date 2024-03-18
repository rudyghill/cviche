import re
import sys

def replace_placeholders(document, replacements):
    for placeholder, value in replacements.items():
        pattern = re.compile(re.escape('{{' + placeholder + '}}'))
        if type(value) == str:
            document = re.sub(pattern, value, document)
    return document

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