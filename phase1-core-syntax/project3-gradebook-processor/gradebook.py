# The student.txt file is already created and the format of it is very simple - name, score1, score2, score3.
# The first step would be to get the file open.

with open('student.txt', encoding='utf-8') as file:
    file_data = file.readlines()
    for line in file_data:
        


# Let us take an empty dictionary for now to store the student data.
student_data = {}
