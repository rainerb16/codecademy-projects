#Write your function here
def reversed_list(lst1, lst2):
  rvsd_lst2 = []
  x = len(lst2)-1
  while x >= 0:
    rvsd_lst2.append(lst2[x])
    x -= 1
  if lst1 == rvsd_lst2:
    return True
  else:
    return False
#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

