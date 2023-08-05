import sys

filename = sys.argv[0]

with open(filename, 'r') as f:
    text = f.readlines()

for line in text[::-1]:
    print(line)
  