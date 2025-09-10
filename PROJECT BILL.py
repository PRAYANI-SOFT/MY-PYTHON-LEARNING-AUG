x = float(input("TOTAL BILL AMOUNT: "))
y=int(input("PERCENTAGE OF TIP: mostly 10 15 20:"))
s=int(input("number of members will share the bill:"))
z= x/100*y+x
q= z/s
print(f"TOTAL BILL AMOUNT WITH TIP: {z}\n AMOUNT PER PERSON: {q}" )
