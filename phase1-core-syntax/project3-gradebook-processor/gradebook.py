# The student.txt file is already created and the format of it is very simple - name, score1, score2, score3.
# The first step would be to get the file open.


# Let us take a new list just for the sake of storing intermediate results.
student_data_list = []

with open('student.txt', encoding='utf-8') as file:
    file_data = file.readlines()
    for line in file_data:
        cleaned_line = line.rstrip('\n')
        split_data = cleaned_line.split(',')
        student_data_dict = {}
        student_data_dict['name'] = split_data[0]
        student_data_dict['marks'] = list(map(int, split_data[1:]))
        student_data_dict['highest_score'] = max(split_data[1:])
        student_data_dict['lowest_score'] = min(split_data[1:])
        student_data_dict['average_score'] = round((sum(list(map(int, split_data[1:]))))/len(split_data[1:]), 2)

        student_data_list.append(student_data_dict)


print(student_data_list)



