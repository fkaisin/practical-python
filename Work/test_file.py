import stock
import fileparse

# with open('Data/portfolio.csv') as lines:
#     portdicts = fileparse.parse_csv(lines, select=['name', 'shares', 'price'], types=[str, int, float])

# portfolio = [stock.Stock(s['name'], s['shares'], s['price']) for s in portdicts]
# print(sum(s.cost() for s in portfolio))

s = stock.MyStock('GOOG', 100, 490.1)
print(s.cost())