# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

sum = 0

for i in student_heights:
  sum = sum + i 

sum = sum/len(student_heights)

print(round(sum))


# print(student_heights)
#Write your code below this row 👇




