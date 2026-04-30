lists=[25,67,12,70,33]
for list in lists:
  print(list)
  print(max(lists))
  print(min(lists))
  print(sum(lists))
  print(sum(lists)/len(lists))
  for mark in lists:
    if mark>75:
      print(mark)
  lists.sort()
  lists.reverse()
print(lists)