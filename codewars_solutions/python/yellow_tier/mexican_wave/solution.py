def wave(people):
    container = list(people)
    container_main = [list(container) for _ in range(len(people))]
    result = []

    for i, item in enumerate(container_main):
        modified_item = item
        if item[i] == " ":
            continue
        else:
            modified_item[i] = modified_item[i].upper()
            result.append(modified_item)
    
    final_result = ["".join(i) for i in result]

    return final_result

print(wave("hello"))

def wave_better_version(people):
    result = []
    for i, char in enumerate(people):
        if char == " ":
            continue
        # Slice before char, uppercase char, slice after char
        result.append(people[:i] + char.upper() + people[i + 1 :])
    return result
