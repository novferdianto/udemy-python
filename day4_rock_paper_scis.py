import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))

computer_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print("Invalid Input, You Lose !.. Try Again")
else:    
    print(game[user_choice])
    print(f"Computer choose :\n {game[computer_choice]}")
    if user_choice == computer_choice:
        print ("It's Draw, try again ")
# elif user_choice == 0 and computer_choice == 1:
#     print ("You Lose")
# elif user_choice == 0 and computer_choice == 2:
#     print ("You Win")
# elif user_choice == 1 and computer_choice == 0:
#     print ("You Win")
# elif user_choice == 1 and computer_choice == 2:
#     print("You Lose")
# elif user_choice == 2 and computer_choice == 1:
#     print("You Win")
# elif user_choice == 2 and computer_choice == 0:
#     print("You Lose")
    elif user_choice == 0 and computer_choice == 2:
        print ("You Win")
    elif computer_choice == 2 and user_choice == 0:
        print ("You Lose")
    elif user_choice > computer_choice: # see the index of the list
        print ("You Win")
    elif computer_choice > user_choice: # see the index of the list
        print ("You Lose")
    