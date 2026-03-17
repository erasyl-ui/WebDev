def sum13(nums):
  if not nums:
  
    return 0
    
  else:
    running_sum, idx = 0, 0
    
    while (idx < len(nums)):
      if (nums[idx] == 13):
        
        idx += 2
        
      else:

        running_sum += nums[idx]
        idx += 1
        
    return running_sum
        
