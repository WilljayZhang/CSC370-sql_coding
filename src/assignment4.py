import psycopg2

query = ["select count(*) Number from Participator where Type = 'volunteer';", 
"select Participator.Name, count(*) Number from Participator, Working where Participator.ID = Working.Participator_ID group by Participator.ID;",
"select Funding from Donors where Name = 'Oracle';",
"select ID from Campaign where Campaign.start_time = '2019-6-1';",
"select ID from Campaign where end_time = '2019-3-30';",
"select Campaign.Content from Campaign where Campaign.ID in (select Campaign_ID from Adopt group by Adopt.Campaign_ID order by count(*) asc) limit 1;",
"select Campaign.Content from Campaign right join Working W on Campaign.ID = W.Campaign_ID group by W.Campaign_ID, Campaign.Content order by count(*) desc limit 1;",
"select D.Name, D.Funding - sum(Funding.expense) Remain from Funding join Donners D on Funding.Donners_ID = D.ID group by Donners_ID;",
"select Participator.Name from Participator where Participator.ID in (select Participator_ID from Working join Campaign C on Working.Campaign_ID = C.ID where C.Address = 'New York');",
"select Donors.Name from Donors where Donors.ID in(select Donors_ID from Funding join Campaign C on Funding.Campaign_ID = C.ID where C.Address = 'Washington');"]

query_questions = ["1. How many volunteers does this company have",
                    "2. How many activities does everybody participate in?",
                    "3. How much does Oracle donate?",
                    "4. Which campaign was held on 2019-6-1?",
                    "5. Which campaigns was finished on 2019-3-30?",
                    "6. Which campaign uses the least types of advertise?",
                    "7. Which campaign has the most workers?",
                    "8. How much have each donor remained?",
                    "9. Who have participated the campaign in New York?",
                    "10. Which donor have donated the campaign in Washington?"]
 
def connect(user, password, host='studsql.csc.uvic.ca'):
	connection = psycopg2.connect(host=host,user=user, password=password)
	cursor = connection.cursor()
	return connection, cursor

def add_volunteers(cursor, name, type, phone, address, salary=None):
	sql = "insert into Participator (Name, Type, Salary, Contact, Address) values (\'{}\', \'{}\', {}, \'{}\', \'{}\')".format(name, type, salary if salary else 'Null', phone, address)

	cursor.execute(sql)

def add_compaign(cursor, content, address, start_time, finish_time, participators, fundings=None, advertise=None):

	sql = "insert into Campaign (Content, Address, start_time, end_time) values (\'{}\', \'{}\', \'{}\', \'{}\')".format(content, address, start_time, finish_time)

	cursor.execute(sql)
	cursor.execute("SELECT max(ID) FROM Campaign;")
	id = cursor.fetchall()[0][0]
	for participator in participators:
		sql = "insert into Working values ({}, (select ID from Participator where Name = \"{}\"))".format(id, participator)
		cursor.execute(sql)
    
	if fundings:
		for (donner, funding) in fundings.items():
			sql = "insert into Funding values ({}, (select ID from Donners where Name = \"{}\"), {})".format(id, donner, funding)
			cursor.execute(sql)
    
	if advertise:
		for adv in advertise:
			sql = "insert into Adopt values ({}, (select ID from Advertise where Method = \"{}\"))".format(id, adv)
			cursor.execute(sql)


