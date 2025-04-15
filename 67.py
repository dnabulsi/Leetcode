class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        a = list(a)
        b = list(b)
        carry = 0
        sum = ''
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            sum = str(carry%2) + sum
            carry //= 2
        return sum
        
    
print(Solution().addBinary('1011111','10'))