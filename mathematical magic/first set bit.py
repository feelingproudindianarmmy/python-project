def firstsetbit(n):
    count=0
    while(n):
        if(n&1==1):
            count+=1
            n>>=1 
    return count
n=int(input("enter any number"))
print(firstsetbit(n))