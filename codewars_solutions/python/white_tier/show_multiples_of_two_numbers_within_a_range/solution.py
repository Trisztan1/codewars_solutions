def multiples(a: int, b: int, limit: int) -> list[int]:
    numbers_list = []

    for number in range(limit+1):
        if number % a == 0 and number % b == 0 and number != 0:
            numbers_list.append(number)

    return numbers_list


numbers = multiples(2, 4, 40)
print(numbers)
