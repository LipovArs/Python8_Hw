import sys

filename = sys.argv[1]

f = open(filename, 'r')

for line in f:
  print(line)

f.close()