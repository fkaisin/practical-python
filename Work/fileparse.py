# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    # with open(filename, 'rt') as f:
    rows = csv.reader(lines, delimiter=delimiter)
    records = []

    # Read the file headers (if any)
    headers = next(rows) if has_headers else []

    # If a column selector was given, find indices of the specified columns.
    # Also narrow the set of headers used for resulting dictionaries
    if select:
        indices = [headers.index(colname) for colname in select]
        headers = select

    for row_nr, row in enumerate(rows, start=1):
        if not row: # Skip rows with no data
                continue
        
        # If specific column indices are selected, pick them out
        if select:
            row = [row[i] for i in indices]

        # Make the type conversion if the types are provided
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {row_nr} : Couldn\'t convert {row}')
                    print(f'Row {row_nr} : Reason {e}')
                continue

        # Make a dictionary or a tuple
        if headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)

        records.append(record)
        
    return records

if __name__ == '__main__':
    import gzip
    with gzip.open('Data/portfolio.csv.gz', 'rt') as f:
        print(parse_csv(f,select=['name', 'shares', 'price'], types=[str, int, float]))