players={'p1':{'nm':'Rohit','jrsy':45},
        'p2':{'nm':'Kohli','jrsy':18}
        }
for n,j in players.items():
    print(n,j) 
return id
#fromkeys()
# keys=['K','V','S']
# values=1122
# dct=dict.fromkeys(keys,values)
# print(dct)

#get()
# d={'K':11,'V':22,'S':19}
# d={'K':11,'V':22,'S':19}
# print(d.get('K',-1))
# print(d.get('S',-1))
# print(d.get('V'))
# print(d['V'])

#key()
# d={'a':11,'k':12,'s':13}
# for i in d.keys():
#     print(i,end=' ')
# d={'a':11,'k':12,'s':13}
# for i in d:
#     print(i,end=' ')

# values()
# d={'a':11,'k':12,'s':13}
# for i in d.values():
#     print(i,end=' ')

#items()
# d={'a':11,'k':12,'s':13}
# for i,(j,k) in enumerate(d.items()):
#     print(i,j,k)

#update()
# d1={'a':11,'k':12,'s':13}
# d2={'h':14,'a':15,'i':16}
# print(d1,d2)
# d1.update(d2)
# print(d1)

#setdefault()
# d={'a':11,'k':12,'s':13}
# d.setdefault('a',25)
# print(d)

# print(dir(dict))
# print(ord(' '))

# d={}
# for i in range(3):
#     k=input()
#     v=int(input())
#     d[k]=v
#     print(d)

# d=str(input())
# for i in d.items():
#     print(i,end='')

# s=input("Enter a string:")
# freq={}
# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)



# crd={}

# for i in range(3):
#     un=input("Enter a username %d:"%i)
#     ps=input("Enter a password:")
#     crd[un]=ps

# lus=input("Enter a new username:")
# lps=input("Enter a new password:")

# if lus in crd:
#     if crd[lus]==lps:
#         print("Match found")
#     else:
#         print("User is not found")
# else:
#     print("Not found")


# import random
# accnt={}
# avl_bal={}
# while True:
#     print("1.Create A/c 2.View 3.Exit")
#     ch=int(input("Enter choice:"))
#     if ch==1:
#         while True:
#             ac_nmbr=random.randint(100000,999999)
#             if ac_nmbr not in accnt:
#                 hldr_nm=input("Enter A/c holder name:")
#                 blnce=int(input("Enter A/c holder name:"))
    
#     elif ch==2:
#         if len(accnt)==0:
#             print("No accounts")
#         else:
#             for i,j in accnt.item():
#                 print(i,j,avl_bal[i])
#     else ch==3:
#         break

#functions:parameter and return type
# def add(n1,n2):
#     sm=n1+n2
#     return sm
# n1=float(input("Enter the 1st number:"))
# n2=float(input("Enter the 2nd number:"))
# rs=add(n1,n2)
# print("Sum of %.2f  and %.2f is %.2f"%(n1,n2,rs))
# def add(n,m):
#     res=n+m
#     return res
# a=int(input("Enter the 1st number:"))
# b=int(input("enter the 2nd number:"))
# r=add(a,b)
# print("Sum of %d and %d is:%d"%(a,b,r))

#parameter with no return type
# def add(n,m):
#     return n+m

# Local vs Global variable : 
# num1 = 11  
# num2=69  # Global
# def show():
#     num1 = 12     # Local
#     num2 = 23
#     print(num1)
#     print(num2)
# show()
# print(num1)
# print(num2)   # Error because its local
    
# num1 = 1122
# def show():
#     global num2
#     num2 = 12
#     num3 = 33
#     print(num1)
#     print(num2)
#     print(num3)
# show()
# print(num1)
# print(num2)

# def operation(n,m):
#     if operator=="+":
#         result=n+m
#         return result
#     elif operator=="-":
#         result=n-m
#         return result
#     elif operator=="*":
#         result=n*m
#         return result
#     elif operator=="/":
#         result=n/m
#         return result
#     elif operator=="%":
#         result=n%m
#         return result
#     else:
#         print("Give a valid operator")
    


# n=float(input("Enter first number : "))
# m=float(input("Enter second number : "))
# operator = input("Enter operator : ")
# print("The result of the operation is :",operation(n,m))

#positional arguments
# def details(n,r):
#     print(n.upper(),r)
# nm="k v"
# rnk=1122
# details(nm,rnk)

# def k_a(iv,fv):
#     print(iv,fv)
# k_a(fv=25.19,iv=1122)
# k_a(fv='python',iv=1122)
# k_a(fv='hi',iv='program')
# k_a(fv=25.19,iv=1122)

# def v_a(*args):
#     print()
#     for var in args:
#         print(var,end=' ')
# v_a(1122)
# v_a(1122,25.19)
# v_a(1122,25.19,'python')
# v_a(1122,25.19,'python','programming')


# def v_a(**kwargs):
#     print()
#     for name,val in kwargs.items():
#         print(name,val,end=' ')
# v_a(a=1122)
# v_a(a=1122,b=25.19)


# def k_a(iv,fv=12):
#     print(iv,fv)
# k_a(iv=25.19)


# def cb(x):
#     '''Cube of a number'''
#     print(x**3)
# print(cb.__doc__)
# cb(5)
# print(dir(set))

# def p(l1,l2):
#     print(l1,l2)
# l = [1,2,3,4]
# t = (5,6,7,8)-
# p(l,t)

# def f(x):
#     return x+2
# x=9
# print("Result:%d"%f(x))
# def f2(y):
#     return
# f=input("give name:")
# word=f.split()
# ini=" "
# for wor in word:
#     ini=ini+wor[0]
# print("Ini:",ini.upper())