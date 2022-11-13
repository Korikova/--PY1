import random


def get_unique_list_numbers(min_value, max_value, length) -> list[int]:
    unique_numbers = []

    while len(unique_numbers) < length:
        list_random = random.randint(min_value, max_value)
        if list_random not in unique_numbers:
            unique_numbers.append(list_random)

    return unique_numbers


length = 15
list_unique_numbers = get_unique_list_numbers(-10, 10, length)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)) == length)
