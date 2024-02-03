# def add(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# n=int(input("Enter the n :"))
# print(add(n))
# # ##################################
# # Add two numbers:
# def add(n1,n2):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum=n1+n2
#     return sum
# n1=45
# n2=76
# # # positional argument
# # print(add(n2,n1))
# # # keyword argument
# # print(add(n2=45,n1=67))
##################################
# # default arguments
# def showValue(value=67):
#     print(value)
# showValue(54)
####################################
# # arbitary arguments(variable-length arguments 
# # *args :treate as tuple
# def arbitary_args(*args):
#     for i in args:
#         print(i)

# arbitary_args(10,50,30,20,60,80,90,70)
# # **kwargs :treate as dictionary (key value pair)
# def arbitary_args(**args):
#     for i,j in args.items():
#         print(i,":",j)

# arbitary_args(name="bhupendra",course="MCA",college="IISE LUCKNOW")
# ##########################################
# # call by value:
# def num(a):
#     a=56
#     print("a inside function :",a)
# a=60
# num(a)
# print("a outside function :",a)

# # call by reference:list,dictionary
# def list_fun(list):
#     list.append(40)
#     print(list)
# list=[10,20,30]
# list_fun(list)
# print(list)

# ############################
# # factorial of a number: 
# def factorial(n):
#     fact=1
#     if n==1 or n==0:
#         return 1
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact
# n =int(input("Enter number to get factorial :"))
# print(factorial(n))