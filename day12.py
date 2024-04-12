# class variable vs object variable :-
# class Circle:
#     pi=3.14159
#     def __init__(self,r):
#         self.radius=r
#     def area(self):
#         return self.pi*self.radius**2
# c1=Circle(5)
# c2=Circle(10)
# print("Radius=%.2f\tArea=%.2f"%(c1.radius,c1.area()))
# print("Radius=%.2f\tArea=%.2f"%(c2.radius,c2.area()))

#__del__() :-
# it's automatically called when the obj is del,either explicitly using the del keyword 
# or when there are no more reference to the obj
# class Employee:
#     def __init__(self):
#         print("Object created")
#     def __del__(self):
#         print("Destructor called,Object deleted")
# obj=Employee()
# del obj

# __len__() :-
# class emp:
#     def __init__(self,name,id_no):
#         self.n=name
#         self.ind=id_no
#     def display(self):
#         print(self.n,self.ind)
#     def __len__(self):
#         return len(self.n)
# e1=emp("Akshai",122)
# e1.display()
# print("Length of",e1.n,"is",len(e1))

#coverting an instance to a string
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
# p=Point(15,25)
# print(p)

# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     def __str__(self):
#         return "({0},{1})".format(self.x,self.y)
# p=Point(15,25)
# print(p)
class midpoint:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.m1=(x1+x2)/2
        self.m2=(y1+y2)/2
        self.midpoint=self.m1,self.m2
    def display(self):
        print("The midpoint is:",self.midpoint)
x1=int(input("Enter the value for x1:"))
x2=int(input("Enter the value for x2:"))
y1=int(input("Enter the value for y1:"))
y2=int(input("Enter the value for y2:"))
x=midpoint(x1,x2,y1,y2)
x.display() 