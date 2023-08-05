import sys

fizz = int(input("Enter fizz: "))
buzz = int(input("Enter buzz: "))

filename = sys.argv[1]

with open(filename, 'r') as f:
    lines = f.readlines()

with open('test2.txt', 'w') as file:
    output = [
        'FB ' if int(num) % fizz == 0 and int(num) % buzz == 0 else
        'F ' if int(num) % fizz == 0 else
        'B ' if int(num) % buzz == 0 else
        f'{int(num)} '
        for line in lines
        for num in line.split()
    ]
    file.writelines(''.join(output))
