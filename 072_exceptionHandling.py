a=int(input("Enter number :"))
b=int(input("Enter number :"))
try:
    result = a/b
except ZeroDivisionError:
    result=None
    print("Error: Cannot devide by Zero.")
    # exit()
finally:
    print("Division completed :",result)

# print("hello")