# def outer_funt():
#     def inner_funt():
#         print("Hello")
#     inner_funt()
# outer_funt()

#Recursive function
# def gcd(n,m):
#     if m==0:
#         return n
#     else:
#         return gcd(m,n%m)
# n=25
# m=75
# result=gcd(n,m)
# print(f"The gcd of {n} and {m} is:{result}")
# print(25%75)

#filter()
# def evn(n):
#     return n%2==0
# num=range(21,30)
# evn_list=list(map(evn,num))
# print(evn_list)

#map()
# def evn(n):
#     return n**2
# num=[1,2,3,4,5]
# evn_list=list(filter(evn,num))
# print(evn_list)

#reduce()
# from functools import reduce
# def add(x,y):
#     return x+y
# num=[1,2,3,4,5]
# result=reduce(add,num)
# print(result)

# def nm():
#     print("Name:----")
#     def rno():
#         print("Roll NO:-----")
#         # print(__name__)
#     rno()
# nm()


#importing a module
# def nm():
#     print("Name:Mighty Raju")
# def id():
#     print("Identity:Gidda")


# import math
# print(math.pi)
# print(math.e)
# print(math.factorial(5))
# print(math.floor(9/2))
# print(math.gcd(50,90))
# print(math.pow(2,8))
# print(math.sqrt(9801))

# import time
# print(time.gmtime())
# print(time.asctime())
# print(time.strftime("%H:%M:%S"))

# import time
# def ts():
#     print("Red light-stop!")
#     time.sleep(1)
#     print("Yellow light-Prepare to stop!")
#     time.sleep(5)
#     print("Green light-Go!")
#     time.sleep(15)
# for i in range(8):
#     ts()

# import random
# print(random.randint(11,22))
# lst=[10,20,'akshai',40,50]
# random.shuffle(lst)
# print(lst)
# print(random.choice(lst))

# Advantages Packages
# -Modular Organization:
# import pkg.details
# pkg.details.nm()
# pkg.details.id()

#try and except:-
# n=int(input("Enter numerator:"))
# m=int(input("Enter denominator:"))
# try:
#     q=n/m
#     print("Quotient:",q)
# except ZeroDivisionError:
#     print("Denominator can not be ZERO")

# n=int(input("Enter numerator:"))
# m=int(input("Enter denominator:"))
# if m!=0:
#     q=n/m
#     print("Result:",q)
# else:
#     print("It can't be determined")

#try and except and except.....
# try:
#     n=int(input("Enter Numerator:"))
#     d=int(input("Enter Denominator:"))
#     q=n/d
#     print("Quotient:",q)
# except ZeroDivisionError:
#     print("Denominator can not be zero")
# except ValueError:
#     print("Invalid data type")

#except block without exception:-
# try:
#     n=int(input("Enter Numerator:"))
#     d=int(input("Enter Denominator:"))
#     q=n/d
#     print("Quotient:",q)
# except ZeroDivisionError:
#     print("Denominator can not be zero")

# except:
#     print("Unkown Error")

#finally block:-
# try:
#     print("Rasising an error")
#     raise ValueError
# finally:
#     print("In finally Block")
d1={}
print("WELCOME TO TICKET BOKING")
while True:
    print("\n1.Book ticket 2.View 3.Exit")
    ch=int(input("Enter the choice"))
    if ch==1:
        name=input("Enter your name:")
        age=int(input("Enter your age:"))
        depature=input("Enter depature:")
        destination=input("Enter destination:")
        seat=int(input("Enter the no.of seats you want to book:"))
        d1=[name,age,depature,destination,seat]
        print("Booked successfully")
    elif ch==2:
        print("Name:\tAge:\tDepature:\tDestination:\tSeat:")
        for i in d1:
            print(i,end='\t')
    elif ch==3:
        break