class Time:
    def __init__(self,h,minute,second):
        self.hour=h
        self.minute=minute
        self.second=second
    def __add__(self,other):
        h=self.hour+other.hour
        minute=self.minute+other.minute
        second=self.second+other.second
        if(second>=60):
            minute=minute+int(second/60)
            second=second%60
        if minute>= 60:
            h = h + int(minute / 60)
            minute = minute % 60
        t3=Time(h,m,s)
        return t3
    def display(self):
        print("hour:minute:second")
        print(f"{self.hour}:{self.minute}:{self.second}")
t1=Time(4,70,80)
t2=Time(8,60,30)
t3=t2+t1
t3.display()


