def get_average(marks):
  return sum(marks)/len(marks)
def get_highest(marks):
  return max(marks)
def get_lowest(marks):
  return min(marks)
def get_grade(average):
   if average>=80:
     return "A"
   elif average >=60:
     return "B"
   else:
    return "c"
   
def print_report(name,marks):
  avg=get_average(marks)
  print(f"Name:{name}")
  print(f"Highest: {get_highest(marks)}")
  print(f"Lowest: {get_lowest(marks)}")
  print(f"Average: {avg}")
  print(f"Grade: {get_grade(avg)}")

print_report("Greeshma", [80, 90, 75, 88, 92])