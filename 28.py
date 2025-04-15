class Solution(object):
    def checkingLetters(self, haystack, needle):
        for index in range(len(needle)):
            if haystack[index] == needle[index]:
                if index + 1 == len(needle):
                    return True
                else:
                    continue
            else:
                return False
            
    
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for index, letter in enumerate(haystack):
            if letter == needle[0] and len(haystack[index:]) >= len(needle):
                # trigger search through remaining letters
                if self.checkingLetters(haystack[index:], needle):
                    return index
        return -1

print(Solution().strStr("sadbutsad", "sad"))