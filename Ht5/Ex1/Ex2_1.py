nums = list(range(0, 51))


def is_simple(num):
    for i in range(2, round(num / 2)):
        if not num % i:
            pass
    return num**2


print(list(map(is_simple, nums)))
