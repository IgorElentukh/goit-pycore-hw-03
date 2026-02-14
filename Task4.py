from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    upcoming_birthdays = []

    today = datetime.today().date()

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        difference_days = (birthday_this_year - today).days

        if difference_days >= 0 and difference_days <= 7:
            day_of_week = birthday_this_year.weekday()

            if day_of_week == 5:
                congratulation_date = birthday_this_year + timedelta(days=2)
            elif day_of_week == 6:
                congratulation_date = birthday_this_year + timedelta(days=1)
            else:
                congratulation_date = birthday_this_year

            congratulation_date_string = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthday = {
                "name": user["name"], 
                "congratulation_date": congratulation_date_string
                } 
            
            upcoming_birthdays.append(upcoming_birthday)

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.02.14"},
        {"name": "Jane Smith", "birthday": "1990.02.12"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)

