a=int(input("enter a number"))
b=int(input("enter a number"))
i=1
while(i<=a and i<=b):
    if(a%i==0 and b%i==0):
        gcd=i
    i+=1
print(gcd)