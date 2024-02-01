# list=["bhupendra","verma",'MCA']
# #indexing  -3       -2      -1
# print(list[-1])
# # print(list[-4]) # give error: indexError: 
# # ====================================
# # to search element in list
# if "MCA" in list:
#     print("MCA available")
# else:
#     print("MCA not available")
# # =======================================
# # append(value): add value at end
# print(list)
# list.append("IISE")
# print(list)
# # ===========================================
# # insert(index,value): add value to given index
# print(list)
# list.insert(2,"56")
# print(list)
# # ===========================================
# # extend(): list1.extend(list2):list2 to added in list1
# list1=[10,20,30,40]
# print(list1)
# list1.extend(list)
# print(list1)
# # ===========================================
# # pop():pop(2):remove last element or if your given index
# print(list)
# list.pop()
# print(list)
# print(list.pop(0))
# print(list)
# # ===========================================
# # remove(value): value will me removed
# print(list)
# list.remove("MCA")
# print(list)
# # ===========================================
# # sort():list.sort():list.sort(reverse=True)
# # reverse():list.reverse()
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.sort()
# print(list)
# list.reverse()
# print(list)
# # ===========================================
# # List Comprehension :When we want to make a new list from existing list.
# list1=[10,20,30,40,50,60,70,80,90]
# newlist=[]
# for i in list1[4:]:
#     newlist.append(i)
# print(newlist)
# # other way to write
# newlist=[x for x in list1[0:6]]
# print(newlist)
# # ===========================================
# # Nested List:
# list.insert(2,["hello","world!"])
# print(list)
##############################################
# 
# list2=[10,20,30,40,50,60,70,80,90,100]
# def number(msg):
#     return int(input(msg))
# index1=number("Enter index 1 :")
# index2=number("Enter index 2 :")
# print(f"List Before swaping :{list2}")
# Swapping using list methods()
# temp=list2[index1]
# list2.pop(index1)
# list2.insert(index1,list2[index2-1])
# list2.pop(index2)
# list2.insert(index2,temp)
# print(f"List after swaping :{list2}")

# # ============================================
# swapping without methods
index_one=int(input("Enter first index :"))
index_second=int(input("Enter second index :"))
list=[10,20,30,40,50,60]
print("List before swapping element",list)
temp=list[index_one]
list[index_one]=list[index_second]
list[index_second]=temp
print("List after swapping element",list)
# # ==================================================