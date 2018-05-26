import csv


rows = list(csv.reader(open('input.csv', 'r'), delimiter=','))
cols = zip(*rows)
unik = set(cols[0])

indexed = defaultdict(list)

for x in unik:
    i = cols[0].index(x)
    indexed[i] = rows[i]

print (indexed)