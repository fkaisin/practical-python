# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(file_name):

    portfolio = []

    try:
        with open(file_name, 'rt') as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                try:
                    holding = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
                    portfolio.append(holding)
                except IndexError:
                    pass
            
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


file = 'Work/Data/portfolio.csv'
portfolio = read_portfolio(file)

file = 'Work/Data/prices.csv'
prices = read_prices(file)

report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print(f'%10s %10s %10s %10s' % headers)
print(f'{"":->10}', f'{"":->10}', f'{"":->10}', f'{"":->10}')

for n, s, p, c in report:
# for r in report:
    # string = f'%10s %10d %10.2f %10.2f' % r
    string = f'{n:>10s} {s:>10d} {'$' + str(p):>10s} {c:>10.2f}'
    print(string)