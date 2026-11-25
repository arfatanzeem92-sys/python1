#tuple is a securable data type

"""a = {"a":10,"a":20}
print(a)
a["c"] = 15
print(a)"""

#dictionary accessing
"""a = {"a":[10,20,30],"b":[40,50,60]}
print(a['a'][1])"""

#string slicing using positive numbers
"""a = "hello"""
"""print(a[0:3]) #from left ti right
print(a[0:4])"""

#string slicing using negative numbers
"""print(a[-3:-2+1])""" #from right to left
"""a = "good morning" 
print(a[7:11])
print(a[-2:-6])"""

"""a = "hello"
print(a[1:2-1]) #start:end+1:jump
print(a[::-1])""" #reversing the entire string

"""a = "good morning"""
"""print(a[1:5+1:1])
print(a[5::3])
print(a[-7::3])"""
"""print(a[-2:-8-1:-3])
print(a[10:4-1:3])"""

"""a="happy birthday" 
print(a[-4:-7-1])"""

"""a = input("enter")
print(a)"""
"""b=int(input("enter: "))
print(b)"""

"""c=eval(input("enter: "))
print(c)"""

#t0 check if a number is even
"""a=int(input("enter: "))
if a%2==0:
    print("number is even")
else:
    print("number is odd")"""

#to check the length if a list
"""a=[1,3,5,8,5]
if len(a)==5:
    print("list length is 5")
else:
    print("list length is not 5")"""

#to convert a number to character
"""print(chr(10))"""

#to find the ascii value of a charachter
"""print(ord('a'))
print(ord('7'))"""

#to check if a charater is upper or lowercase
"""ch=input("enter a character: ")
if ch==ch.upper():
    print("uppercase")
elif ch==ch.lower():
    print("lower")
else:
    print("neither")"""

#or
"""ch=input("enter a character: ")
if 'A'<=ch<='Z':
    print("uppercase")
elif 'a'<=ch<='z':
    print("lower")
else:
    print("neither")"""

#to access insta id
"""un=input("enter username: ")
if un=="___arfa.______":
    print("username corret")
    pw=input("enter password: ")
    if pw=="rasam":
        print("password is correct")
    else:
        print("incorrect password")
else:
    print("incorrect username")"""

#or
"""username="___arfa.______"
password="rasam"
un=input("enter username: ")
if un=="___arfa.______":
    print("username corret")
    pw=input("enter password: ")
    if pw=="rasam":
        print("password is correct")
    else:
            print("incorrect password")
else:
    print("incorrect username")"""

#while loop
#printing numbers from 1 to 10
"""i=1
while i<=10:
    print(i)
    i=i+1"""

#to check if a number is even or not
"""i=1
while i<10:
    if i%2==0:
        print(i)
    i=i+1"""

#to print even numbers from 1 to 100
"""i=1
while i<=100:
    if i%2==0:
        print(i)
    i=i+1"""

#to print odd numbers from 1 to 100
"""i=1
while i<=100:
    if i%2!=0:
        print(i)
    i=i+1"""

#reversing a number usuing while loop
"""n=int(input("enter a number: "))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("reversed number is: ", rev)"""

#for loop
#to print numbers from 1 to 10
"""for i in range(1,11):
    print(i)"""

#to print even numbers from 1 to 100
"""for i in range(1,101):
    if i%2==0:
        print(i)"""

#to print odd numbers from 1 to 100
"""for i in range(1,101):
    if i%2!=0:
        print(i)"""

#to check character is uppercase or lowercase using for loop
"""ch=input("enter a character: ")
for i in ch:
    if 'A'<=i<='Z':
        print("uppercase")
    elif 'a'<=i<='z':
        print("lower")
    else:
        print("neither")"""

#reversing a number using for loop n without using string slicing
"""num=int(input("enter a number: "))
rev=''
for i in num:
    rev=i+rev
print("reversed number is: ", rev)"""

#using nested for loop 
#to print 5*5 matrix of *
"""for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()"""

#to print 5*5 matrix of * in diagonal form
"""for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()"""

#function
#with arguments and with return type
"""def convert(a):
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return (out) 
print(convert(input("enter a string: ")))"""
#a return functionreturns the output address. not the actual output

#with arguments n without return 
"""def convert(a):
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
print(convert(input("enter a string: "))"""
#prints the actual output 

#without arguments n with return type
"""def convert():
    a=input("enter a string: ")
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert())"""

#without arguments n without return type
"""def convert():
    a=input("enter a string: ")
    out=""
    for i in a:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert()"""

#classes and objects
#to create a class
"""class college:
    cname="gpln"
    cloc="hoodi"
college.cloc="krpuram"
s1=college()
print(s1.cname,s1.cloc)"""
#changes made in the class will be reflected in the object
"""s1.cloc="madavara"
print(college.cname,college.cloc)"""
#changes made in the object will not be reflected in the class

"""class college:
    cname="gpln"
    cloc="hoodi"
s1=college()
s1.sname="kushi"
s1.sphone="1234567890"

s2=college()
s2.sname="arfa"
s2.sphone="0987654321"

print(s1.cloc)
s1.cloc="krpuram"
print("after changing")
print(s1.cloc)

print(s2.cloc)
print(college.cloc)"""

#init constructor
"""class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
s1=college("arfa",1234567890,"1GD25CS067")
s2=college("kushi",9876543210,"1GD25CS065")
print(s1.name,s1.phone,s1.usn)
print(s2.name,s2.phone,s2.usn)"""

#or
"""class college:
    def __init__(self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
s1=college("arfa",1234567890,"1GD25CS067")
s2=college("kushi",9876543210,"1GD25CS065")
s1.display()
s2.display()"""


