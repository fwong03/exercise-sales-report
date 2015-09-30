"""
sales_report2.py - Takes sales-report.py and uses dictionaries instead
of lists.

"""

melons_by_person = {}

f = open("sales-report.txt")
for line in f:
    line = line.rstrip()
    entries = line.split("|")

    salesperson = entries[0]
    melons = int(entries[2])

    melons_by_person[salesperson] = melons_by_person.get(
        salesperson, 0) + melons


for person, melons_sold in melons_by_person.items():
    print "{} sold {:,} melons".format(person, melons_sold)
