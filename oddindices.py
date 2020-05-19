#Write your function here
def odd_indices(lst):
  odd_lst = []
  for x in range(len(lst)):
    if x % 2 != 0:
      odd_lst.append(lst[x])
  return odd_lst

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
