exist_money = (10, 20, 50, 100, 200, 500, 1000)

money = int(input())

for i in exist_money:
  count = min(money // i, 10)
  if count > 0:
    print(f"{i} - {count} cup.")
    money -= count * i
