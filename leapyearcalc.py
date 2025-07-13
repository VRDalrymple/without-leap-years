import datetime

''' 
    The pre-Julian Roman calendar had entire month's worth of leap days. This month, 
    Mercedonius, was said to be 27 days long. Theoretically added every 2-3 years,
    political corruption affected its actual usage. Because the Republic was formed
    in `509 BCE, I will estimate that this is when a formal calendar began usage.
    There were 13 erroneous leap years after the Julian calendar was adopted in 45 BCE. 
    7 CE was the next leap year. There are 107 leap years between 1582 and 2023.
    There were 393 leap years in between 7 CE and 1582 CE in the Julian Calendar.
    In 1582, the Gregorian calendar was introduced to the world. It had a new way
    of calculating leap years.
    
    As of 2023, without leap years, the current date would be 513 days behind the actual date
    taking into account only the Julian and Gregorian calendars.
'''
# the number of estimated leap days from the Julian calendar, and later the Gregorian calendar.
leap_days = 513
# the estimated number of days from the pre-Julian Roman calendar.
# Calculated with the equation ((509-45)/2)*27.
before_Julian = 6254

current_date = datetime.date.today()
year = int(current_date.strftime("%Y").replace(" 0", " "))

if year % 4 != 0:
    pass
elif year % 100 != 0:
    leap_days += 1
elif year % 400 != 0:
    pass
else:
    pass

no_leap = current_date - datetime.timedelta(days=(leap_days+before_Julian))
current_date = current_date.strftime("%A, %B %d, %Y").replace(" 0", " ")
print(f"Actual date: {current_date}")

no_leap = datetime.datetime.strptime(str(no_leap), "%Y-%m-%d")
no_leap = no_leap.strftime("%A, %B %d, %Y").replace(" 0", " ")

print(f"Without leap years, it might be around {no_leap}.")