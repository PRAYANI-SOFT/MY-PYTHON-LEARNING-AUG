import random
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
choices = ["ROCK", "PAPER", "SCISSOR"]
choose=input("Do you choose ROCK/PAPER /SCISSORS? : ")
COMPUTER =(random.choice(choices))
print(f"COMPUTER CHOICE:{COMPUTER}")
if choose==COMPUTER:
    print("DRAWN")
    if choose!=COMPUTER and choose=="ROCK" and COMPUTER=="SCISSOR":
                print("YOU WON")
        else:
             print("YOU LOSE")
if choose!=COMPUTER and choose=="SCISSOR" and COMPUTER=="PAPER":
    print("YOU WIN")
else:
    print("YOU LOSE")
if choose!=COMPUTER and choose=="PAPER" and COMPUTER=="ROCK":
    print("YOU WIN")
else:
    print("YOU LOSE")


