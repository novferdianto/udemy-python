target = int(input())
even_sum=0
# for number in range(2,int(target)+1,2):
#   even_sum += number
# print(even_sum)

# alternative solution #1
for number in range(1,int(target)+1):
  if number %2 == 0:
    even_sum += number

print(even_sum)

# alternative solution #2
# for number in range(even_sum,target):
#   if target > 0:
#     if target % 2 == 0: 
#       even_sum += target
#   target -= 1
# print(even_sum)


