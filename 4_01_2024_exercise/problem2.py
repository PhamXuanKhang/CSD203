"""
Write a program to do the following:
-  Enter the grade of a subject in decimal system (requirement check inputted data) 
-  Print out the corresponding grade in alphabetic and 4th system
"""

alphabetic_grades = ['F', 'D', 'C', 'B', 'A'] #Intialize arrays of grade
fourth_grades = [0, 1, 2, 3, 4]
upbound_grade = [3.9, 5.4, 6.9, 8.4, 10]
downbound_grade = [0, 4.0, 5.5, 7.0, 8.5]

def check_grade(grade):
    for i in range(len(alphabetic_grades)):
        if grade <= upbound_grade[i] and grade >= downbound_grade[i]:
            return alphabetic_grades[i], fourth_grades[i]

grade = -1
while grade < 0 or grade > 10:
    grade = float(input("Enter the grade of a subject in decimal system: "))

handled_grade = check_grade(grade)
print(f"The corresponding grade in alphabetic system is: {handled_grade[0]}\nThe corresponding grade in 4th system is: {handled_grade[1]}")
