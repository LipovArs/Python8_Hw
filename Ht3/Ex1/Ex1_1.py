elem_list = list(range(15))
amount = 0

for i in elem_list:
  amount += i
print(amount)

amount = 0
i=0

while i < len(elem_list):
  amount+=elem_list[i]
  i+=1
print(amount)