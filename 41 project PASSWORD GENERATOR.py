import random
numbers= ['0','1','2','3','4','5','6','7','8','9']
letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbol = ['!','#','$','%','&','*',')','(','+','*']
print(numbers)
print(letters)
print(symbol)

print("Welcome to password generator")
nr_of_letters= int(input("HOW MANY LETTERS SHOULD THERE IN PASSWORD GENERATOR? :\n"))
nr_of_symbols= int(input("HOW MANY SYMBOLS SHOULD THERE IN PASSWORD GENERATOR? :\n"))
nr_of_numbers= int(input("HOW MANY NUMBERS SHOULD THERE IN PASSWORD GENERATOR? :\n"))

check = nr_of_letters + nr_of_symbols + nr_of_numbers
password =""
if check == 16 :

    print("This is your password generator")
    for num in range (0,nr_of_numbers) :
        password += random.choice(numbers)
    for sym in range (0,nr_of_symbols) :
        password += random.choice(symbol)
    for letter in range (0,nr_of_letters) :
       password += random.choice(letters)
    print(password)
    print(len(password))

else:
    print("CHOOSE THE SUM OF LETTERS + SYMBOLS + NUMBERS=16")

