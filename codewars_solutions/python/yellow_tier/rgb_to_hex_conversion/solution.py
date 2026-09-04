HEX_CODES = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F"
}

def main():
    print(rgb(-20, 275, 125)) # FFFFFF

    
def rgb(r, g, b):
    first = get_hex_pair(r)
    second = get_hex_pair(g)
    third = get_hex_pair(b)

    return "".join([first, second, third])

def get_hex_pair(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0

    first_hex = HEX_CODES[value // 16]
    second_hex = HEX_CODES[value % 16]

    return "".join([first_hex, second_hex])




if __name__ == "__main__":
    main()
