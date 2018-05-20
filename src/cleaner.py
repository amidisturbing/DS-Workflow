import csv

def check_name(name):
	if name == '':
		return False
	else:
		return True

def clean_age(age):
	data = abs(int(age))
	try:
		if 0<=data<=120:
			print("WTF?")
	except:
		data =='NAN'
		return 'NO_AGE'
	return data



input_data = 'input.csv'

def clean_data(data):
	csv_file = data
	f = open(csv_file)
	#out = open('first_edit.csv')
	CSV = csv.DictReader(f)
	for row in CSV:
		print(row)
		a = check_name("Laura")
		check_name(row['first_name'])
		if check_name(row['first_name']):
			print (row['first_name'])
		if not check_name(row['first_name']):
			#row['first_name']='NO_NAME'
			print ("No Name -> DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!")
		try:
			if 0<=int(row['age'])<=120:
				print("WTF?")
				if int(row['age'])<=-1:
					row['age'] = abs(int(row['age']))
		except:
			row['age']=='NAN'

	f.close()

clean_data(input_data)

#with open('input	.csv') as f:
#	reader = csv.DictReader(f, delimiter=';')
#	for row in reader:
	#print(row)