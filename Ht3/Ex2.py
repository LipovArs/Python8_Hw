import sys

fizz = int(input("Enter fizz: "))
buzz = int(input("Enter buzz: "))

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

for line in lines:
    numbers = line.split()
    for num in numbers:
        i = int(num)
        if i % fizz == 0 and i % buzz == 0:
            print("FB", end=' ')
        elif i % fizz == 0:
            print("F", end=' ')
        elif i % buzz == 0:
            print("B", end=' ')
        else:
            print(i, end=' ')
    print()