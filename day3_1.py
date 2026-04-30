list=["apple","mango","orange","berry"]
print(list)
print(list[0])
print(list[-1])
list.append("cherry")
list.remove("mango")
print(list)
for index,fruit in enumerate(list):
  print(f"{index+1}.{fruit}")
  print(len(list))