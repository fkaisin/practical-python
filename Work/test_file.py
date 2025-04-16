from pprint import pprint
import csv
from collections import Counter, defaultdict, deque

portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]

total_shares = Counter()
for name, shares, price in portfolio:
    total_shares[name] += shares

holdings = defaultdict(list)
for name, shares, price in portfolio:
    holdings[name].append((shares,price))

history = deque(maxlen=3)
with open('Work/Data/portfolio.csv') as f:
    rows = csv.reader(f)
    for line in rows:
        history.append(line)

pprint(history)

# REPRENDRE AUX EXERCICES DU CHAPITRE 2.5