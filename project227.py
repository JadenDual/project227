import json
import csv

data_from_csv = []

with open('data_set.txt', 'r') as f:
	data_from_text = json.load(f.read())

field_names = ['brake', 'hand_brake', 'throttle', 'steer']

csv_store = open('project227.csv', 'w', newline = '')

writer = csv.DictWriter(csv_store, fieldnames = field_names)
writer.writeheader()
writer.whiterows(data_from_text)

with open('project227.csv', 'r') as file:
	reader = csv.Reader(file)
	for row in reader:
		data_from_csv.append(row)

print(data_from_csv)