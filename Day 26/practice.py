# Day 26 List Comprehensions - Practice

import random

test_list = [2*num for num in range(1,5)]

#print(test_list)

list_A_names = ['Caroline', 'Jack', 'Oscar', 'Toby', 'Alex']

list_B_names = [name.upper() for name in list_A_names]

#print(list_B_names)

student_marks = {student:random.randint(1,100) for student in list_A_names}

passed_students = {student:mark for student,mark in student_marks.items() if mark > 50}

print(student_marks)
print(passed_students)