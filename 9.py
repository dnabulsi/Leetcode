class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        strx = str(x)
        for number in range(len(strx)//2):
            if strx[number] != strx[-1*(number+1)]:
                return(False)
        return(True)

example = Solution()
print(example.isPalindrome(12345321))