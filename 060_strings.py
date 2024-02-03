# # String:sequence of character inclosed with 
# #     'name'  
# #     "name"  
# #     """name""" :it also print multiline string

# name1='bhupendra'
# name2="Bhupendra"
# name3="""name :Bhupendra Verma 
#         class :MCA
#         clg : IISE"""
# # length of string:
# print(len(name1))
# print(len(name2))
# print(len(name3))
# # Print string:
# # print(name1)
# # print(name2)
# # print(name3)

# for char in name1:
#     print(char)
# name="   bhupendra verma"
# # string.find('char') :find character/substring in string:
# # and return first occurence of char or substring
# print(name.find('pe'),':',name.find('r'))
# # modifying srtrings to upper,lower
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

# # for removing stripping/removing  any trailing(before and after string) spaces
# print(name.strip())
# # replace substring of string 
# # string_name.replace(oldSubString,newSubString,count):count:if given then no. of count occurence will replace esle all the old substring replace with new substring
# print(name.replace('bhupendra','bhuvie',1))
# # stringName.split(separator,maxsplit)
# str="hii this is bhuvie .hii how are you"
# split_str=str.split('i')
# print(split_str)
# print("Hii! {name1} and {name2}".format(name1='bhuvie',name2='bhupendra'.upper()))
# # Assignment types:
# text='The unexpected always happens'
# print(text)
# print(len(text))
# print(text.find('pp')) #print index where it exist
# print('pp' in text) #OR
# if 'pp in text':
#     print("pp available")

# print(text[:11])
# print(text.replace('always','never'))
# text2='no matter what'
# text_final=text+text2
# print(text_final)

# # To check String is palindrome or not
# def ispalindrome(str):
#     str_rev=cls_str[::-1]
#     if str_rev==str:
#         return 1

# str=str(input("Enter String :"))
# cls_str=str.replace(" ","").lower()
# if ispalindrome(cls_str):
#     print(f"{str} is palindrome")
# else:
#     print(f"{str} is not palindrome")

