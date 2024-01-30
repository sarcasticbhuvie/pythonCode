# # Print Hello World!
# print("Hello World!")
# print("Hello\n World!")
# # ===============================================
# #to print ASCII value
# print(ord('a')) 
# # type(variable_name) : to find dataType
# a=30
# print(type(a))
# #================================================
# # Take input 2 number and print sum
# num1=int(input("Enter number 1 :"))
# num2=int(input("Enter number 2 :"))
# print(f"{num1} + {num2} = {num1+num2}")
# # ================================================
# # use of **,//
# # ** print square
# # // print int value not float
# print(5**2) # print 25
# print(11//2) # print 5
# # =================================================
# #  Logical operator: and, or, not
# print(2<4 and 5>3)
# print(2<1 or 5>3)
# print(4!=2)
# # ===============================================
# #  Identity Operator: is(return True when both variable are of same object), is not(return True  when both operators are not of same object) "Both check object type not value".
# x=5
# y=7
# z=7
# print(x is y) # return false beacause x,y both are diffrent obj
# print(x is not y) # return True beacause x,y both are diffrent obj
# print(z is y) # return true beacause z,y both are same obj means 5 is an object and y,z both pointing same obj.
# # ==========================================================
# # Membership Operator: in, not in
# fruits = ["apple","banana","papaya"]
# print("banana" in fruits)
# print("mango" not in fruits)
# # ===============================================================
# # Calculate volume of a sphare.
# import math
# radius=float(input("Enter the radius :"))
# volume=(4/3)*math.pi*(radius**3) 
# print(volume)
# # ==================================================================
# # # Operator Precedence:BODMAS: 
# # () => ** => /,//,% => * => +,- => Bitwise operator (>>,<<) => Bitwise operator (&,|,!) => comparison operator => logical operator=> (and,or,not)
# # ==========================================================
# # temprature from celsius to fahrenheite
# temp_celsius = float(input("Enter the Temprature in Celsius :"))
# temp_fahrenheit = temp_celsius * (9/5) +32
# print(f"{temp_celsius} degree celsius in Fahrenheit is {temp_fahrenheit} degree")
# # ===============================================================