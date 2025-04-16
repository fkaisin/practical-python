# pcost.py
#
# Exercise 1.27

import csv
import sys

def portfolio_cost(filename = 'Data/portfolio.csv'):
    try:
        total_cost = 0.0

        if len(sys.argv) == 2:
            filename = sys.argv[1]

        with open(filename,'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for n, row in enumerate(rows, start=1):
                record = dict(zip(headers, row))
                try:
                    nshares = int(record['shares'])
                    price = float(record['price'])
                    total_cost += nshares * price
                except ValueError:
                    print(f'Row {n}: Bad row: {row}')

        # total_cost = round(total_cost,2)
        return total_cost

    except FileNotFoundError:
        print('File not found.')
        return 0.0


file = 'Work/Data/portfoliodate.csv'
print('Total cost : ', portfolio_cost(file))