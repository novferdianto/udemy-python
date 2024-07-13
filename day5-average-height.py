# Input a Python list of student heights
student_heights = input().split()
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

# print (student_heights)
total_heights = 0
for heights in student_heights:
  total_heights += int(heights)
# print (total_heights)

total_students = 0
for student in student_heights:
  total_students +=1
# print (total_students)

print (f"total height = {total_heights}")
print (f"number of students = {total_students}")
print (f"average height = {round(total_heights/total_students)}")