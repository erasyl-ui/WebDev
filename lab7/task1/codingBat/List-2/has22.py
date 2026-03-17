def has22(nums):
  for i, elem in enumerate(nums):
    if (len(nums) > (i+1)):
      if (elem == 2) and (nums[i+1] == 2):
        return True
        
  return False
