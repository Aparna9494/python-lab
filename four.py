import math
start=int(input("enter the starting number"))
end=int(input("enter the ending range"))
perfect=[]
for i in range (start,end+1):
    flag=0
    num=i
    while num>0:
        digit=num%10
        if digit not in[0,2,4,6,8]:
         flag=1
         break
        num=int(num/10)
    if flag==0 and math.sqrt(i)%1==0:
        perfect.append(i)
print(perfect)


