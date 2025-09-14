student_courses= [150,490,690]

total_courses = sum(student_courses)
print(total_courses)

sumof=0
for count in student_courses:
    sumof=sumof+count
print("TOTAL SUM OF THE NUMBER:", sumof)

MAX_courses = max(student_courses)
print(MAX_courses)

MAX=0
for count1 in student_courses:
    if count1 > MAX:
        MAX=count1
print("HIGHEST VALUE :", MAX)
