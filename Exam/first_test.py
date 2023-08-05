def spam(number):

    return 'bulochka' * number


def my_sum(list_of_numbers):

    sum_of_dig = 0

    for nums in list_of_numbers:
        sum_of_dig += nums

    return sum_of_dig


def shortener(string):

    ls = string.split(' ')
    trimmed_wrd_list = []

    for word in ls:
        if len(word) > 6:
            word = word[:6] + '*'
        trimmed_wrd_list.append(word)

    res_string = ' '.join(trimmed_wrd_list)

    return res_string


def compare_ends(words):
    count = 0

    for wrd in words:
        if len(wrd) >= 2:
            if wrd[0] == wrd[-1]:
                count += 1

    return count

