# pcost.py
#
# Exercise 1.27

def portfolio_cost(filename = 'Data/portfolio.csv'):
    import csv
    import sys

    try:
        total_cost = 0

        if len(sys.argv) == 2:
            filename = sys.argv[1]

        with open(filename,'rt') as f:
            headers = next(f)
            rows = csv.reader(f)
            for row in rows:
                total_cost += float(row[1]) * float(row[2])

        total_cost = round(total_cost,2)
        print(f'Total cost {total_cost}')
    except FileNotFoundError:
        print('File not found.')


# file = 'C:/Users/kaisin_f/OneDrive - sabca.be/code/practical-python/Work/Data/portfolio.csv'
# file = 'missing.csv'
portfolio_cost()