from datetime import datetime, timedelta


def get_days_from_today(today, user_date) ->int:
    delta = today - user_date
    return delta.days

while True:
    user_input = input("Введіть довільну дату у форматі YYYY-MM-DD: ").strip()

    try:
        user_date = datetime.strptime(user_input, "%Y-%m-%d")
        break
    except ValueError:
        print("Невірний формат дати. ")

today = datetime.today()
delta_days = get_days_from_today(today, user_date)

if __name__ == "__main__":
    print(delta_days)




