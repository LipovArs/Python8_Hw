# url -  https://www.codewars.com/kata/josephus-permutation/

def josephus(items,k):
    death_count = []
    
    index = 0

    while len(items) > 0:
        index = (index + k-1) % len(items)
        death_count.append(items.pop(index))
    
    return death_count