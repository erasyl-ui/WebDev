def big_diff(nums):
  sorted_nums = sorted(nums)
  return abs(sorted_nums[-1] - sorted_nums[0])
