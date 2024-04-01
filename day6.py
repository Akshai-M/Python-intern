
forgot_password=input("Forgot password(y/n)\n")
if forgot_password=='y':
        new_password=input("Enter the new password\n")
        conform_password=input("Conform the password\n")
        while(new_password!=conform_password):
            print(" New password and conform password doesn't match Re-enter password")
            new_password=input("Enter the new password\n")
            conform_password=input("Conform the password\n")
        print("Password updated sucessfull")
else:
#     print("Thanks for banking with us")
# PIN="1234"
# Card_number="1234 5678 9876 5432"
# C_number="123456" 
''''

    
card_number=(input("Enter the user name\n"))
pin=(input("Enter the pin \n"))
if (card_number==Card_number or card_number==C_number) and pin==PIN:
    print("Transaction sucessful")
    
while (card_number!=Card_number or card_number!=C_number):
    print("Give a valid user name")
    card_number=(input("Enter the user name\n"))
    pin=(input("Enter the pin \n"))
    if (new_password!=conform_password):
        a()'''

#multiline string
'''print(r"Hello\n""world")
print("""Hello world""")'''
#print('''Hello world''')
'''msg="Python"
print(msg[0])    
print(msg[1])    
print(msg[1+3])'''

'''m="Pyhton pgramming"'''
'''print(m)
print(m[1:18])
print(m[18:0:-1])
print(m[::-1])
print(m[:6])
print(m[-3:-1])'''
    
'''print(m[2:200])
print(m[200])'''

'''m1="python"
m2="programing"
m=m1+m2
print(m1,m2)'''

#string repetition
'''str='Hai'
print(str*3)'''

#string methods
'''lang='python'
print(lang.isalpha())'''

'''s="Welcome to python programming"
print(s.find("python"))#it starts from zero
print(s.find("python",0,10))#not found -1 is going to print by default
print(s.replace("p","P"))'''

'''s="     welcome     to python programming"
print(s)
print(s.lstrip())'''

'''s="Welcome to Python programming"
print(s.split())

print(s)
print("-".join(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())'''

'''s=65
print(chr(s))
print(ord(' '))'''

'''name=input("Enter your name:")
for i in range(len(str(name))):
    print(ord(name[i]))
    
    print(chr(name[i]))'''
#aka->ak$
'''st=input("Enter the string")
s=st[0]
for i in st:
    r=st.replace(st[0],"$")
print(s+r[1:])'''

'''s=input("Enter a string\n")

if len(s)>=3:
    if s.endswith('ing'):
        print(s+'ly')
    else:
         print(s+'ing')
else:
    print(s)'''
# s=input("Enter a string")

# print(len(s))
print(dir(dict))