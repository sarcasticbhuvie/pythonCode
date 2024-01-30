#sum of digits is even or odd
for i in range(100,201):
    sum=0
    num=i
    while num!=0: #i=102
        mod=num%10    #mod=2,0,1
        sum=sum+mod #sum=0+2+0+1
        num=num//10 #i=10,1
    if sum%2==0:
        print(i)
