from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    upcoming_week_birthdays = []
    current_date = datetime.today().date()

    for user in users:
        try:
            # Перетворення рядка дати народження на об'єкт datetime
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

            # Отримання дня народження цього року: замінити рік народження на поточний рік
            birthday_this_year = user_birthday.replace(year=current_date.year)
            
            # Якщо день народження вже був цього року, то беремо наступний рік
            if birthday_this_year < current_date:
                birthday_this_year = user_birthday.replace(year=current_date.year + 1)

            # Визначення різниці між днем народження та поточним днем
            days_until_birthday = (birthday_this_year - current_date).days

            # Перевірка, чи день народження випадає протягом наступних 7 днів (включаючи поточний)
            if 0 <= days_until_birthday <= 7:
                congratulation_date = birthday_this_year

                # Якщо день народження припадає на вихідний, перенести дату привітання на наступний понеділок
                if birthday_this_year.weekday() >= 5: 
                    days_to_add = 7 - birthday_this_year.weekday()
                    congratulation_date = birthday_this_year + timedelta(days=days_to_add)

                upcoming_week_birthdays.append({
                    'name': user['name'],
                    'congratulation_date': congratulation_date.strftime("%Y.%m.%d")
                })

        except ValueError:
            print(f"Невірний формат дати для користувача {user['name']}. Очікується формат: 'РРРР.ММ.ДД'")

    print(upcoming_week_birthdays)
    return upcoming_week_birthdays

    

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.08"},
    {"name": "Annie Rock", "birthday": "1989.04.09"},
    {"name": "Eric Down", "birthday": "1996.11.09"}
]

get_upcoming_birthdays(users)