from random import randrange
from time import sleep

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

while True:
    num = randrange(100)
    print_factors(num)
    print()
    sleep(0.5)
