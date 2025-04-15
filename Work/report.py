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

# # Calcul du gain total

# file = 'Work/Data/portfolio.csv'
# portfolio = read_portfolio(file)

# file = 'Work/Data/prices.csv'
# prices = read_prices(file)

# total_gains = 0.0

# for s in portfolio:
#     gain = s['shares'] * (prices[s['name']] - s['price'])
#     total_gains += gain
#     print(f'Gains sur {s['name']} : {round(gain,2)}')

# print('Gain total : ', total_gains)