#BASIC PYTHON POGRAM

# #print the line
print("sorna sree")
print('40')
# multiply the string
print('*'*10)
#initialize the value
price=10
prince=20
rating=9.0
name="sorna"
#boolean value
is_published=True
print(price)
name="john Smith"
age=20
is_new=True
name=input("what is your name: ")
favourite_clr=input("enter your favourite clr: ")
print(name +" likes " +favourite_clr)

#find the type

birth_year=input(("enter the birth year: "))
print(type(birth_year))
age=2022-int(birth_year)
print(type(age))
print(age)
#weight program
weight=input("enter the weight: ")
weight_kgs=int(weight)*0.45
print(weight-weight_kgs)
#terminate loop
course='python'
print(course[1:-1])
#format string
first="sorna"
last="sree"

message=first+'[' +last +'] is a code'
msg=f'{first}' '[{last}] is a code'
print(message)
print(msg)
course="sorna sree"
#fing the length
print(len(course))
#change the upper case and replace functions
print(course.upper())
print(course.replace("sorna","s.sorna"))
print(course in "sorna")
x=10+3*2**2
print(x)
#paranthesis,exponentiation,multiplication or division addition or subraction
x=2.9
print(round(x))
x=2.9
print(abs(-2.9 ))
#absolotly value
import math
print(math.floor(6.0))
print(math.ceil(6.9))
#if statement
is_hot=False
is_cold=True
if is_hot:
    print("IT's hot day")
elif is_cold:
    print("its cold day")
else:
    print("IT's lovely day")
print("enjoy the day")
#example if statement program
price=1000000
good_credit=False
if good_credit:
    print((price*10)/100)
else:
    print(f'down payment {(price*20)/100}')
#logical operator
high_income=True
good_credit=True
if high_income or good_credit:
    print("loan")
else:
    print("not give loan")
#both conditon true AND
# atleast one condition TRUE
temparature=input ("Enter the temparature: ")
if int(temparature)>=30:
    print("Its a hot day:")
elif int (temparature)<=10:
    print("its a day cold")
else:
    print("its neither hot not cold")
name=input("enter the name")
characters=len(name)
if characters<=3:
    print("long name must be at least 3 characters")
elif characters>=50:
    print("long name can be a maximum 50 charaters")
else:
    print("name looks good!")
#weight converter
weight=int(input("enter the weight"))
unit=input("(L)b or (K)g")
if unit.upper()=='L':
    convert=weight*0.45
    print(f"cconvert {convert} kilograms")
    
#while loop
i=1
while i<=5:
    print(i)
    i+=1
print("done")
#guess number
secret_number=9
n=5
while(n>=5):
    guess=int(input("enter the number"))
    n=-1
    if(secret_number==guess):
      print("you win the game")
      break
    
else:
    print("you loss!")
    #car game
'''from ast import Break
from pickle import TRUE'''


#car=input("enter the stop or start or quite")
while True:
    car=input("enter the stop or start or quite")
    car=car.lower()
if str(car) =='start':
    print("start the car")
elif str(car) =='stop':
    print("stop the car")
elif str(car) =='quite':
    print("quite the car")
    Break

else:
    print("i dont know understand")
#for loop
for item in "python":
 print(item)
for item in ["python","sorna","sree","riya"]:
    print(item)
for item in range(5,10,2):
    print(item)
price=[10,20,30]
total=0
for prices in price:
    total=total+prices
print(total)
#Nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')
numbers=[5,2,5,2,2]
for x_count in numbers:
    print(x_count*"X")
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)
    
#list
numbers=[90,80,34,58,68,49]
max=numbers[0]
for i in numbers:
    if i>max:
        max=i
print(max)
# 2d list
matrix=[
    [1,2,3],
    [2,3,4],
    [3,4,5]
]
for row in matrix:
    for item in row:
        print(item)
matrix [0][2]=50
print(matrix[0][2])
#List Method
from enum import unique


numbers=[2,3,45,54,6,3,2,3,2]
unique=[]
for number in numbers:
    if number not in unique:
        unique.append(number)
        
print(unique)
numbers.append(39)
numbers.insert(0,5)
numbers.remove(45)
numbers.index(54)
print(numbers)
print(3 in numbers)
#Tuples
from unicodedata import name


items=(2,1,2,3,4)
print(items)
#unpacking
coordinates=(3,2,4)
x,y,z=coordinates
print(x*y*z)
#dictionaries
customer={"name":"sorna",
          "age":48 ,
          "is_verify":True }
customer["birth_date"]="aug-31"
print(customer["name"])
#phone numbers
numbers={"1":"one","2":"two","3":"three"}
output=""
phone_no=(input("enter the number"))
for ch in phone_no:
    output+=numbers.get(ch,)+ " "
print(output)
#emoji converter
from email import message


message=input("enter the message")
words=message.split("")
#functions
name=input("enter the name")
def greet_user(name):
    print("hii i am",name)
print("Welcome aborded")
greet_user(name)
print("finish")
#parameters
#key arguments
#return valued
from multiprocessing import reduction


def square(a):
    return a*a
result=square(5)
print(square(8))
print(result) 
#Exseption
try:
    age=int(input("Enter the age:"))
    print(age)
except ValueError:
    print("Invalied va;ue") 
#classes
from re import X
from unicodedata import name


class Point:
    def __init__(self,name):
        self.name= name
    def talk(self):
        print(f'i am {self.name}')
sorna=Point("sorna")
sree=Point("sree")
sorna.talk()
sree.talk()
#inheritance
class Mummal:
    def walk(self):
        print("walk")
class Dog(Mummal):
    pass
class Cat(Mummal):
    pass
dog1=Dog()
dog1.walk()
#Modules













    


        