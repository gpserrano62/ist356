import datetime

my_birthday = " Nov 6, 2007"

today = datetime.date.today()

print("Today's date:", today)

# add 30 days to today's date
added_days = today + datetime.timedelta(days=30)
print("Date after adding 30 days:", added_days)


#strftime_format = today.strftime("%Y-%m-%d")
#strptime_format = datetime.datetime.strptime(strftime_format, "%Y-%m-%d")

date_string = datetime.datetime.strftime(strptime_format, "%B %d, %Y")
print("Today's date in string format:", date_string)

my_birthday = datetime.datetime.strptime(my_birthday, "%b %d, %Y")
born_on = datetime.datetime.strftime(my_birthday, "%A")
print("I was born on a", born_on)