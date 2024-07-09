# Welcome to rollercoaster height check program
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to
# == equal
# != not equal

print("Welcome to rollercoaster height check program \n")
height = int(input("What's your height in cm ? "))
if height >= 120:
  print("You can ride the rollercoaster")
  age = int(input("What's your age ? "))
  if age < 12:
    print("Please pay IDR 50,000")
  elif age < 15:
    print("Please pay IDR 60,000")
  elif age <= 18:
    print("Please pay IDR 70,000")
  else:
    print("Please pay IDR 100,000")
else:
  print("You can't ride the rollercoaster")