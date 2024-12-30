class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
n1=input("enter a name: ",)
a1=int(input("enter the age: "))
p1=Person(n1,a1)
n2=input("enter a name: ",)
a2=int(input("enter the age:"))
p2=Person(n2,a2)
if a1>a2:
    print(n1,"is elder")
else:
    print(n2,"is elder")
