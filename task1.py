from datetime import datetime, timedelta
from collections import defaultdict

def get_birthdays_per_week(users):
    birthdays_per_day = defaultdict(list)

    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime('%A')
            birthdays_per_day[day_of_week].append(name)
        else:
            continue

    for day, names in birthdays_per_day.items():
        print(f"{day}: {', '.join(names)}")