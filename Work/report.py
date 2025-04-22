# report.py
#
# Exercise 2.4

from pprint import pprint
from fileparse import parse_csv

def read_portfolio(file_name):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    try:
        with open(file_name, 'rt') as f:
            portfolio = parse_csv(f, select=['name','shares','price'], types=[str, int, float])
            
    except FileNotFoundError:
        print('File not found.')
        portfolio = None

    return portfolio

def read_prices(file_name):

    try:
        with open(file_name, 'rt') as f:
            prices = dict(parse_csv(f, types=[str, float], has_headers=False))

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

def main(args):
    if len(args) != 3:
        raise SystemExit(f'Usage: {args[0]} ' 'portfile pricefile')
    portfolio_report(args[1], args[2])

if __name__ == '__main__':
    portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
    # portfolio_report('Work/Data/portfolio2.csv', 'Work/Data/prices.csv')
    # import sys
    # main(sys.argv)