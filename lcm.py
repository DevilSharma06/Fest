a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
if a>b:
      for index in range(a,a*b+1):
           if(index%a==0 and index%b==0):
                print("LCM is",index)
                break
else:
      for index in range(b,a*b+1):
           if(index%a==0 and index%b==0):
                print("LCM is",index)
                break
