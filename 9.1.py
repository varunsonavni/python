dict1 = {"name": "demo", "age": "10"}

# print(dict1.keys())
# print(dict1.values())
# print(dict1.))

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for grade in student_scores:
    if student_scores[grade] >= 91 and student_scores[grade] <= 100:
        student_grades[grade] = "Outstanding"
  
    elif student_scores[grade] >= 81 and student_scores[grade] <= 90:
        student_grades[grade] = "Exceeds Expectations"

    elif student_scores[grade] >= 71 and student_scores[grade] <= 80:
        student_grades[grade] = "Acceptable"
    else:
        student_grades[grade] = "Fail"


print(student_grades)