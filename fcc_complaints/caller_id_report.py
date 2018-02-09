#!/usr/bin/env python
"""
Check how many complaints each phone number has from a csv file input.

Usage:
python3 -m fcc_complaints.caller_id_report -i input.csv -o /tmp/output.csv --cid_column=number
"""
import csv

from fcc_complaints import FccApi

COMPLAINTS_FIELD = 'num_complaints'
DEFAULT_CID_FIELD = 'cid'


def main(input_path, output_path, cid_column=DEFAULT_CID_FIELD):
    api = FccApi()
    reader = csv.DictReader(open(input_path))
    fieldnames = list(reader.fieldnames) + [COMPLAINTS_FIELD]
    writer = csv.DictWriter(open(output_path, 'w'), fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        new_row = row.copy()
        try:
            new_row[COMPLAINTS_FIELD] = len(api.query(caller_id_number=row[cid_column]))
        except Exception as e:
            new_row[COMPLAINTS_FIELD] = str(e)
        writer.writerow(new_row)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Check complaints on caller id number from csv file input. '
                                                 'Appends a column {} to the csv. '.format(COMPLAINTS_FIELD))
    parser.add_argument('-c', '--cid_column', help='The column in the csv with the caller id number.',
                        default=DEFAULT_CID_FIELD)
    parser.add_argument('-i', '--input', help='The input csv file. ', required=True)
    parser.add_argument('-o', '--output', help='The output csv file. ', required=True)

    args = parser.parse_args()
    main(input_path=args.input, output_path=args.output, cid_column=args.cid_column)
