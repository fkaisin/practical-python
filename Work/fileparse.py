# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a csv file into a list of records
    '''
    if select and not has_headers:
        raise RuntimeError('select requires column headers')

    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter=delimiter)
        records = []

        # Read the file headers
        if has_headers:
            headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        for row_nr, row in enumerate(rows):
            if not row: # Skip rows with no data
                    continue
            
            if has_headers:
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[i] for i in indices]
                # Make the type conversion if the types are provided
                if types:
                    try:
                        row = [func(val) for func, val in zip(types, row)]
                    except ValueError as e:
                        if not silence_errors:
                            print(f'Row {row_nr} : Couldn\'t convert {row}')
                            print(f'Row {row_nr} : Reason {e}')

                # Make a dictionary 
                record = dict(zip(headers, row))
            
            else:
                # Make a tuple 
                record = tuple(row) 

            records.append(record)
        
    return records