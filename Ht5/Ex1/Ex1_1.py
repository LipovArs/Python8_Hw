user_input = input("---> ")


def to_lower(word):
    return word.lower()


def to_upper(word):
    return word.upper()


lowercase_words = list(map(to_lower, user_input.split()))
uppercase_words = list(map(to_upper, user_input.split()))

print("Lowercase:", lowercase_words)
print("Uppercase:", uppercase_words)