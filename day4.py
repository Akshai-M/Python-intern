'''two way selection'''
'''day=input("Enter the day\n")
if day.lower()=="sunday":
    print("Holiday")
else:
    print("Not a holiday")'''

'''a=int(input("Enter your age\n"))
b=(input("Enter your weight(in kg's)\n"))
if ((18<=a<=55)and(b>=45)):
    print(1)
else:
    print(0)'''

'''cost_of_product=float(input("Enter the cost\n"))
selling_priceof_product=float(input("Enter the selling price\n"))
if selling_priceof_product>cost_of_product:
    res=selling_priceof_product-cost_of_product
    print("Profit:",res)
elif selling_priceof_product<cost_of_product:
    rest=cost_of_product-selling_priceof_product
    print("Loss:%.5f"%rest)
else:
    print("You at even")'''

'''salary_of_employer=int(input("Enter the salary\n"))
if (25000<=salary_of_employer<=40000):
    designation='Manager'
elif (15000<=salary_of_employer<=25000):
    designation='Accountant'
elif (10000<=salary_of_employer<=15000):
    designation='Clerk'
else:
    designation='None'
print("Your designation is:",designation)'''

'''a=int(input("How many days have been late\n"))
if a==0:
    print("You have submitted on time")
elif (1<=a<=5):
    print("The fine is $15")
elif (6<=a<=10):
    print("The fine is $50")
elif (10<=a<=30):
    print("The fine is $100")
else :
    print("Membership Canceled")'''

'''designstion=input("Enter your designastion in N,S,E or W\n").upper()
if designstion=='N':
    print("North")
elif designstion=='S':
    print("South")
elif designstion=='E':
    print("East")
elif designstion=='W':
    print("West")
else:
    print("Give a correct designation")'''

'''x=int(input("Enter the number from\n"))
y=int(input("Enter the number to\n"))
if x<y:
    for i in range(x,y+1):
        print(i,end=' ')
else:
    for i in range(y,x+1 ):
        print(i,end=' ')'''

'''avg=res=1
a=int(input("Enter the n number\n"))
for i in range (a):
    res=int(input())
    avg=avg+res
rest=avg//a
print(rest)'''

'''a=int(input("Enter the number from\n"))
b=int(input("Enter the to\n"))
for i in range(a,b):
    if i%2!=0:
        print(i,end=' ')'''

a=int(input("Enter the number\n"))
for i in range(1,11):
    print(i,"*",a,"=","%+a2d"%(a*i))
        
