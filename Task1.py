from datetime import datetime, timedelta


def get_days_from_today(user_date) -> int:
    today = datetime.today().date()

    try:
        target_date = datetime.strptime(user_date, "%Y-%m-%d").date()
        delta = today - target_date
        return delta.days
    except ValueError:
        print("Невірний формат дати.")
        return None
    
    
if __name__ == "__main__":
    test_date = "2020-02-02"
    delta_days = get_days_from_today(test_date)
    print(delta_days)