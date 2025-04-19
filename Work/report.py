# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(file_name):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    portfolio = []

    try:
        with open(file_name, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for n, row in enumerate(rows):
                try:
                    record = dict(zip(headers, row))
                    record['name'] = str(record['name'])
                    record['shares'] = int(record['shares'])
                    record['price'] = float(record['price'])
                    portfolio.append(record)
                except IndexError:
                    print(f'Row {n}: Bad row: {row}')
                except ValueError:
                    print(f'Row {n}: Bad row: {row}')
            
    except FileNotFoundError:
        print('File not found.')
        portfolio = None

    return portfolio

def read_prices(file_name):

    prices = {}

    try:
        with open(file_name, 'rt') as f:
            rows = csv.reader(f)
            for row in rows:
                try:
                    prices[row[0]] = float(row[1])
                except IndexError:
                    pass

    except FileNotFoundError:
        print('File not found.')
        prices = None

    return prices

def make_report(portfolio, prices):

    report = []
    for s in portfolio:
        current_price = prices[s['name']]
        change = current_price - s['price']
        report.append((s['name'], s['shares'], current_price, change))
    return report

def print_report(report):
    '''
    Print a report of the stock portfolio.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print(f'%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for r in report:
        string = f'%10s %10d %10.2f %10.2f' % r
        print(string)

    ## Pour afficher le prix avec le signe dollars $
    # for n, s, p, c in report:
        # string = f'{n:>10s} {s:>10d} {'$' + str(p):>10s} {c:>10.2f}'
        # print(string)

def portfolio_report(portfolio_file, prices_file):
    '''
    Read a stock portfolio file and a prices file, and print a report.
    '''
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    if portfolio is None or prices is None:
        print('Error reading files.')
        return

    print_report(make_report(portfolio, prices))

# portfolio_report('Work/Data/portfolio.csv', 'Work/Data/prices.csv')
# portfolio_report('Work/Data/portfolio2.csv', 'Work/Data/prices.csv')
