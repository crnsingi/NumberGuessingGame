import random
import math

lower = int(input("Enter the lower bound : "))
upper = int(input("Enter the upper bound : "))

x = random.randint(lower,upper)
print("You have got",round(math.log(upper-lower+1,2)), "chances to guess.")

count = 0

while count < math.log(upper-lower+1,2):
    count+=1
    
    guess = int(input("guess the numnber : "))