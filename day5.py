'''sum=0
d=int(input("Enter the number\n"))
for i in range(d):
    day=int(input())
    sum=sum+day
print("The sum of integers is:%d"%sum)'''

'''num=int(input("Enter an intger:\n"))
sod=0
 
for i in num_str:
    dgt=int(i)
    sod=sod+dgt
print("Sum is:%d"%sod)'''

'''n=int(input())
cnt=0
for i in range(1,n+1):
    if(n%i==0)
    cnt=cnt+1
if(cnt==2)
    print("Prime")'''

'''res=rem=0
n=int(input("Enter a number\n"))
for i in range(len(str(n))):
    rem=n%10
    res=(res*10)+rem
    n=n//10
print(res,"is the reverse of:%d"%n)'''

'''res=rem=0
d=int(input("Enter a number\n"))
temp=d
for i in range(len(str(d))):
    rem=d%10
    res=(res*10)+rem
    d=d//10
if temp==res :
    print(temp,"is a palindrome")
else:
    print(temp,"is not a palindrome")'''

'''n=int(input("Enter the value of n\n"))
first,second=0,1
print("Fibonacci Series:")
for i in range(n):
    print(first,end=' ') 
    first,second=second,first+second'''

'''n=int(input("Enter the number\n"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")'''
 
'''n=int(input("Enter the number\n"))
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j,end=' ')
    print(" ")'''

'''n=int(input("Enter the number\n"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end=' ')
    print(" ")
print(" ")
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j,end=' ')
    print(" ")'''

'''n=int(input("Enter the number\n"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print(" ")'''

'''n=int(input("Enter the number\n"))
for i in range(1,n):
    for j in range(1,n):
        print(i*j,end=' ')
    print()'''

'''n=int(input("Enter the number\n"))
m=int(input("Enter the number\n"))
for i in range(1,n+1):
    for j in range(m,m-i,-1):
        print(j,end=' ')
    m+=i+1
    print()'''

'''cnt=0
for i in range(5):
    for j in range(1,i+1):
        print(cnt,end=' ')
        cnt+=1
    print()'''

cnt=0
while cnt<10:
    print(f"Current count: {cnt}")
    cnt=cnt+1
else:
    print("Loop completed normally")
    
