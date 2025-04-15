class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 1 and digits[0] == 9:
            return [1,0]

        elif digits[-1] != 9:
            digits[-1]+=1
            return digits

        else:
            digits[-1] = 0
            digits[:-1] = self.plusOne(digits[:-1])
            return digits



print(Solution().plusOne([1,2,3,4,9,9,9,9,9,9,9]))