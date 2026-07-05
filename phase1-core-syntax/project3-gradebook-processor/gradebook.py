# The student.txt file is already created and the format of it is very simple - name, score1, score2, score3.
# The first step would be to get the file open.


# Let us take a new list just for the sake of storing intermediate results.
student_data_list = []

with open('students.txt', encoding='utf-8') as file:
    file_data = file.readlines()
    for line in file_data:
        if line.strip():
            cleaned_line = line.rstrip('\n')
            split_data = cleaned_line.split(',')
            student_data_dict = {}
            marks_as_int = list(map(int, split_data[1:]))
            student_data_dict['name'] = split_data[0]
            student_data_dict['marks'] = marks_as_int
            student_data_dict['highest_score'] = max(marks_as_int)
            student_data_dict['lowest_score'] = min(marks_as_int)
            student_data_dict['average_score'] = round(sum(marks_as_int)/len(marks_as_int), 2)

            student_data_list.append(student_data_dict)

print(student_data_list)

# Now that we have all the data about all the students, we can have some general statistics about the entire class.
# We can start by declaring variables and assigning them to 0.
highest_average_score = 0
highest_average_student_name = ""
lowest_average_score = float('inf')
lowest_average_student_name = ""
total_average_score = 0

for student in student_data_list:
    if student['average_score'] > highest_average_score:
        highest_average_score = student['average_score']
        highest_average_student_name = student['name']

    if student['average_score'] < lowest_average_score:
        lowest_average_score = student['average_score']
        lowest_average_student_name = student['name']

    total_average_score += student['average_score']
    
# Next we calculate the average of all averages of the students in the class.
average_of_averages = total_average_score/len(student_data_list)

print(f'The highest average score in the class is {highest_average_score} and is scored by {highest_average_student_name}')
print(f'The lowest average score in the class is {lowest_average_score} and is scored by {lowest_average_student_name}')
print(f'The average class score is {round(average_of_averages, 2)}')


# Now all the scores have been calculated, and we just need to write to an output file.
with open('report.txt', 'w', encoding='utf-8') as file:
    file.write('The class results are as follows:\n')
    for student in student_data_list:
        file.write(f"{student['name']}, " 
                   f"{student['average_score']}, "
                   f"{'Pass' if student['average_score']>= 40 else 'Fail'}\n")
