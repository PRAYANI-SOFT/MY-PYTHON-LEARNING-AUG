import random
#from dis import RETURN_CONST


def rock():
    print(""" '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''""")
def paper():
    print('''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''')
def scissors():
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
print("LET US PLAY ROCK PAPER SCISSORS")
choices = ["ROCK", "PAPER", "SCISSORS"]
choose=input("Do you choose ROCK/PAPER /SCISSORS? : ")
if choose=="ROCK":
    rock()
elif choose=="PAPER":
    paper()
else :
    scissors()
COMPUTER =(random.choice(choices))


print(f"COMPUTER CHOICE:{COMPUTER}")
if COMPUTER=="ROCK":
    rock()
elif COMPUTER=="PAPER":
    paper()
else :
    scissors()
if choose==COMPUTER:
    print("DRAWN")
elif choose=="ROCK" and COMPUTER=="SCISSORS":
     print("YOU WON")
elif choose=="SCISSORS" and COMPUTER=="ROCK":
    print("YOU LOSE")
elif choose=="SCISSORS" and COMPUTER=="PAPER":
    print("YOU WIN")
elif choose=="PAPER" and COMPUTER=="SCISSORS":
    print("YOU LOSE")
elif choose=="PAPER" and COMPUTER=="ROCK":
    print("YOU WIN")
elif choose == "ROCK" and COMPUTER == "PAPER":
    print("YOU LOSE")



