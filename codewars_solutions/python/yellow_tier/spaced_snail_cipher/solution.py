ORIENTATIONS = {
        1: {"start_dir": "DOWN",  "turn": "CW"},
        2: {"start_dir": "DOWN",  "turn": "CCW"},
        3: {"start_dir": "UP",    "turn": "CW"},
        4: {"start_dir": "UP",    "turn": "CCW"},
        5: {"start_dir": "LEFT",  "turn": "CW"},
        6: {"start_dir": "LEFT",  "turn": "CCW"},
        7: {"start_dir": "RIGHT", "turn": "CW"},
        8: {"start_dir": "RIGHT", "turn": "CCW"},
    }


def main():
    ...

def encode(plaintext : str, key : int) -> str:
    string_key = str(abs(key))
    mode = get_mode(key)
    if mode == "CENTER_OUT":
        or_code, gap_size = get_orientation_and_gap(key)

    else:
        pass

    return ''
                                

def decode(cipher : str,key : int) -> str:
    return ''

def get_orientation_and_gap(key):
    string_key = str(abs(key))
    or_code = ORIENTATIONS[int(string_key[0])]
    gap_size = int(string_key[1])

    return or_code, gap_size


def get_mode(key):
    if key > 0:
        return "CENTER_OUT"
    else:
        return "OUTSIDE_IN"



if __name__ == "__main__":
    main()
