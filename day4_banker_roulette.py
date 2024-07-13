# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.
import random
names=["Ferdi","Octi","Zafran","Atik"]
num_len = len(names)
get_item = random.randint(0,num_len-1)

print(f"{names[get_item]} is going to buy the meal today!")

# print(names)
# 🚨 Remember to remove the print statement above when you submit.