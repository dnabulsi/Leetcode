class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = 0
        temp = -101
        for index,value in enumerate(nums):
            if value == temp:
                nums[index] = 101
            else:
                length+=1
                temp = value
        nums.sort()
        return length
        
        
        


example = Solution()
print(example.removeDuplicates([1,1,2]))