import random


def get_numbers_ticket(min_value, max_value, quantity):
    if min_value < 1 or max_value > 1000 or not (1 <= quantity <= max_value - min_value + 1):
        return []
    
    numbers = random.sample(range(min_value, max_value + 1), quantity)
    numbers.sort()

    return numbers


if __name__ == "__main__":
    min_value = int(input("Введіть початок діапазону чисел (не менше 1): "))
    max_value = int(input("Введіть кінець діапазону чисел (не більше 1000): "))
    quantity = int(input("Введіть кількість номерів: "))

    result = get_numbers_ticket(min_value, max_value, quantity)
    print(result)
