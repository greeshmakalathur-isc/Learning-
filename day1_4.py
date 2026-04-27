num1=int(input("Enter First number : "))
num2=int(input("Enter Second number : "))
sum=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
print(f"The sum is {sum}")
print(f"The difference is {sub}")
print(f"The multiplication is {mul}")
print(f"The division is {div}")
if num2>0 and num2<0:
  print(f"The sum is {sum}")
  print(f"The difference is {sub}")
  print(f"The multiplication is {mul}")
  print(f"The division is {div}")
else:
 print("cannot divide by zero")

