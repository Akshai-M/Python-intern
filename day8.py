# # tpl=(11,22,'k','v','KV',65.75,True,False)
# # print(tpl)
# # print(type(tpl))

# # rp=()

# # type(rp)
# # vp=(1122)
# # type(vp)

# # tpl=(1122,)
# # type(tpl)

# #Looping in Tuples
# # tpl=(11,22,33,44,55)
# # for i in tpl:
# #     print(i,end=' ')

# #while loop in tuple
# # tpl=(11,22,33,44,55)
# # indx=0
# # while indx<len(tpl):
# #     print(tpl[indx],end=' ')
# #     indx=indx+1

# #range
# # tpl=(11,22,33,44,55)
# # for i in range(len(tpl)):
# #     print(tpl[i],end=' ')

# #enumerate
# # tpl=(11,-22,33,-44,55)
# # for i,j in enumerate(tpl):
# #     print(i,j)

# # k=11,22,33,44,55
# # print(k[0])
# # print(k[0]==11)
# # print(k[0:3])
# # del(k)

# # s=([11,22,33],[1,2,3],"python")
# # print(s)
# # print(s[0])
# # print(s[0][1])
# # print(s[1])
# # print(s[1][2])

# # tpl=([11,22,33],(44,55))
# # for i in tpl:
# #     print(i,end=' ')

# # tpl=([11,22,33],(44,55))
# # tpl[0][1]='k'
# # print(tpl)

# # (x,y)=(10,20)
# # unpack a tuple using *
# # k=(11,22,33,44)
# # s=(1,2,*k,3,4)
# # print(s)

# #packing a tuple
# # l=55,44,33
# # print(l)
# # k,*l=11,22,19
# # print(k,l)

# #disposal variable(_)
# # f,*_,l=(11,22,33,44,55)
# # print(f)
# # print(l)
# # print(_)

# #built-in ()
# # t=(12,15,13,26,49,50)
# # print(len(t))
# # print(max(t))
# # print(min(t))
# # print(sum(t))
# # print(any(t))
# # print(all(t))
# # print(sorted(t))
# # print(tuple(reversed(t))) #tuple should be used

# # print(dir(tuple))

# #zip()
# # players=["kohli","Rohit"]
# # jersey_number=[18,45]
# # tm=list(zip(players,jersey_number))
# # print(tuple(tm))
# # print(list(tm))

# #Tuple comprehension
# # lst=[1,2,3,4,5]
# # dtpl=tuple(i**2 for i in lst)
# # print(dtpl)

# # lst=[-12,84,11,22,-3,0,-25]
# # pstv_tpl=tuple(i for i in lst if i>0)
# # print(pstv_tpl)
# # odd_tpl=tuple(i for i in lst if i%2==0 and i>0)
# # print(odd_tpl)

tpl=()
n=int(input("Enter no.of ele in tuple:"))
for i in range(n):
    ele=int(input())
    tpl=tpl+(ele,n)
print(tpl)

# # import random
# # otp=random.randint(1000,2000)
# # d=input("enter")
# # for i in d:
# #     print(i)

# # dep=()

# import random
# min_bal=5000
# avl_bal=min_bal
# acc_mn=12345
# trnsc=()
# while True:
#     print("1.To do transactions 2.View 3.Exit")
#     ch=int(input("Enter your choice:"))
#     if ch==1:
#         ty=input("For deposit/withdraw:press(D/WD):")
#         if ty.upper()=='D':
#             deposit=int(input("Enter Deposit amount:"))
#             avl_bal=avl_bal+deposit
#             t_id=random.randint(100000,999999)
#             trnsc=trnsc+((t_id,acc_mn,ty,avl_bal))
#             print("Deposit Done")
#         elif ty.upper()=='WD':
            
#             depoit=int(input("Enter withdraw amout:"))
#             if deposit<avl_bal:
#                 avl_bal=avl_bal-deposit
#                 t_id=random.randint(100000,999999)
#                 trnsc=trnsc+((t_id,acc_mn,ty,acc_mn,avl_bal))
#                 print("WithDraw Done")
#             else:
#                 print("Insufficient Balance:Try again")
#     elif ch==2:
#         if len(trnsc)==0:
#             print("No transaction")
#         else:
#             for i in trnsc:
#                 print(*i)
#     elif ch==3:
#         break

#create set

# k={}
# print(type(k))
# k={1122,2191.22191,'k v',True,1122}
# print(k)
# v={1122,2191.22191,True,1122,'k v',}
# print(v)

#looping in set
# st={11,22,33,44,55}
# for i in st:
#     print(i,end=' ')

# k={11,22,33,44,55,99}
# print(k)
# k.add(100)
# print(k)

# k={11,22,33,44,55,'akshai'}
# v={5,4,3,2,1,'kumar'}
# k.intersection_update(v)#intersection(&)
# print(k)

# k={33,22,11,44}
# v={33,66,44,55}
# k.difference(v) #diffenerce(-)
# print(k)

# k={33,22,11,44}
# v={33,66,44,55}
# k.difference_update(v)  #diffenerce_update(-=)
# print(k)

# k={33,22,11,44}
# v={33,66,44,55}
# k.symmetric_difference_update(v)  #symmetric_update(=^)
# print(k)

# k={33,22,11,44}
# v={33,66,44,55}
# k.isdisjoint(v)  #disjoint(=^)
# print(k)

# k={33,22,11,44}
# v={33,66,44,55}
# k.issubset(v)  #issubset(<=)
# print(k)

# k={33,22,11,44} 
# v={33,66,44,55}
# k.issuperset(v)  #issubset(<=)
# v.issuperset(k)  #issubset(<=)
# print(k)
# print(v)

# print(dir(set))
# print(dir(str))

#dictionary properties
# d={ }
# print(type(d))

# d3={'k':'11','z':'22','k':'19'}
# print(d3)

# #d4={'k':'11','z':'22','k':'11'}
# #print(d4)

# d2={'A':'65','Z':'91','K':'V'}
# del(d['A'])
# print(d2)
n=input("Enter your name:")
print(f"HELLO!,{n}")