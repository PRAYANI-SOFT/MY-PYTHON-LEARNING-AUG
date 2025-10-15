import random
word_list = ["aardvark","baboon","camel"]
random_word = (random.choice(word_list))
print(random_word)
length = len(random_word)
print(length)
while length:
    print(" _ ",end="")
    length=length-1

print("")


guess= input("Enter the correct letters:").lower()
display = " "
for letter in random_word:
    if guess == letter :
        display += letter
    else :
        display += " _ "
print(display)
