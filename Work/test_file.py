import csv
from pprint import pprint

with open('Work/Data/portfoliodate.csv','rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    select = ['name', 'shares', 'price']
    indices = [headers.index(colname) for colname in select]

    row = next(rows)
    # record = {colname: row[index] for colname, index in zip(select, indices)}

    portfolio = [{colname: row[index] for colname, index in zip(select, indices)} for row in rows]

pprint(portfolio)