number=int(input("enter your number"))

temp=number
digits=len(str(number))

resultmaker= 0

while  temp > 0:
    rem=temp%10
    resultmaaker=resultmaker+rem**digits
    temp=temp//10

if number=resultmaker:
    print("the number is armstrong")

else:
    print("the number is not armstorng")
    

