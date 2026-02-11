import random


def get_numbers_ticket(min, max, quantity):
    numbers = []
    
    if min < 1 or max > 1000 or not (1 <= quantity <= max):
        return numbers
    
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()

    return numbers

min = int(input("Введіть початок діапазону чисел (не менше 1): "))
max = int(input("Введіть кінець діапазону чисел (не більше 1000): "))
quantity = int(input("Введіть кількість номерів: "))

result = get_numbers_ticket(min, max, quantity)

if __name__ == "__main__":
    print(result)
