from collections import Counter

def scramble(s1, s2):
    collection_s1 = Counter(s1)
    collection_s2 = Counter(s2)
    bools = []

    for item in collection_s2:
        if item in collection_s1:
            if collection_s2[item] <= collection_s1[item]:
                bools.append(True)
            else:
                bools.append(False)
        else:
            bools.append(False)

    return all(bools)
