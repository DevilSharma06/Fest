num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
if(num1>num2):
    max=num1
    min=num2
elif(num2>num1):
    max=num2
    min=num1

print("Max=",max)
print("Min=",min)
