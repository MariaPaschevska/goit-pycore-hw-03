import re

def normalize_phone(phone_number):
    phone_number = str(phone_number)

    # Перевірка, чи номер починається з символу "+"
    if phone_number.find("+", 0) == -1:
        phone_number = "+" + phone_number

    # Перевірка, чи номер має міжнародний код України
    if phone_number.find("38", 1) == -1:
        phone_number = phone_number.replace('+', '+38')

    # Видалення усіх символів, крім цифр та '+', з номера телефону
    phone_number_pattern = r"[^0-9+]"
    clean_number = re.sub(phone_number_pattern, '', phone_number)

    return clean_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
