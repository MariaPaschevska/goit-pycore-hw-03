from datetime import datetime
import re

def get_days_from_today(date) -> int:
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    match = re.search(date_pattern, str(date))

    if match:
        try:
            input_date = datetime.strptime(match.group(), "%Y-%m-%d")
            current_date = datetime.today()
            days_diff = input_date - current_date
            print(days_diff.days)
            return days_diff.days
        except ValueError:
            print(f"Невалідна дата: {match.group()}")
            return None

    else:
        print("Невірний формат дати. Очікується формат: 'РРРР-ММ-ДД'")
        return None
