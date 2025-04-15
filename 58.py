class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = []
        for element in s[::-1]:
            if element == ' ':
                continue
            while element != ' ':
                    word.append(element)

        return word[::-1]



print(Solution().lengthOfLastWord("    hello    dana     "))