import csv

def check_input(input):
	if input == '':
		return False
	else:
		return True

def clean_age(age):
	try:
		#if the age is negative, assume the absolute value is the correct one
		if int(age)<=(-1):
			age = abs(int(age))
	except:
		age =='NAN'
		#if there is no age set, use string for field and instruct customer service to call client for age information
		return 'NO_AGE'
	return age



input_data = 'input.csv'

def clean_data(data):
	csv_file = data
	f = open(csv_file)
	out = open('output.csv', 'w')
	fieldnames = ['id','full_name','first_name','last_name','email','gender','age']
	writer = csv.DictWriter(out, fieldnames=fieldnames)
	writer.writeheader()
	CSV = csv.DictReader(f)
	entries = set()
	i = 1
	for row in CSV:
		print(row)
		email = row['email']
		gender = row['gender']
		full_name=row['full_name']
		first_name = row['first_name']
		last_name = row['last_name']
		#if there is no name set for the user the information in the row is useless  => Delete.
		if not check_input(full_name or first_name or last_name ):
			continue
		if not check_input(email):
			#if there is no email set, assume client has a defaut email on our domain
			email = first_name + '.' + last_name + '@defaultemail.com'
		if not check_input(gender):
			#if there is no gender set, use string for field and instruct customer service to call client for gender information
			gender = 'NO_GENDER'
		age=clean_age(row['age'])

		entry = '%s,%s,%s,%s,%s,%s' % (full_name,first_name,last_name,email,gender,age)
		if entry not in entries:
			#write entry with new id fitting the iteration
			writer.writerow({'id':i,'full_name':full_name,'first_name':first_name,'last_name':last_name,'email':email,'gender':gender,'age':age})
			entries.add(entry)
		#iter count used as id
		i = i+1

	f.close()
	out.close()

clean_data(input_data)
