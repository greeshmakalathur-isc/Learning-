def add(a,b):
  return a+b
def subtract(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b==0:
    return "cant be divided by zero"
  return a/b
oper=int(input("Enter 1.add 2.subtract 3.multiply 4.divide"))
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
if oper==1:
  print(add(num1,num2))
elif oper==2:
  print(subtract(num1,num2))
elif oper==3:
  print(multiply(num1,num2))
elif oper==4:
  print(divide(num1,num2))
 
