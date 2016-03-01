# Written by Thomas John Calhoun
# Jan 15 2016, Py 3.5.1
# Personal Milestone: My first Python program! (After my week1 Python class experience)

import datetime

def age_calc():
	print()
	print("Welcome to the Fabulous Age Checker!")
	print()

	YEAR = datetime.date.today().year #Breaking down the date into segments allows me to have it printed in any order I like...
	MONTH = datetime.date.today().month
	DAY = datetime.date.today().day
	print("Current date: %d/%d/%d" % (MONTH, DAY, YEAR)) #...Since M/D/Y is the American way, 'MURICA!

	print()
	BYEAR = int(input("Birth year? YYYY ->")) #User Birthday input
	BMONTH = int(input("Birth month? MM  ->"))
	BDAY = int(input("Day of birth? DD ->"))

	TIME = datetime.date.today() - datetime.date(BYEAR, BMONTH, BDAY) #This shows in DAYS total
	Y,D = divmod(TIME.days, 365) #divides by years
	AGE = TIME.days #Discovery: .days prevents a timestamp of zeros from showing.

	print()
	print('And now, The moment of truth! Here is the breakdown of your time in existence...')
	print("%a Years, %a Days." % (Y,D))
	print(AGE," Days Total.")
	print()

	input("PRESS ENTER TO CLOSE")