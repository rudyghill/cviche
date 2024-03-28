import argparse
import sys
from pathlib import Path
from pprint import pprint

# import json
# print(json.dumps(master)) #can dump into a json file later
import utilities


def yaml_test(config: Path, tag: str):
    processed_config = utilities.process_config(config)
    master_template = processed_config["template"]
    output_filename = processed_config["output"]
    sections = processed_config["sections"]

    processed_sections = {}
    for section in sections:
        selected = utilities.filter_by_key(sections[section]["csv"], "tag", tag)
        output = ""
        for line in selected:
            output += utilities.replace_placeholders(
                sections[section]["template"], line
            )
        processed_sections[section] = output

    output_text = utilities.replace_placeholders(master_template, processed_sections)
    utilities.write_file(output_filename, output_text)

    return output_text


def _get_arg_parser():
    parser = argparse.ArgumentParser(description="generate a resume")
    parser.add_argument("-t", "--tag", help="tag to filter on", required=True)
    parser.add_argument("-y", "--yaml", help="yaml file to take in")
    return parser


def from_args(args: dict):
    pass


def main():
    parser = _get_arg_parser()
    args = parser.parse_args()

    if args.yaml:
        output = yaml_test(args.yaml, args.tag)
        # sys.stdout.write(output)
    else:
        ("Invalid argument")


if __name__ == "__main__":
    main()
