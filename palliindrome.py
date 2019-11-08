a=input("Enter the first string: ")
b=input("Enter the second string: ")
c=input("Enter the third string: ")

d=a[::-1]
e=b[::-1]
f=c[::-1]

if(d==a):
    print("First string is a pallindrome")
else:
    print("First string is not a pallindrome")


if(e==b):
    print("Second string is a pallindrome")
else:
    print("Second string is not a pallindrome")

if(f==c):
    print("Third string is a pallindrome")
else:
    print("Third string is not a pallindrome")
