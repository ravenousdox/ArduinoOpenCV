def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

num = int(input("Enter a number: "))
print_factors(num)
print()

while (input("Do you want to continue? ").lower() == 'y'):
    print()
    num = int(input("Enter a number: "))
    print_factors(num)
    print()
