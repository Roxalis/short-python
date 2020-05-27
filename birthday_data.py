import datetime


def get_birth_date():
    b_date = input("Please provide your birth date (format: 21/6/1989): ")
    day, month, year = map(int, b_date.split('/'))
    return datetime.datetime(year, month, day)


def sec_to_period(seconds):
    days, sec = divmod(seconds, (3600 * 24))
    hours, sec = divmod(sec, 3600)
    minutes, sec = divmod(sec, 60)
    return days, hours, minutes, sec


def get_age(birth_date):
    delta = datetime.datetime.today() - birth_date
    age = int(delta.total_seconds() // (3600 * 24 * 365))
    return age


def next_birthday(birth_date):
    today = datetime.datetime.today()
    b_date = datetime.datetime(today.year, birth_date.month, birth_date.day)
    delta = b_date - datetime.datetime.today()
    if delta.total_seconds() >= 0:
        d, h, m, s = map(int, sec_to_period(delta.total_seconds()))
        print(f"Your next birthday is in {d} days, {h} hours, {m} minutes, and {s} seconds.")
    else:
        b_date = datetime.datetime(today.year + 1, birth_date.month, birth_date.day)
        delta = b_date - datetime.datetime.today()
        d, h, m, s = map(int, sec_to_period(delta.total_seconds()))
        print(f"Your next birthday is in {d} days, {h} hours, {m} minutes, and {s} seconds.")


def birthday_data():
    bdate = get_birth_date()
    print(f"Your age is {get_age(bdate)}.")
    next_birthday(bdate)


if __name__ == '__main__':
    birthday_data()
