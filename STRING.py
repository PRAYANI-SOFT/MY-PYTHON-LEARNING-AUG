# Find the first and last position of "is" in the string "This is a simple string".

a = "this is a simple string"
x = a.find('is')
print('first position:', x)
y = a.rfind('is')
print('last position:', y)

"""OUTPUT: 
first position: 2
last position: 5"""

# Count how many times "a" occurs in "banana"
fruit = "banana"
x = fruit.count("a")
print('count of a:', x)
"""OUTPUT:
count of a: 3"""

# Use .find() to check if "Java" exists in "Python programming".Print "Found" if present, otherwise "Not Found".

SOFTY = "Python programming"
check = SOFTY.find("Java")
if (SOFTY.find("Java") < 0):
    print("Java not found")
else:
    print("Java found")

"""OUTPUT:
Java not found"""

# Find the index of "world" in "Hello world world", using .index() and .rindex().
roof = "Hello world world"
c = roof.index('world')

print('INDEX OF WORLD:', roof.index('world'))
print('REVERSE INDEX OF WORLD:', roof.rindex('world'))
"""OUTPUT:
INDEX OF WORLD: 6
REVERSE INDEX OF WORLD: 12"""

# In "Python python PYTHON", count lowercase "python", uppercase "PYTHON", and mixed "Python" separately.
check = "Python python PYTHON"
count_lower = check.count("python")
count_upper = check.count("PYTHON")
count_mixed = check.count("Python")
print('count_lower:', count_lower, 'count_upper:', count_upper, 'count_mixed:', count_mixed, sep='\n')

"""
OUTPUT: 
count_lower:
1
count_upper:
1
count_mixed:
1
"""

# Convert "python programming" to UPPERCASE.

word = "python programming"
capital_letter = word.upper()
print(capital_letter)

# OUTPUT: PYTHON PROGRAMMING


# 9. Title-case "welcome to the python world".
x = "welcome to the python world"
TITLE_case = x.title()
print('TITLE_CASE:', TITLE_case)

# output : TITLE_CASE: Welcome To The Python World


# 10. Swap the case of "PyThOn Is FuN".

x = "PyThOn Is FuN"
SWAP_CASE = x.swapcase()
print('SWAP_CASE:', SWAP_CASE)

# output : SWAP_CASE: pYtHoN iS fUn

# 11. Check if "12345" contains only digits.
text = "12345"

if text.isdigit():
    print("String contains only digits.")
else:
    print("String has non-digit characters.")

# output : String contains only digits.


# 12. Verify if "Python" starts with "Py" and ends with "on".
text = "Python"

print(text.startswith("Py"))  # True
print(text.endswith("on"))  # True

"""OUTPUT:True
True"""

# 13. Check if "hello123" is alphanumeric.
text = "hello123"

if text.isalnum():
    print("String is alphanumeric.")
else:
    print("String is not alphanumeric.")

# output : String is alphanumeric.


# 14. Test whether " " (only spaces) is considered .isspace().
text = " "

print(text.isspace())

# output :True


# 15 Check if "welcome" is lowercase and "WELCOME" is uppercase
text1 = "welcome"
text2 = "WELCOME"

print(text1.islower())
print(text2.isupper())

"""OUTPUT:True
True"""

# 16 Remove spaces at the beginning and end of " hello world ".
text = "   hello world   "
result = text.strip()

print("REMOVE THE SPACES:", repr(result))

"""OUTPUT : REMOVE THE SPACES: 'hello world'
"""

# 17. Replace "Java" with "Python" in "I love Java".

text = "I love Java"
text1 = "Python"
result = text.replace("Java", "Python")

print("REPLACED:", result)

# OUTPUT : REPLACED: I love Python

# 18. Replace all "o" with "0" in "good morning".
text = "good morning"
result = text.replace("o", "0")
print('REPLACE:', result)

# output : REPLACE: g00d m0rning


# 19. Remove all commas from "1,234,567".

text = "1,234,567"
result = text.replace(",", "")

print('REPLACED:', result)
# output : REPLACED: 1234567



