class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        index = 0
        for number in nums:
            if number < target:
                index+=1
            elif number == target:
                return index
        return index

print(Solution().searchInsert([1,3,5,6],7))
