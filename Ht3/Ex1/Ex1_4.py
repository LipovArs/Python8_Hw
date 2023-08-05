exist_money = (1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

money = int(input())

for i in exist_money:
  count = money // i
  if count > 0:
    print(f"{i} - {count} cup.")
    money -= count * i
