import csv

def check_input(input):
	if input == '':
		return False
	else:
		return True

def clean_age(age):
	data = age
	try:
		if 0<=data<=120:
			print("WTF?")
			if int(data)<=-1:
				data = abs(int(row['age']))
	except:
		data =='NAN'
		return 'NO_AGE'
	return data

def dict_filter(it, *keys):
	for d in it:
		yield dict((k, d[k]) for k in keys)

#def check_duplicates(rows_without_id):


input_data = 'input.csv'

def clean_data(data):
	csv_file = data
	f = open(csv_file)
	out = open('first_edit.csv', 'w')
	fieldnames = ['id','full_name','first_name','last_name','email','gender','age']
	writer = csv.DictWriter(out, fieldnames=fieldnames)
	writer.writeheader()
	CSV = csv.DictReader(f)
	seen_ids = {}
	i = 0
	for row in CSV:
		print(row)
		email = row['email']
		gender = row['gender']
		if check_input(row['full_name']):
			full_name=row['full_name']
			first_name = row['first_name']
			last_name = row['last_name']
		if not check_input(row['full_name']):
			#row['first_name']='NO_NAME'
			print ("No Name -> DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!")
			continue
		if not check_input(email):
			email = 'NO_EMAIL'
		if not check_input(gender):
			gender = 'NO_GENDER'
		age=clean_age(row['age'])
		writer.writerow({'id':row['id'],'full_name':full_name,'first_name':first_name,'last_name':last_name,'email':email,'gender':gender,'age':age})
		i = i+1

	f.close()
	out.close()

clean_data(input_data)
