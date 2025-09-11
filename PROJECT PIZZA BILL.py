print("WELCOME TO PIZZA HOME")
bill=0
size= input("Select the size of pizza S for Small M for medium L for Large :")
pepperoni=input("ADD PEPPERONI SELECT (Y/N): ")
CHEESE=input("ADD EXTRA CHEESE SELECT (Y/N): ")

if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill+=25
else :
    print("INVALID INPUT")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill+= 3
else:
    bill += 0
if CHEESE == "Y":
    bill+=1


print(f"NEED TO PAY :$ {bill}")



