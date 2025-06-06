print()
#   DateTime

#   datetime

# Importing the Datetime Module
#*******************************************************************
import datetime
#*******************************************************************
# Getting the current Date Time
 #get the current time
current_datetime = datetime.datetime.now()
print(f'The Current Date and Time: {current_datetime}')
# Getting the Current Date
current_date = datetime.date.today()
print(f'Curent Date: {current_date}')

#*******************************************************************

# Extracing the Year, Month and Day
current_date = datetime.date.today()
year = current_date.year
month = current_date.month
day = current_date.day
print(f'Year: {year}')
print(f'Month: {month}')
print(f'Day: {day}')

#*******************************************************************

# Working with time
current_time = datetime.datetime.now().time()
print(f'Current time: {current_time}')

#*******************************************************************

# Creating custom Dates and Times
    # Custom datetime
custom_datetime = datetime.datetime(2025, 2, 5, 12,42, 0)
print(f'Custom Date and Time: {custom_datetime}')
    # custom date only
custom_date = datetime.date(2025, 2, 5)
print(f'Custom Date: {custom_date}')

#*******************************************************************

# Format Date an Time
current_datetime = datetime.datetime.now()
formatted_date = current_datetime.strftime("%d%m%Y")
formatted_time = current_datetime.strftime("%H:%M:%S")
print("Formatted Date:", formatted_date)
print("Formatted Time:",formatted_time)

#*******************************************************************

#   Parsing Strings into Dates 

date_str = "26/08/2024"
parsed_date = datetime.datetime.strptime(date_str, "%d/%m/%Y")
print(f"Parsed Date: {parsed_date}")

#*******************************************************************

#   Time Delta(Date Arithemetic)
    #   Adding 5 days to the current date
current_date = datetime.date.today()
new_date = current_date + datetime.timedelta(days=5)
print(f'Date after 5 days is:', new_date)
    #   Subtracting 2 hours from the current time
current_time = datetime.datetime.now()
new_time = current_time - datetime.timedelta(hours=2)
print(f'Time 2 hours ago: ', new_time)

#*******************************************************************

#   Get the difference between two Dates
date1 = datetime.date(2024, 8, 26)
date2 = datetime.date(2024, 9, 5)

difference = date2 - date1
print(f"Difference: {difference.days} days")

'''

Practice Questions
1. Write a Python program that takes a user's birthdate as input (in the format dd/mm/yyyy) and calculates t
2. Write a program that asks the user for their birthdate and then calculates how many days are left until the
3. Write a program that takes a date as input and prints the day of the week (e.g., Monday. Tuesday) for that date

'''

