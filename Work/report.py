# report.py
#
# Exercise 2.4

from pprint import pprint
from fileparse import parse_csv
import stock
import tableformat

def read_portfolio(file_name):
    '''
    Read a stock portfolio file into a list of dictionaries with keys
    name, shares, and price.
    '''
    try:
        with open(file_name, 'rt') as f:
            portdicts = parse_csv(f, select=['name','shares','price'], types=[str, int, float])
            portfolio = [stock.Stock(s['name'], s['shares'], s['price']) for s in portdicts]

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
        current_price = prices[s.name]
        change = current_price - s.price
        report.append((s.name, s.shares, current_price, change))
    return report

def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    '''
    Read a stock portfolio file and a prices file, and print a report.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    if portfolio is None or prices is None:
        print('Error reading files.')
        return
    
    # Make the report
    report = make_report(portfolio, prices)

    # Print it
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(args):
    if len(args) < 3 or len(args) > 4:
        raise SystemExit(f'Usage: {args[0]} portfile pricefile format')
    portfolio_report(args[1], args[2], args[3])

if __name__ == '__main__':
    print(f'{"  RESTART  ":=^50s}')
    # portfolio_report('Data/portfolio.csv', 'Data/prices.csv', 'txt')
    # portfolio_report('Work/Data/portfolio2.csv', 'Work/Data/prices.csv')
    import sys
    main(sys.argv)