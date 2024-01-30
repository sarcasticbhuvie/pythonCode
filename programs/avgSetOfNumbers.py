count = int(input("Enter the number count :"))
sum=0
for i in range(count):
    temp = int(input(f"Enter number {i+1} :"))
    sum=sum+temp
print(f"Average of {count} numbers is {sum/count}")