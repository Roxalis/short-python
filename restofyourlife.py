import datetime

date_today = datetime.date.today()

name = input("What's your name? ")
year = input('Hello %s, what year were you born? ' % name)
month = input('What month were you born? Please provide a number. ')
day = input('What day of the month was it? Please provide a number. ')
gender = input('Are you male or female? ')

if gender == 'male':
    expect = (78.6 + 10) * 365
elif gender == 'female':
    expect = (83.5 + 10) * 365
else:
    expect = 80 * 365

date_birth = datetime.date(int(year), int(month), int(day))

delta = date_today - date_birth
years = delta.days / 365.0
days = delta.days
hours = delta.days * 24.0

print("You were born %r years or %d days or around %d hours ago." % (round(years, 2), days, hours))

date_expect = date_birth + datetime.timedelta(days = int(expect))
year_expect = date_expect.year
delta_expect = date_expect - date_today
days_expect = delta_expect.days
hours_expect = days_expect * 24.0

print("Statistically and optimistically you will die in the year %d.\n"
      "That is in %d days or %d hours" % (year_expect, days_expect, hours_expect))
