#Write your function here
def max_num(nums):
  max = nums[0]
  for x in range(len(nums)):
    if nums[x] > max:
      max = nums[x]
  return max
#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
