a=input("enter a string: ")
b=a[0]
s=a[1:]
for i in range (len(s)):
    if s[i]==a[0]:
        b=b+'$'
    else:
        b=b+s[i]
print(b)
