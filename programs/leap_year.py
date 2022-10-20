# year = 2000
# if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")

import calendar
print(calendar.isleap(2020))
print(calendar.isleap(2000))
print(calendar.isleap(2003))