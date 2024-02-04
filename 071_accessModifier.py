# # public attribute:can be accessed outside of the class
# # all the attribute by default is public
# class ClassName:
#     def __init__(self,name):
#         self.public_name=name   # public attribute
#     def public_function(self):  # public function
#         print(self.public_name)
# c1=ClassName('hello World!')
# c1.public_function()


# # private attribute:can not be accessed outside of the class
# # use __ before attribute or function name
# class ClassName:
#     def __init__(self,name):
#         self.__private_name=name   # private attribute
#     def __private_function(self):  # private function
#         print(self.__private_name)
# c1=ClassName('hello World!')
# # c1.__private_function() # give error
# # print(c1.__private_name) # give error
# # ####################################

# # protected attribute:can be accessed by child class only
# # use _ before attribute or function name
# class ClassName:
#     def __init__(self,name):
#         self._protected_name=name   # protected attribute
#     def _protected_function(self):  # protected function
#         print(self._protected_name)
# c1=ClassName('hello World! by protected')
# c1._protected_function()
# print(c1._protected_name)
# # ####################################

# # 1. Inheritance :
# class Parent:
#     def __init__(self):
#         self.super_attribute="parent class attribute"
#         print("This is Parent Class")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("This is Child class")

# obj=Child()
# print(obj.super_attribute)

# # Q. print fare(fare=seating capacity*100) of vehicle and 10% extra for bus where bus is child class of vehicle

# class Vehicle:
#     def __init__(self,capacity):
#         self.seating_capacity= capacity

#     def fare_charge(self):
#         return self.seating_capacity*100

# class Bus(Vehicle):
#     def __init__(self, capacity):
#         super().__init__(capacity)

#     def fare_charge(self):
#         fare_charge=super().fare_charge()
#         maintenance_charge=fare_charge*.1
#         return fare_charge+maintenance_charge
    
# vehicle1 = Vehicle(50)
# print(vehicle1.fare_charge())

# bus1=Bus(50)
# print(bus1.fare_charge())

# # ###############################################

# # 2. Polymorphism:: it allowa obj of diff classes as obj of same superClass

# class Animal:
#     def speaks(): # Abstract method to be overwritten
#         pass
# class Dog:
#     def speaks(self):
#         print("Dogs Bark....")
# class Cat:
#     def speaks(self):
#         print("Cats Meo.....")
# class Cow:
#     def speaks(self):
#         print("COW Mooo...")

# dog1=Dog()
# dog1.speaks()

# cat1=Cat()
# cat1.speaks()

# cow1=Cow()
# cow1.speaks()

# # ############################################

# 3. Abstraction: This allow us to focus on the what of an object rather then how of the object
# helps us to hide unneccassry detail hide implementation

# 4. Encapsulation: bundle the attribute(data) and methods(functions) togather in one class
