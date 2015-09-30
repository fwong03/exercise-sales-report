"""
sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
"""

# To do this more efficiently, we could make a dictionary.
# The keys would be the salesperson and the values would be
# the number of melons sold.

# Create empty empty lists. One holds in index indicating the
# sales person, and the melons sold by that salesperson is stored
# on the same index in the melons list.

salespeople = []
melons_sold = []

# Open up the file and iterate over each line, stripping out any white
# space on the edges and splitting the text into words at pipes.
# The name of the sales person is at index 0 and the number of 
# melons sold is at index 2.
# We then check what index the salesperson is in the salespeople list,
# and add the melons to that same index in the melons_sold list.
# If the salesperson is not in the salespeople list, we add that
# person to the end.

f = open("sales-report.txt")
for line in f:
    line = line.rstrip()
    entries = line.split("|")
    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Here we print out the info by salesperson.

for i in range(len(salespeople)):
    print "{} sold {} melons".format(salespeople[i], melons_sold[i])
