print("""Welcome to Treasure Island. Your mission is to find the treasure""")
direction= input("ADD DIRECTION SELECT (right:RIGHT, left:LEFT): ")
if direction == "LEFT":
    activity= input("ADD ACTIVITY SELECT (SWIM /WAIT): ")
    if activity == "SWIM":
        print("Attacked by trout.Game Over.")
    else:
        door=input("ADD DOOR SELECT (BLUE, RED, YELLOW): ")
        if door == "RED":
            print("Burned by fire. Game Over.")
        elif door == "BLUE":
            print("Eaten by beasts.Game Over.")
        elif door == "YELLOW":
            print("You Win!")
        else :
            print("Game Over.")
elif direction == "RIGHT":
    print("Fall into a hole.Game Over.")
else :
    print("ENTER THE CORRECT VALUE")

