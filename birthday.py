from datetime import date, timedelta

now = date.today()

#still requires handling of non-real dates
name= raw_input("What is your name? ")
m = int(raw_input("What month were you born? (1-12) "))
d = int(raw_input("What day were you born? "))
y = int(raw_input("What year were you born? "))

birthday = date(y, m, d)
age = now - birthday

print name, "you are", age.days, "days old today."

#my first attempt at this before the for statement below
#tenk = timedelta(days=10000)
#twek = timedelta(days=20000)
#earlier10k = now - tenk
#earlier20k = now - twek
#earlier_10kstr = earlier10k.strftime("%Y %m %d 10,000'ers ")
#earlier_20kstr = earlier20k.strftime("%Y %m %d 20,000'ers ")
#print earlier_10kstr
#print earlier_20kstr



#incidentally it was my 10,084th day alive when I wrote this age calculator in days
#so having just missed my 10,000th day I wanted to know why we don't celebrate peoples
#birthdays in days.  Bigger numbers is obviously cooler.  Sadly no one lives to 40k.

for x in range(1,5):
	delt = (now-timedelta(days=x*10000))
	print repr(str(x*10000) + "'ers").rjust(2), 
	print repr(delt.strftime("%Y %m %d")).rjust(3)