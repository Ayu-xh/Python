# Statistics calculator.
# We are given exam scores of a student in 5 subjects.
import random

lowest_marks = 0
highest_marks = 100
marks = random.choices(range(lowest_marks, highest_marks+1), k=5)

max_marks = max(marks)
min_marks = min(marks)

total_subjects = len(marks)
total_marks = sum(marks)
print(f'Your marks are : {marks}')

average_marks = total_marks/total_subjects
print(f'The average marks are {average_marks}')
print(f'The maximum marks are {max_marks}')
print(f'The minimum marks are {min_marks}')

above_average_count = 0
for mark in marks:
    if mark > average_marks:
        above_average_count += 1

print(f"The student has received above average marks in {above_average_count} subjects")

# This gives the index of the highest marks
i = marks.index(max_marks)

# Then we use the list splicing technique to create a new list by combining the remaining two halves.
new_marks = marks[:i] + marks[i+1:]
smax_marks = max(new_marks)

print(f'The second highest marks are {smax_marks}')

reverse_list = marks[::-1]
print(f'The marks in the reverse order are {reverse_list}')
print(f"The average marks are {average_marks}, highest marks are {max_marks}, lowest marks are {min_marks}, and second highest marks are {smax_marks}")
