'''type conversion
Converting of one Dt into another Dt'''
x=5
z=2.5
y=x+z
print(y)
'''expilcite conversion'''
x=5.25
print(x)
print(int(x))

'''x=int(input("Enter the no.of days\n"))
z=x//365
c=x%365//30
d=x%365%30
print("Year=%d"%z,"month=%d"%c,"days=%d"%d)'''

'''min=int(input("Enter the no.of seconds\n"))
days=min//1440
r=min%1440
hour=r//60

print("days=%d"%days,"hours=%d"%hour)'''

'''x=int(input("Enter the number\n"))
w=(x%10*10)+(x//10)
print(w+x)  '''

'''x=int(input("Enter the 1st no"))
y=int(input("Enter the 2nd no"))
r=(x%y)
if r==0:
    print(x)
else :
        r=(x//y)+1
        res=r*y
        print(res)'''

d = input("Enter a day: ")
result = "holiday" if d == "sunday" else "no holiday"
print(result)
