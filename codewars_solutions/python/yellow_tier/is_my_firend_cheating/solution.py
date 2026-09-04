def main():
    pass

def remov_nb(n):
    collector = []
    S = add_numbers_formula(n)
    # for a in range(1, n+1):
    #     for b in range(1, n+1):
    #         if a * b == S - (a + b):
    #             collector.append((a, b))
    #         else:
    #             continue

    for a in range(1, n+1):
        b = (S - a)/(a + 1)
        if b.is_integer() and b <= n:
            collector.append((a, b))
    
    sorted_results = sorted(collector)

    return sorted_results

def add_numbers(number):
    result = 0

    for i in range(1, number+1):
        result += i

    return result

def add_numbers_formula(n):
    return (n*(n+1))/2



if __name__ == "__main__":
    main()

