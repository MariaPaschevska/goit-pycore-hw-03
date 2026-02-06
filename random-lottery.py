import random

def get_numbers_ticket(min, max, quantity):
    # Валідація даних
    try:
        min = int(min)
        max = int(max)
        quantity = int(quantity)

    except (ValueError, TypeError):
        print(f"Передані невірні дані: {min}, {max}, {quantity}. Введіть числа")
        return []
        
    # Перевірка обмежень
    if min < 1 or max > 1000:
        print(f'Мінімальне число повинно бути не менше 1. Ви ввели: {min}')
        print(f'Максимальне число повинно бути не більше 1000. Ви ввели: {max}')
        return []
    
    if min > max:
        print('Мінімальне число повинно бути менше, ніж максимальне')
        return []
    
    if quantity < 1 or quantity > (max - min + 1):
        print(f'Кількість повинна бути в діапазоні між мінімальним та максимальним числом. Ви ввели: {quantity}')
        return []
    
    # Генерація унікальних випадкових чисел
    lottery_numbers = random.sample(range(min, max + 1), quantity)

    # Сортування та повернення результату
    print(sorted(lottery_numbers))
    return sorted(lottery_numbers)
