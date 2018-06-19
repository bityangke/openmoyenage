#!/usr/bin/env python

import argparse
import os
import shutil

import xml.etree.ElementTree as etree


def parse_xml_without_schema(file_path):
    it = etree.iterparse(file_path)
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1]
    return it.root


def extract_date(xml):
    element = xml.find(".//date")
    if element is not None:
        return element.text
    return None


def contains_person(xml):
    for el in xml.findall(
        ".//subject[@{http://www.w3.org/2001/XMLSchema-instance}type='iconclass']"
    ):
        if el.text.startswith("31"):
            return True
    return False


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("record_directory")
    arg_parser.add_argument("output_directory")
    args = arg_parser.parse_args()

    for filename in os.listdir(args.record_directory):
        if not filename.endswith(".xml"):
            continue

        record_path = os.path.join(args.record_directory, filename)
        xml = parse_xml_without_schema(record_path)
        if contains_person(xml):
            shutil.copy(
                record_path,
                os.path.join(args.output_directory, filename)
            )


if __name__ == "__main__":
    main()

