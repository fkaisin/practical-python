import csv

with open('Work/Data/portfolio.csv','rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    
    row = next(rows)
    print (dict(zip(headers, row)))