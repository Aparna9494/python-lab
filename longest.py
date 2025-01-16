n=int(input("enter the limit"))3
li=[]
for i in range(n):
    word=input("enter a string")
    li.append(word)
print(li)
max=len(li[0])
temp=li[0]
for i in li:
    if(len(i)>max):
        max=len(i)
        temp=i
print("the word having longest length is",temp,"with langth",max)

