student_marks = input("Input a list of student Scores ").split()
for n in range(0, len(student_marks)):
    student_marks[n] = int(student_marks[n])
'''making a list of student'''
'''creating a for loop to check every element in the list'''
new_marks = 0
for marks in student_marks:
    '''if statement to check if the number is greatest than the previous if yes then changing it to new value'''
    if new_marks < marks:
        new_marks = marks
    else:
        continue
print(f"Highest score of student in the list is: {new_marks}")
