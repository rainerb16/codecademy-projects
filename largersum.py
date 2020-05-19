#Write your function here
def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for x in range(len(lst1)):
    sum_lst1 += lst1[x]
  for x in range(len(lst2)):
    sum_lst2 += lst2[x]
  if sum_lst2 > sum_lst1:
    return lst2
  else:
    return lst1

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
