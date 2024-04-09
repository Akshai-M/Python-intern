#read()
# f=open('biodata.txt','r')
# data=f.read()
# # data=f.readline(25)
# print(data)
# print("File read succesfully")
# f.close()

#write()
# f=open('biodata.txt','w')
# data=f.write("Yeah\nNo")
# f.close()
# f=open('biodata.txt','r')
# data=f.read()
# print(data)
# # print("File read succesfully")
# f.close()

#using list or tuple
# l=['akshai kumar'] #l=('')
# f=open('biodata.txt','w')
# data=f.writelines(l)
# print(data)
# f.close()

#file.name:Return the name of the file
#file.mode:Returns the access mode with which the file was opened
#file.closed:Returns true if the file is closed else false
#file.readable(),file.writable(),file.seekable():Returns true it done these operations

# f=open('biodata.txt','r')
# data=f.read()
# print(data)
# print(f.name)
# print(f.mode)
# print(f.readable())
# print(f.writable())
# print(f.seekable())
# print("File read succesfully")
# f.close()
# print(f.closed)

#Opening file using "with" keyword
#execute a operation and closure automatically

# with open('biodata.txt','r') as akshai:
#     data=akshai.read()
#     print(data)
# print("File closed:",akshai.closed)

#seek():before reading/writing it'll move to desired position
# syntax: 
# seek(offset,reference)
# offset: +ve means cursor moves forward,-ve means backwards
# reference: determines the point for offset.it takes three values
# 0(default):beginning of the file
# 1:current position of the file cursor
# 2:relative to the end of the file

#if the file is opend with binary it'll print b at o/p 
# with open('biodata.txt','rb') as akshai:
#     akshai.seek(2,1)
#     data=akshai.read(7)
#     print(data)

# with open('biodata.txt','rb') as akshai:
#     akshai.seek(4,1)
#     p=akshai.tell()
#     print(p)
#     data=akshai.read(7) #(7):7 palces it'll move
#     print(data)

# import os
# os.rename("hi.py","hai.py")
# os.remove("hai.py")
# with open('RESULTS-1.jpg','rb') as f:
#     d=f.read()
#     print(d)

#class and objects
# class Test:
#     name=None
#     id=None
#     def details(self,nm,iid):
#         self.name=nm
#         self.id=iid
#     def display(self):
#         print(self.name,self.id)
# e1=Test()
# e1.details("Akshai",25)
# e1.display()

class he:
    # n=None
    # m=None
    def __init__(self,num1,num2):
        self.n=num1
        self.m=num2
        self.res=num1+num2
    def display(self):
        print(f"Sum of {self.n} and {self.m} is:{self.res}")
num1=int(input("Enter a value:"))
num2=int(input("Enter a value:"))
obj=he(num1,num2)
obj.display()