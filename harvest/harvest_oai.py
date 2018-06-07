#!/usr/bin/env python

import argparse
import os
import sys

import lxml.etree as etree

from sickle import Sickle


def prettify_xml(xml_str):
    return etree.tostring(
        etree.fromstring(xml_str),
        pretty_print=True
    )


def warn(msg, *args, **kwargs):
    print(msg.format(*args, **kwargs), file=sys.stderr)


def get_args():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-r", "--max-retries",
        type=int,
        default=3
    )
    arg_parser.add_argument(
        "-f", "--format",
        default="dcx"
    )
    arg_parser.add_argument(
        "-s", "--record-set",
        required=True
    )
    arg_parser.add_argument(
        "-u", "--base-url",
        required=True
    )
    arg_parser.add_argument(
        "-o", "--output-dir"
    )
    return arg_parser.parse_args()


def main():
    args = get_args()

    sickle = Sickle(args.base_url)

    warn("getting records...")
    records = sickle.ListRecords(
        metadataPrefix=args.format,
        set=args.record_set,
        ignore_deleted=True,
        max_retries=args.max_retries
    )
    try:
        processed = 0
        for record in records:
            record_id = record.header.identifier.replace(":", "-")
            path = os.path.join(args.output_dir, "{}.xml".format(record_id))
            with open(path, "w") as out:
                print(
                    prettify_xml(record.raw).decode("utf-8"),
                    file=out
                )
            processed += 1
            if processed % 100 == 0:
                warn("processed {} records".format(processed))
    except Exception as err:
        warn(
            "something went wrong: {}, resumption token is {}".format(
                err,
                records.resumption_token
            )
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

