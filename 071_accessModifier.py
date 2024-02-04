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