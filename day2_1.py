guess=int(input("enter a number:"))
secret=int(7)
if guess==secret:
  print("You got it!")
elif guess<secret:
  print("Too low")
else:
  print("Too high")