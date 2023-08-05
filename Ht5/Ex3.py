city = []
zip_code = []


def user_menu():
    a = input("Input City's name ---> ")
    b = input("Input City's zip code ---> ")

    city.append(a)
    zip_code.append(b)

    print(list(zip(city, zip_code)))


def prog_loop():
    wal = 0

    while wal < 1:
        print('1. Add city\n2. Print list\n3. Exit')

        answer = int(input("---> "))

        if answer == 1:
            user_menu()
        elif answer == 2:
            print(list(zip(city, zip_code)))
        elif answer == 3:
            wal = 1
        else:
            print("ERROR: Incorrect answer!")


print('''Hello! 
This program use zip!
''')

prog_loop()
