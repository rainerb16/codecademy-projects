#Write your function here
def exponents(bases, powers):
  new_lst = []
  for b in range(len(bases)):
    for p in range(len(powers)):
      new_lst.append(bases[b]**powers[p])
  return new_lst

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
