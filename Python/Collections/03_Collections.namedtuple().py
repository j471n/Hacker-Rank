# Programmer : Jatin Sharma

from collections import namedtuple

n = int(input())
s = input()
total = 0.0
Student = namedtuple('Student', s)

for i in range(n):
    students = Student(*input().split())
    total += int(students.MARKS)

print("%0.2f" % (total/n))
