class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for x in range(n):
            a, b = b, a + b
        return a


print(Solution().climbStairs(45))