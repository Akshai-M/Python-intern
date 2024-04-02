# #write a program to take string and to return the lenght of longest word in it
# # string=input("Enter a string:\n")
# # word=string.split()
# # lngst=0
# # for words in word:
# #     if len(words)>lngst:
# #         lngst=len(words)
# # print("Length of the longest word:",lngst)

# #to swap 1st and last character
# # string=input("Enter a string:\n")
# # if len(string)>=2:
# #     ns=string[-1]+string[1:-1]+string[0]
# #     print("Modified string:"ns)
# # else:
# #     print("String is too short.")

# #to remove odd index value in a character
# # s=input("Enter a string\n")
# # ns=s[::2]
# # print("Modified string:",ns)


# # print("enter the string : ")
# # while(1):
# #     s=input()
# #     if s=="QUIT" or s=="quit":
# #         break
# #     else:
# #         # print(s)
# #         len=int(len(s))
# #         print(f"Length of the string is:{len}")
# # print("thank you")

# # s=input("Enter a string which is graterthan 6 words\n")
# # r=len(s)
# # while(1):
# #     if r>=6:
# #         break
# #     else:
# #         print("Re-enter again")
# # print(s) 

# #LISTS
# #  list=[11,22,'k','m','o',[2,3,4],"akshai",True]
# # print(list,type(list))
# # print(list.[1:3])

# # list=[10,20,30]
# # lst4=[list*2]
# # print(lst4)

# # list=[50,20,30,60,10,40]
# # print(len(list))
# # print(min(list))
# # print(max(list))
# # print(sum(list))
# # print(any(list))
# # print(all(list))
# # # print(del(list[2]))
# # print(sorted(list))
# # # print(reversed(list))
# # r=list(reversed(list))
# # print(r)

# #append()
# # lst=[11,22,33,44,55,66,77,88]
# # print(lst)
# # lst.append(65)
# # print(lst)

# #count()
# # k=[11,22,11,44,11,66,11,88]
# # print(k)
# # print(k.count(11))

# #index()
# # print(k.index(11))
# # print(k.index(11,3))
# # print(k.index(11,1,9))

# #insert()
# # k.insert(2,'k')
# # print(k)

# #pop()
# # k.pop()#it will delete last value by default
# # k.pop(3)
# # print(k)

# #sort()
# # v=[44,22,11,55,33]
# # v.sort()
# # print(v)

# extend()
# =[11,22]
# v=['hi',33,44]
# k.extend(v)
# print(k)

#reverse()
# k=[11,22,33]
# k.reverse()
# print(k)

# #copy()
# k=[11,22,33,44,55]
# v=k[:]
# r=id(k)
# print(r)
# id(v)
# k.pop()
# print(k)

# print(dir(list))

#looping lists
# list=[11,22,33,44,55]
# for i in list:
#     print(i,end=" ")
# indx=0
# while indx<len(list):
#     print(list[indx],end=" ")
#     indx+=1

# list=[11,22,33,44,55]
# for j,i in enumerate(list): #enumerate() iterable value & index values
#     print(i,j)

#list comprehensions
# list=[1,2,3,4,5]
# dbl_list=[i**2 for i in list]
# print(dbl_list)

# list=[-12,84,11,22,-3,0,-25]
# pstv_list=[i for i in list if i>0]
# print(sorted(pstv_list))
# odd_list=[i for i in list if i!=0]
# print(odd_list)

#Read values into list
# value=int(input("Enter total no.of elements:"))
# list=[]
# for i in range(value):
#     ele=input(f"Enter element{i+1}:")
#     list.append(ele)
# print("List:",list)

# list=[]
# ele=int(input("Enter element:"))
# while ele!=0:
#     list.append(ele)
#     ele=int(input("Enter element:"))
# print("List:",list)

# tnoe=int(input("Enter the no.of elements:\n"))
# lst=[]
# for i in range(tnoe):
#     ele=int(input(f"Enter element{i+1}:"))
#     lst.append(ele)
# print("Org List:",lst)
# ps2=int(input("Enter no.of position to shift:"))
# rr1=lst[-ps2:]+lst[:-ps2]
# print(f"Right Rotated List:{rr1}")
# rr2=lst[ps2:]+lst[:ps2]
# print(f"Left Rotated List:{rr2}")

# tnoe=input("Enter the no.of elements:\n")
# lst=[]
# for item in tnoe:
#     o=input()
#     if item not in lst:
#         lst.append(item)
# print(f"Original List:{lst}")
# print(f"List with Unique Elements:{lst}")


# l=[]
# values=int(input(f"Enter the value:"))
# while values!=0:
#     l.append(values)
#     values=int(input(f"Enter the value:"))
# print(1)
# pstv_list=[i for i in l if i>0]
# print(sorted(pstv_list))
# ngtv_list=[i for i in l if i<0]
# print(ngtv_list)

usrnm=[]
accnt=[]
lmt=[]
while True:
    print("1.Add 2.View")
    ch=int(input("Enter choice:"))
    if ch==1:
        nm=input("Enter name:")
        while True:
            an=int(input("Enter A/c number:"))
            can=int(input("Confirm A/c number:"))
            if an==can:
                tl=int(input("Enter Limit:"))
                usrnm.append(nm)
                accnt.append(an)
                lmt.append(tl)
                print("Beneficiary added")
                break
            else:
                print("A/c not matched.Try again")
        print()
    elif ch==2:
        if len(usrnm)==0:
            print("List is empty")
        else:
            print("Name\t\tAccount\t\tLimit")
            print("------------------------")
            for i in range(len(usrnm)):
                print("%s\t\t%d\t\t%d"%(usrnm[i],accnt[i],lmt[i]))
    c=input("Do you want to continue: press(y/n)")
    if c=='n':
        break
