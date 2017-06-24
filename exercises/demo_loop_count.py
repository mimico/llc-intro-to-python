import csv

csv_file = open('llc-chapters.csv', 'r')
csv_data = csv.DictReader(csv_file)

count = 0
for row in csv_data:
    count = count + 1

print("There are " + str(count) + " chapters")
csv_file.close()
