def create_phone_number(n):
    first_part = ["("]
    second_part = []
    third_part = []

    for i, number in enumerate(n):
        if i < 3:
            first_part.append(number)
        elif i < 6:
            second_part.append(number)
        else:
            third_part.append(number)

        
    first_part += [")", " "]
    second_part.append("-")
    merged_list = first_part + second_part + third_part

    return "".join(map(str, merged_list))


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
phone_number = create_phone_number(n)

print(phone_number)
