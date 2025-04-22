# pcost.py
#
# Exercise 1.27

import csv
import sys
import report

def portfolio_cost(filename = 'Data/portfolio.csv'):
    try:
        total_cost = 0.0

        if len(sys.argv) == 2:
            filename = sys.argv[1]

        portfolio = report.read_portfolio(filename)
        for row in portfolio:
            total_cost += row['shares'] * row['price']

        # total_cost = round(total_cost,2)
        return total_cost

    except FileNotFoundError:
        print('File not found.')
        return 0.0

def main(args):
    if len(args) != 2:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile')
    print('Total cost :', portfolio_cost(args[1]))


if __name__ == '__main__':
    # import sys
    # main(sys.argv)
    print('Total cost :', portfolio_cost('Data/portfolio.csv'))