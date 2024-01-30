# number = int(input("Enter the number :"))
# for num in range(2,number):
#     isprime=1
#     for i in range(2,number//2):
#         if number%i==0:
#             isprime=0
#     if isprime:
#         print(f"{number} is prime")
#     else:
#         print(f"{number} is not prime")

import math


num =int(input("Enter the range: "))
for n in range(2,num):
    temp=n
    for i in range(2,temp):
        if(n%i==0):
            break
    else:
        print(n)