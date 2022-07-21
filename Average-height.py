student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
''' for taking a list'''
''' for calculating total height'''
new_height = 0
for height in student_heights:
    new_height += height
''' for calculating total students'''
number_of_students = 0
for student in student_heights:
    number_of_students += 1
''' taking the average of total and printing'''
average_height = round(new_height/number_of_students)
print(f"The average height of {number_of_students} is {average_height}")
