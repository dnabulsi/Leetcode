class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        length = 0
        temp = 0
        for number in range(len(nums)):
            if nums[number] == val:
                nums[number] = 51
            else:
                length+=1
                

        nums.sort()
        
        return length

example = Solution()
print(example.removeElement([1,2,2,2,3,3,3,3,3],3))