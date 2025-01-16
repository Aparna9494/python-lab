n=int(input("enter the limit"))
li=[]
for i in range(n):
    x=str(input("entre a name"))
    li.append(x)
print(li)
c=0
for j in li:
    for k in j:
        if 'a' in k.lower():
             c=c+1
print(c)
