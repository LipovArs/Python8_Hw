import sys

fizz = int(input("Enter fizz: "))
buzz = int(input("Enter buzz: "))

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()
file = open('test2.txt', 'x')


for line in lines:
    numbers = line.split()
    for num in numbers:
        i = int(num)
        if i % fizz == 0 and i % buzz == 0:
            file.write("FB ")
        elif i % fizz == 0:
            file.write("F ")
        elif i % buzz == 0:
            file.write("B ",)
        else:
            file.write(f"{i} ")
    file.write("\n")