def main(cursor, connection):
	while True:
		print("1. Queries from Assignment #3")
		print("2. Setting up a campaign with volunteers, activities.")
		print("3. Some accounting information")
		print("4: Membership history")
		print("5: Get the remain money for the donner(My Own Idea)")
		print("6: Exit")
		choose = int(input("Please input the index you want to use (1-6): "))
		while choose < 1 or choose > 6:
			print("Incorrect index!")
			print("1. Queries from Assignment #3")
			print("2. Setting up a campaign with volunteers, activities.")
			print("3. Some accounting information")
			print("4: Membership history")
			print("5: Get the remain money for the donner(My Own Idea)")
			print("6: Exit")
			choose = input("Please input the index you want to use (1-6): ")

		if choose == 1:
			for q in query_questions:
				print(q)
			choose = int(input("Please input the index you want to use (1-{}): ".format(len(query))))

			while choose < 0 or choose > len(query):
				print("Incorrect index!")
				for q in query_questions:
					print(q)
				choose = input("Please input the index you want to use (1-{}): ".format(len(query)))
		    
			cursor.execute(query[choose])
			for d in cursor.description:
				if isinstance(d[0], str):
					print('{}\t'.format(d[0]), end='')
				else:
					print('{}\t'.format(str(d[0], "UTF-8")), end='')
		    
			print()
		        
			for res in cursor.fetchall():
				for r in res:
					print("{}\t".format(r), end='')
				print()
		elif choose == 2:
			print("1. Add new volunteers")
			print("2. Add new campaign")
			choose = int(input("Please input the index you want to use (1-2): "))
			while choose < 1 or choose > 2:
				print("Incorrect index!")
				print("1. Add new volunteer")
				print("2. Add new campaign")
				choose = int(input("Please input the index you want to use (1-2): "))

			if choose == 1:
				volunteer = input("Please input the information of the participator (Name Type Contact Address Salary(If Have)): ")
				info = volunteer.split(" ")
				add_volunteers(cursor, info[0], info[1], info[2], info[3], info[4] if len(info) > 4 else None )
			elif choose == 2:
				campaign = input("Please input the inofrmation of the campaign (content, address, start_time, finish_time): ").split(" ")
				participators = input("Please input the participators for this campaign: ").split(" ")
				tmp = input("Please input the donner and funding for this campaign: ")
				funding = None
			if tmp:
				tmp = tmp.split(" ")
				funding = dict()
				for i in range(0, len(tmp), 2):
					funding[tmp[i]] = int(tmp[i + 1])
			advertise = input("Please input the advertise for this campaign: ").split(" ")

			add_compaign(cursor, campaign[0], campaign[1], campaign[2], campaign[3], participators, funding, advertise)
		elif choose == 3:
			print("1. Get the funding for Campaigns")
			print("2. Get the funding for Donors")
			choose = int(input("Please input the index you want to use (1-2): "))

			while choose < 1 or choose > 2:
				print("Incorrect index!")
				print("1. Get the funding for Campaigns")
				print("2. Get the funding for Donors")
				choose = int(input("Please input the index you want to use (1-2): "))
			if choose == 1:
				campaign = input("Please input the campaign's content: ")
				sql = "select C.Content, D.Name, Funding.expense from Funding LEFT JOIN Campaign C ON Funding.Campaign_ID = C.ID LEFT JOIN Donors D ON Funding.Donors_ID = D.ID where Campaign_ID in (SELECT ID FROM Campaign WHERE Content = \'{}\');".format(campaign)
				print('Campaign'.ljust(30), end='')
				print('Donner'.ljust(30), end='')
				print('Funding'.ljust(30), end='')
				print('ASCII bar charts'.ljust(30))
				cursor.execute(sql)
				for res in cursor.fetchall():
					for r in res:
						print("{}".format(r).ljust(30), end='')
				for i in range(0, int(res[-1]), 100):
					print("*", end='')
				print()
			elif choose == 2:
				donner = input("Please input the donner's name: ")
				sql = 'select D.Name, C.Content, Funding.expense from Funding LEFT JOIN Campaign C ON Funding.Campaign_ID = C.ID LEFT JOIN Donors D ON Funding.Donors_ID = D.ID WHERE Donors_ID in (SELECT ID FROM Donors WHERE D.Name = \'{}\');'.format(donner)
		        
				cursor.execute(sql)
				print('Donner'.ljust(30), end='')
				print('Campaign'.ljust(30), end='')
				print('Funding'.ljust(30), end='')
				print('ASCII bar charts'.ljust(30))
				for res in cursor.fetchall():
					for r in res:
						print("{}".format(r).ljust(30), end='')
				for i in range(0, int(res[-1]), 100):
					print("*", end='')
				print()
		elif choose == 4:
			print("1. Get the membership history.")
			print("2. Add annotations for participator.")
			choose = int(input("Please input the index you want to use (1-2): "))

			while choose < 1 or choose > 2:
				print("Incorrect index!")
				print("1. Get the membership history.")
				print("2. Add annotations for participator.")
				choose = int(input("Please input the index you want to use (1-2): "))
			if choose == 1:
				name = input("Please input the name of the member: ")
				sql = "SELECT Name, Type, Contact, Annotation, Campaign.Content, Campaign.Address, Campaign.start_time, Campaign.end_time FROM Working LEFT JOIN Participator ON Working.Participator_ID = Participator.ID LEFT JOIN Campaign ON Working.Campaign_ID = Campaign.ID WHERE Name = \'{}\';".format(name)
				cursor.execute(sql)
				results = cursor.fetchall()
				if results:
					print("Name".ljust(15), end='')
					print("Type".ljust(15), end='')
					print("Contact".ljust(15), end='')
					print("Annotation".ljust(30), end='')
					print("Campaign".ljust(30), end='')
					print("Address".ljust(15), end='')
					print("Start_time".ljust(15), end='')
					print("End_time".ljust(15))

					for res in results:
						for (i,r) in enumerate(res):
							print("{}".format(r).ljust(30 if i == 3 or i == 4 else 15), end='')
						print()                    
				else:
					print("No such participator or relative campaigns")
			else:
				name = input("Please input the name of member: ")
				annotation = input("Please input the annotation: ")
				sql = "UPDATE Participator SET Annotation = \"{}\" WHERE Name = \'{}\';".format(annotation, name)
				cursor.execute(sql)
		        

		elif choose == 5:
			donner = input("Please input the donner's name: ")
			sql = "SELECT Funding - (SELECT sum(expense) FROM Funding WHERE Donors_ID in (SELECT ID FROM Donors WHERE Name = '{}')) Remain_Money FROM Donors WHERE Name = '{}';".format(donner, donner)
			cursor.execute(sql)
			res = cursor.fetchall()
			if res:
				print("Donner".ljust(30), end='')
				print("Remain Money".ljust(30))
				print("{}".format(donner).ljust(30), end='')
				print(res[0][0])
		elif choose == 6:
		    return
if __name__ == '__main__':
    connection, cursor = connect("belaya", "cL}A&DSqw;")

    # add_compaign(cursor, "abc", "adb", "2018-1-1", "2018-1-1", ["John", "Jane"], {"Google":100}, "Poster")
    # cursor.execute("SELECT * from Campaign;")
    # print(cursor.fetchall())
    main(cursor, connection)

    cursor.close()
    connection.commit()
    connection.close()
