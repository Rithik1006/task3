name = "Lissa"
age  = 35
print(name) #variables


#conditional statement
a=int(input("Enter your age"))
if (a>=18):
    print("you can vote to elect a good leader.")
else:
    print("you can't vote.")
# short hand cs
num=23
print("+ve num") if (num>=0) else print("-ne num")


#loops
#their are 2 types of loops 1)for loops and 2)while loop
count=1
for i in range(5):
    print(i)
    # result=i*count
    # print(i,'*',count,'=',result)
    # count+=1



num=int(input("enter the number"))
count=1
while count<=10:
    result=count*num
    print(num, "*", count, "=", result)
    count+=1#tables

y=3
count=1
while count<=11:
    result=count*y
    print(y,'*',count,'=',result)
    count+=2

# list
var=['a','b','c','d']
# print(var)
print(var[3])
print(var[:3])
print(len(var))
var.append('e')
print(var)
var.pop() # is removes the items from back side of the list
print(var)

# Tuples
t=('a','b','c','d')
print(len(t))
print(t + ('e','f'))

#dictionaries
n={'name':'ravi','age':23}
n['place']='india'
print(n)
print(n.keys())

#sets
s={'a','b','c','d'}
s.add('e')
s.remove('c')
print(s)
print(len(s))
s2={'a','c','f','e'}
print(s & s2)
print(s - s2)
#function
def cage(cy,by):
    a=cy-by
    print(a)
cage(30,10)

def greet(name):
    print("Hello,", name)

greet("Alice")

#class and objects
class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def setting(self, model):
        self.model=model
    def getting(self):
        return self.model
    def des(self):
        return f"this is {self.make} {self.model} {self.year}."
# model=(input("model of the car"))
a=Car("toyota","etios",2016)
# a.setting("innova")
print(a.getting())
print(a.des())

