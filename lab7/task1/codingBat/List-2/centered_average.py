def centered_average(nums):

  sorted_nums = sorted(nums)
  arr_length = len(nums)

  return (sum(sorted_nums[1:arr_length-1]) / (arr_length - 2))
