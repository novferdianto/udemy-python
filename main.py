# Welcome to rollercoaster height check program
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal
# != not equal

print("Welcome to rollercoaster height check program \n")
height = int(input("What's your height in cm ? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What's your age ? "))
  if age < 12:
    # print("Please pay IDR 50,000")
    bill = 50000
  elif age < 15:
    # print("Please pay IDR 60,000")
    bill = 60000
  elif age <= 18:
    # print("Please pay IDR 70,000")
    bill = 70000
  else:
    # print("Please pay IDR 100,000")
    bill = 100000
  photo = input ("Do you want a photo taken ? Y or N. ")
  if photo == "Y":
    bill +=25000
  print (f"Your final bill is IDR {bill}")
else:
  print("You can't ride the rollercoaster")