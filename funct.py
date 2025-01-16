def largest(a,b,c):
    if a>c and a>b:
        print(a," is largest")
    elif b>a and b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")
print("enter three numbers")
num1=int(input())
num2=int(input())
num3=int(input())
largest(num1,num2,num3)