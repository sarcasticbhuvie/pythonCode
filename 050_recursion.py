# # factorial of a number: using recursion
# def factorial(n):
#     if n==1 or n==0:
#         return 1 
#     fact=n*factorial(n-1)
#     return fact
# n =int(input("Enter number to get factorial :"))
# print(factorial(n))
# # ##########################################
# # print 1-n number using recursion
# def print_1_to_n(n):
#     if n==1:
#         print(1) 
#         return
#     print_1_to_n(n-1)
#     print(n)
# n =int(input("Enter number :"))
# print_1_to_n(n)
# # #####################################
# # print n-1 number using recursion
# def print_1_to_n(n):
#     if n==1:
#         print(1) 
#         return
#     print(n)
#     print_1_to_n(n-1)
# n =int(input("Enter number :"))
# print_1_to_n(n)
# # ###################################
# # sum of 1-n
# def sum_1_to_n(n):
#     if n==1:
#         return 1 
#     return n+sum_1_to_n(n-1)
# n =int(input("Enter number :"))
# print(f"sum of 1 to {n} : {sum_1_to_n(n)}")
# # ##################################################
# #  function calculate a aised to power b using recursion
# def a_raised_to_power_b(a,b):
#     if b==1:
#         return  
#     return a*a_raised_to_power_b(a,b-1)
# n =int(input("Enter number :"))
# m =int(input("Enter power :"))
# print(f"{n} power raised to {m} : {a_raised_to_power_b(n,m)}")

# ##############################
#  print fibonacci series:
def print_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return print_fibonacci(n-1)+print_fibonacci(n-2)
n=int(input("Enter the length of fibonacci series :"))
for i in range(n):
    print(print_fibonacci(i))