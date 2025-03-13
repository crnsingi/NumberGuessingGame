import random

lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

x = random.randint(lower,upper)
print("You have got",round(math.log(upper-lower+1,2)), "chances to guess.")
