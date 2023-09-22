# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
# print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# for i in range(0,len(student_scores)):
#   for j in range(1,len(student_scores)):
#     if i > j:

print(max(student_scores))