import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k',
           'l','m','n','o','p','q','r','s','t','u','v',
           'w','x','y','z']
symbols = ['!','#','$','%','&','*',')','(','+','*']

print("Welcome to Password Generator!")

nr_of_letters = int(input("HOW MANY LETTERS SHOULD BE IN PASSWORD? : "))
nr_of_symbols = int(input("HOW MANY SYMBOLS SHOULD BE IN PASSWORD? : "))
nr_of_numbers = int(input("HOW MANY NUMBERS SHOULD BE IN PASSWORD? : "))
n = int(input("HOW MANY PASSWORDS NEED TO BE GENERATED? : "))

check = nr_of_letters + nr_of_symbols + nr_of_numbers

for _ in range(n):  # generate n passwords
    if check == 16:
        password_list = []  # reset for each password

        # Add random numbers, symbols, letters
        for _ in range(nr_of_numbers):
            password_list.append(random.choice(numbers))
        for _ in range(nr_of_symbols):
            password_list.append(random.choice(symbols))
        for _ in range(nr_of_letters):
            password_list.append(random.choice(letters))

        # Shuffle so order is random
        random.shuffle(password_list)

        # Convert list → string
        password = "".join(password_list)
        print(f"Your password is: {password}")
    else:
        print("❌ CHOOSE THE SUM OF LETTERS + SYMBOLS + NUMBERS = 16")
        break