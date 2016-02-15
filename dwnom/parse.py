#!/usr/bin/env python

import csv
import json


try:
    from itertools import izip_longest  # added in Py 2.6
except ImportError:
    from itertools import zip_longest as izip_longest  # name change in Py 3.x

try:
    from itertools import accumulate  # added in Py 3.2
except ImportError:
    def accumulate(iterable):
        'Return running totals (simplified version).'
        total = next(iterable)
        yield total
        for value in iterable:
            total += value
            yield total

# CURRENT_NAMES_URL = 'ftp://voteview.com/S01114NW_DECEMBER_2015.TXT'
# CURRENT_SCORES_URL = 'ftp://voteview.com/junkord/SC01114B21.DAT'

FIELDS = [
    (4, 'congress'),
    (6, 'icpsr_id_number'),
    (3, 'state_code'),
    (2, 'congressional_district'),
    (9, 'state_name'),
    (5, 'party'),
    (14, 'name'),
    (10, 'first_dimension'),
    (9, 'second_dimension'),
    (10, 'log_likelihood'),
    (8, 'number_of_votes'),
    (4, 'number_of_classification_errors'),
    (5, 'geometric_mean_probability')
]

def make_parser(fieldwidths):
    cuts = tuple(cut for cut in accumulate(abs(fw) for fw in fieldwidths))
    pads = tuple(fw < 0 for fw in fieldwidths)
    flds = tuple(izip_longest(pads, (0,)+cuts, cuts))[:-1]
    parse = lambda line: tuple(line[i:j] for pad, i, j in flds if not pad)
    parse.size = sum(abs(fw) for fw in fieldwidths)
    parse.fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's') for fw in fieldwidths)
    return parse

def parse_row(row):
    line = row
    fieldwidths = tuple(l for l,k in FIELDS)
    parse = make_parser(fieldwidths)
    fieldnames = [k for l,k in FIELDS]
    payload = dict(zip(fieldnames, list(parse(line))))
    for k,v in payload.items():
        payload[k] = v.strip()
    for k,v in payload.items():
        if k == 'party':
            if v == '200':
                payload[k] = 'Republican'
            if v == '100':
                payload[k] = 'Democrat'
    return payload

def load_data():
    with open('data/senate/senate_dw_nominate.txt', 'r') as readfile:
        rows = list(readfile.read().split('\n'))

    payload = []

    for row in rows:
        if row != '':
            row = parse_row(row)
            if row['congress'] == '114':
                payload.append(row)

    with open('output.csv', 'w') as csvfile:
        fieldnames = [k for l,k in FIELDS]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for r in payload:
            writer.writerow(r)

def main():
    load_data()

if __name__ == "__main__":
    main()