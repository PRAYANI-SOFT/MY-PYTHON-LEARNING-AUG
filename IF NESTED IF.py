print("WELCOME TO PARK")
height=int(input("height of the human in cm:"))

if height>150:
    print("Eligible to go to PARK ")
    age = int(input("age of the human:"))
    if age>18:
        print("NEED TO PAY: 20$ ")
    elif age<=18:
        print("NEED TO PAY :10$ ")

else :
    print("not eligible to go to park ")


    #BMI value

    weight = 85
    heightt = 1.85

    bmi = weight / (heightt ** 2)
    if bmi < 18.5:
        print("UNDER WEIGHT")
    elif bmi > 25:
        print("OVER WEIGHT")
    else:
        print("NORMAL WEIGHT")
#welcome to park with photo option

print("WELCOME TO PARK")
height = int(input("height of the human in cm:"))
bill=0
if height > 150:
    print("Eligible to go to PARK ")
    age = int(input("age of the human:"))
    if age > 18:
        bill=20
        print("NEED TO PAY: 20$ ")
    elif age <= 18:
        bill=10
        print("NEED TO PAY :10$ ")
    want_photo= input("WANT TO TAKE PHOTO? (Y/N):")
    if want_photo == "Y":
        print("PAY 3$  ")
        bill+=3
    print(f"PAY the bill : {bill}")
else:
    print("not eligible to go to park ")

