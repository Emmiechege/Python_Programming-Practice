#!/usr/bin/python3
students = ['eunice', 'rose', 'dennis', 'peter', 'andrew', 'cate', 'john', 'ann']
print("The fist four students in the list are:")
for student in students[0:4]:
    print(student.title())
print("Four students from the middle of the list are")
for student in students[2:-2]:
    print(student.title())
print("The last four students in the list are: ")
for student in students[4:]:
    print(student.title())
