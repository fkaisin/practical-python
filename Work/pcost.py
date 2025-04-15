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
            headers = next(f)
            rows = csv.reader(f)
            for row in rows:
                total_cost += float(row[1]) * float(row[2])

        # total_cost = round(total_cost,2)
        return total_cost

    except FileNotFoundError:
        print('File not found.')
        return 0.0
