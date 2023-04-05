def twoSum(nums, target):
    seen = {}
    for index,value in enumerate(nums):
        remaining = target-value
        if remaining in seen:
            return[index,seen[remaining]]
        else:
            seen[value] = index

print(twoSum([3,3],6))