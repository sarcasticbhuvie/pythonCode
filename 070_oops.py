# class Student:
#     def set_name(self,name,age):
#         self.name=name
#         self.age=age        
#     def get_name(self):
#         print("Your name is :",self.name)
#         print("Your age is :",self.age)
    
# student1= Student()
# name=str(input("Enter Name:"))
# age=int(input("Enter Age:"))
# student1.set_name(name,age)
# student1.get_name()
# # #########################################
# # to print area and perimeter of rectangle
# class Rectangle:
#     def set_dimensions(self,height,width):
#         self.height=height
#         self.width=width
#     def area(self):
#         return self.height*self.width
#     def parimeter(self):
#         return 2*(self.height+self.width)
# rectangle1=Rectangle()
# height=float(input("Enter the height :"))
# width=float(input("Enter the width :"))
# rectangle1.set_dimensions(height,width)
# print(f"Area of rectangle with height {rectangle1.height},width {rectangle1.width} : {rectangle1.area()}")
# print(f"Perimeter of rectangle with height {rectangle1.height},width {rectangle1.width} : {rectangle1.parimeter()}")
# # #######################################################
# class Rectangle:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
# rectangle1=Rectangle(10,20)
# rectangle2=Rectangle(20,30)
# print(f"rectangle1 ::=> height : {rectangle1.height},width :{rectangle1.width}")
# print(f"rectangle2 ::=> height : {rectangle2.height},width :{rectangle2.width}")
# ################################################
# class Student:
#     def __init__(self,name):
#         self.name=name # class attribute
#     def get_name(self):
#         return self.name
# student1=Student("bhuvie")
# student1.college="iise lucknow" #intance attribute
# print(student1.get_name(),'\n',student1.college)
# print(student1.college)
# ##############################################
