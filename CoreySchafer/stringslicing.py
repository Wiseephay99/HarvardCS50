import datetime
my_date = datetime.datetime(2024,  7, 25, 12, 30, 45)
# March 01 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print()
print(sentence)
print()