import random

lower_bound = int(input("enter the lower bound: ").strip())
upper_bound = int(input("enter the upper bound: ").strip())

n = random.randrange(lower_bound,upper_bound,1)
print(n)