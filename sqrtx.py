class Solution(object):
    def mySqrt(self, x):
        if x == 0:
            return x
        left = 1
        right = x
        while True:
            mid = left + (right - left)/ 2
            if x / mid < mid:
                right = mid - 1
            else:
                if mid + 1 > x / (mid + 1):
                    return int(mid)
                left = mid + 1

print(Solution().mySqrt(4))