list = ["Bhupendra","verma",420,56,111]
list1 = ["Bhuvie","kurmi","verma",20,56]
#index   0/-3        1/-2   2/-1
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-6]) # IndexError : out of index bcoz of no index found
print(list[1:4]) # print all element after index 1 and 4(axcept index 4)
print(list[:3]) # print all element before index 3(axcept index 3)
print(list[2:]) # print all element aftre index 2(with index 2)
print(list[-4:-2]) # print all element aftre index -4 to -2(except index -2) 
print(len(list))
# To check element in list
if "verma" in list:
    print("Verma is available in list")
list[-4:-1]=[000,111,999]
list.insert(len(list),"end")
print(list)
list.append("appendedItem")
print(list)
list.extend(list1)
print(list)
list.remove(111) # remove only first 111 element
list.remove(111)
print(list)
list.pop()
print(list)
list.pop(4)
print(list)
del list[3]
print(list)
list.clear() # IT MAKE LIST EMPTY
list.append("FirstAppend")
print(list)
del list # IT WILL DELETE THE LIST
for i in list1:
    print(i)

for i in range(len(list1)):
    print(list1[i])

[print(i) for i in list1]

name=["bhupendra","anurag","mohit","shaswat","pragyan"]
nameSort = []
for i in name:
    if 'a' in i:
        print(i)
        nameSort.append(i)
print(nameSort)
nameSort.clear()
# In sort for we can write that code as
[ print(i) for i in name if 'a' in i] # to print only
nameSort =[i for i in name if 'a' in i] # to print only
print(nameSort)
# accept number lower then 50
list = [10,60,20,80,40,45,50,60,20]
newlist = [list[x] for x in range(len(list)) if list[x]<50]
print(newlist)

list=[10,30,60,50,90,20,30,50,40]
def fabs(n):
    return abs(n - 50)
list.sort(key=fabs)
print(list)

list3=[10,30,60,50,90,20,30,50,40]
def printlist(a):
    # print(a) 
    return a
list3.sort(key=printlist)
