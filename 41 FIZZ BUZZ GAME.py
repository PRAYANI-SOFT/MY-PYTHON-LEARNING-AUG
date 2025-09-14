"""Rules of FizzBuzz

Print numbers from 1 to N (let’s say 1 to 100).

If a number is divisible by 3 → print "Fizz".

If a number is divisible by 5 → print "Buzz".

If divisible by both 3 and 5 → print "FizzBuzz".

Otherwise, just print the number."""

for number1 in range(1,101):
    if number1 % 3 == 0 and number1 % 5 == 0:
        print("FizzBuzz")
    elif number1 % 3 == 0:
        print("Fizz")
    elif number1 % 5 == 0:
        print("Buzz")
    else :
        print( number1)
