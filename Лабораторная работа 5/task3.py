def get_unique_list_numbers() -> list[int]:
    import random
    start = -10
    stop = 10
    count = 15
    result = []
    seen = set()
    for i in range(count):
        x = random.randint(start, stop)
        while x in seen:
            x = random.randint(start, stop)
        seen.add(x)
        result.append(x)
    return result


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))





