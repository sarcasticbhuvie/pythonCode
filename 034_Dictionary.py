phone_book={
    "key1": 'value1',
    "key2": 'value2'
} 
print(phone_book)
print(phone_book.keys())
print(phone_book['key1'])
print(phone_book['key2'])
print("----------in for loop------------")
for i in phone_book:
    print(phone_book[i])
for i,j in phone_book.items():
    print(i,':',j)

############################################
phone_book={
    "key1": 'value1',
    "key2": 'value2'
} 

# update
phone_book['key1']=256485
print(phone_book)

# insert new key pair
phone_book['key3']='value3'
print(phone_book)

# add two dictionary
d2={
    "name":"your name",
    "class":"class name"
}
phone_book.update(d2)
print(phone_book)
# delete a key pair
print(d2)
d2.pop('class')
print(d2)
d2.popitem() #delete last key pair
print(d2)

###############################
# Q.sum of all items in dictionary
dic={
    'a':25,
    'b':18,
    'c':45
}
# without using functions
sum=0
for x,y in dic.items():
    sum=sum+y
print(sum)
# using functions
# dic.values() :To find values of dictionary
# sum(dic.values()) : To find sum of these values SO:
print(sum(dic.values()))
# #################################
import string
alpha1=string.ascii_lowercase+string.ascii_uppercase
alpha2=(string.ascii_lowercase)[::-1]+(string.ascii_uppercase)[::-1]
dic=dict(zip(alpha1,alpha2)) # Making a dictionary of alpha and its reverse string.
str=str(input("Enter String :"))
index=int(input("Enter index :"))
str_fixed=str[:index-1]
str_mirror=str[index-1:]
for x in str_mirror:
    str_fixed+=dic[x]
print(str_fixed)
# #########################################
list=[]
for i in range(97,123):
    list.append(chr(i))
print(list)
#########################################
# second way to print it
import string
str=str(input("Enter String :"))
index=int(input("Enter index :"))
alpha_low_case=string.ascii_lowercase
alpha_upp_case=string.ascii_uppercase
str_fix=str[:index-1]
str_mirror=str[index-1:]
for ch in str_mirror:
    if ch in alpha_low_case:
        ind=alpha_low_case.index(ch)
        str_fix+=(alpha_low_case[::-1][ind])
    else:
        ind=alpha_upp_case.index(ch)
        str_fix+=(alpha_upp_case[::-1][ind])
print(str_fix)
        