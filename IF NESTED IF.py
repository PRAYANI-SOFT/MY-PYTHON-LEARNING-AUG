print("WELCOME TO PARK")
x=int(input("height of the human in cm:"))

if x>150:
    print("Eligible to go to PARK ")
    y = int(input("age of the human:"))
    if y>18:
        print("NEED TO PAY: 20$ ")
    else :
        print("NEED TO PAY :10$ ")
else :
    print("not eligible to go to park ")


    #BMI value

    weight = 85
    height = 1.85

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        print("UNDER WEIGHT")
    elif bmi > 25:
        print("OVER WEIGHT")
    else:
        print("NORMAL WEIGHT")

    # 🚨 Do not modify the values above
    # Write your code below 👇
