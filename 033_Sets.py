# name={"bhupendra","verma"}
# print(type(name))
# print(len(name))
# print(name,"-------------------")
# for i in name:
#     print(i)
# ####################
# name={"bhupendra","verma"}
# if 'bhupendra' in name:
#     print('yes bhupendra hai')
# name.add('mca') 
# print(name)
# name.add('mca')
# print(name)
# list=['10',10,30,20]
# name.update(list)
# print(name)
# name.remove(10)
# print(name)
# # name.remove(600) # if 600 not in name then it will give error
# name.discard(600) # if 600 not in name,also it will work
# ###############################################
# # joining two set
# s1={10,30,50,60,70,40,100}
# s2={10,20,30,40,50,60}
# # Union : to keep all values of two sets besides duplicate values
# s=s1.union(s2)
# print(s)
# # intersection : to keep only duplicate values
# s=s1.intersection(s2)
# print(s)
# # s1.intersection_update(s2)
# # print(s1)
# s=s1.symmetric_difference(s2)
# print(s)
# ############################################
# # find common element in three lists using sets
# a=[1,5,10,20,40,80]
# b=[6,7,20,80,100]
# c=[3,4,15,20,30,70,80,120]
# s1=set(a)
# s2=set(b)
# s3=set(c)
# s1.intersection_update(s2)
# s1.intersection_update(s3)
# print(s1)
# ##############
# lis1t=[10,10,10,30,20,50]
# set1=set(lis1t) #remove duplicates
# f=list(set1)
# print(f)
# print(set1)
#########################################