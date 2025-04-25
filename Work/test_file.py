import stock
import fileparse
import report

# with open('Data/portfolio.csv') as lines:
#     portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

# portfolio = [stock.Stock(s['name'], s['shares'], s['price']) for s in portdicts]
# print(sum(s.cost() for s in portfolio))

# s = stock.Stock('GOOG', 100, 490.1)
# columns = ['name', 'shares']
# for colname in columns:
#     print(colname, '=', getattr(s, colname))

portfolio = report.read_portfolio('Data/portfolio.csv')
from tableformat import create_formatter, print_table
formatter = create_formatter('xls')
print_table(portfolio, ['name', 'shares', 'price'], formatter)