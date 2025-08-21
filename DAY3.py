"""1.Create three variables: an integer with value 25, a float with value 45.67
and a string with value "Python is fun!" Finally
Print each variable and its type using type()."""

a=25
b=45.67
c="Python is fun!"
print(a, b, c, sep="\n")
print(type(a))
print(type(b))
print(type(c))

"""
25
45.67
Python is fun!
<class 'int'>
<class 'float'>
<class 'str'>"""


"""2.Swap the values of two variables without using a third variable.
Example: a = 10, b = 20 → After swapping: a = 20, b = 10.
"""
a = 10
b = 20
#using tuple
print("a =", a)
print("b =", b)
print("using Tuple swapped the values of two variables without using a third variable.")
a, b = b, a

print("a =", a)
print("b =", b)

"""output: 
a = 10
b = 20
using Tuple swapped the values of two variables without using a third variable.
a = 20
b = 10"""

"""3.Take a string variable with value "123". 
Convert it into an integer and add 10 to it and also Convert it into a float and multiply by 2"""

a = "123"       # string variable

# Convert to integer and add 10
num_int = int(a) + 10
print("Integer + 10:", num_int)

# Convert to float and multiply by 2
num_float = float(a) * 2
print("Float * 2:", num_float)

"""
Output:
Integer + 10: 133
Float * 2: 246.0"""


"""4. Given the string: text = "Python Programming" Perform the following:
(i) Print the first 6 letters.
(ii)Print the last 6 letters.
(iii)Print only "Programming" using slicing."""

text = "Python Programming"

# First 6 letters
print("First 6 letters:", text[:6])

# Last 6 letters
print("Last 6 letters:", text[-6:])

# (Print only "Programming"
print("Only 'Programming':", text[7:])
# (Print only "Programming"
print("Only 'Programming':", text[-11:])

"""Output: First 6 letters: Python
Last 6 letters: amming
Only 'Programming': Programming
Only 'Programming': Programming"""

"""5. From the string "Hello World": Print the character at index 0,
 Print the character at index 4 and finally Print the last character using negative indexing."""


text = "Hello World"

# Character at index 0
print("Index 0:", text[0])

# Character at index 4
print("Index 4:", text[4])

# Last character using negative indexing
print("Last character:", text[-1])

# Last character using  indexing
print("Last indexed character:", text[10])

"""Index 0: H
Index 4: o
Last character: d
Last indexed character: d"""