import csv


class Cleaner(object):
	

	def read_csv():
		f = open("input.csv")
		CSV = csv.DictReader(f)
		for row in CSV:
			print (row['first_name'])
			if row['first_name'] == '':
				row['first_name']='NO_NAME'
				print (row['first_name'])

		f.close()

	read_csv()

	#with open('input	.csv') as f:
	#	reader = csv.DictReader(f, delimiter=';')
	#	for row in reader:
			#print(row)