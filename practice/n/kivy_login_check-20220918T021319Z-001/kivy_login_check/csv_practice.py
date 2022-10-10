import csv

with open('people.csv', 'w') as file:
    n = csv.writer(file)
    n.writerow([3,"Mehrab", "Dhaka"])