# def number():
#     numeric_value=int(input("Enter the number :"))
#     return numeric_value
# # ControlStatement: they allow us to control the flow of our program
# # if-else: Given num is even or odd
# num = int(input("Enter Number :"))
# if num%2==0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")
# # ==================================================================
# # elif: Take input cost and selling price and tell how much profit or loss happen
# cost_price = float(input("Enter the Cost price of product :"))
# selling_price = float(input("Enter the Selling price of product :"))
# if cost_price<selling_price:
#     print(f"Seller get profit of {selling_price-cost_price} Rs. ")
# elif selling_price<cost_price:
#     print(f"Seller get loss of {cost_price-selling_price} Rs.")
# else:
#     print("Sellere get neither loss nor profit")
# # ==================================================================
# #  Given num is a four digit num or not
# num = int(input("Enter the number :"))
# if num>=999 and num<=10000:
#     print("yes")
# else:
#     print("no")
# # ==================================================================
# # find greatest among three num
# num1=int(input("Enter first num :"))
# num2=int(input("Enter second num :"))
# num3=int(input("Enter third num :"))
# if num1 >num2 and num1 > num3:
#     print(f"{num1} is greatest")
# elif num2 >num3 and num2 > num1:
#     print(f"{num2} is greatest")
# else:
#     print(f"{num3} is greatest")
# # ===============================================================
# #  Number is divisible by 5 or 3 but not by 15
# num = int(input("Enter number :"))
# if num%15==0:
#     print(f"{num} is divisible by 15")
#     exit() # exit() from the program
# if num%5==0 and num%15!=0:
#     print(f"{num} is divisible by 5 ")
# elif num%3==0 and num%15!=0:
#     print(f"{num} is divisible by 3 ")
# else:
#     print(f"{num} is not divisible any 15 or 5 or 3")
# #================================================================
# # Match Case : just lilke switch case
# num1=float(input("Enter num1 :"))
# num2=float(input("Enter num2 :"))
# operator = input("Enter operator :")
# match operator:
#     case '+':
#         print("sum = ", num1+num2)
#     case '-':
#         print("sub = ", num1-num2)
#     case '/':
#         print("div = ", num1/num2)
#     case '*':
#         print("mul = ", num1*num2)
#     case '%':
#         print("modulus = ", num1%num2)
#     case _:
#         print("Enter a valid operator")
# # =========================================
# # Printing pattern as input 
# # if 1 then 
# #     *****
# # if 2 then 
# #     *****
# #     *****
# # if 3 then
# #     *****
# #     *****
# #     *****   and so on
# num=int(input("enter number :"))
# for i in range(num):
#     print("*****")
# # ================================================
# # Printing pattern as input 
# # if 1 then 
# #     1
# # if 2 then 
# #     12
# #     12
# # if 3 then
# #     123
# #     123
# #     123  and so on
# num=int(input("enter number :"))
# for i in range(num):
#     for j in range(1,num+1):
#       print(j,end=" ")
#     print("\n")
# # ================================
# # print given pattern as input 4 then
# # 1
# # 12
# # 123
# # 1234
# num=number()
# i=1
# while i<num+1:
#     for j in range(1,i+1):
#         print(j,end=" ")
#     i+=1
#     print("\n")
# # ==================================
# # pattern if 4
# # A
# # AB
# # ABC
# # ABCD
# num=number()
# i=1
# while i<num+1:
#     for j in range(65,i+65):
#         print(chr(j),end=" ")
#     i+=1
#     print("\n")
# # ========================================
# # pattern for diamond if input is 4 then
# #    1   
# #   123
# #  12345 
# # 1234567
# row=number()
# for i in range(1,row+1):
#     print(" "*(row-i),end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print(" "*(row-i),end="")
#     print("\n")
# # =================================
# i=1
# while i<row+1:
#     for j in range(65,65+i):
#         print(chr(j),end="")
#     i+=1
#     print("\n")    
        