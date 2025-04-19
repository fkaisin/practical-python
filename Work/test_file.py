import csv
from pprint import pprint

# with open('Work/Data/portfoliodate.csv','rt') as f:
    # rows = csv.reader(f)
    # headers = next(rows)
    # select = ['name', 'shares', 'price', 'date']
    # types = [str, int, float, tuple]
    # indices = [headers.index(colname) for colname in select]
    
    # portfolio = [{name: func(val) for name, func, val in zip(select, types, [row[i] for i in indices])} for row in rows]


# pprint(portfolio)

def parse_date(date_str):
    return tuple(map(int, date_str.split('/')))

with open('Work/Data/dowstocks.csv','rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    # row = next(rows)
    types = [str, float, parse_date, str, float, float, float, float, int]
    converted = [[func(val) for func, val in zip(types, row)] for row in rows]

    pprint(converted)