class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        shortest = min(strs,key=len)

        for i,char in enumerate(shortest):
            for word in strs:
                if word[i] != char:
                    return shortest[:i]
        return shortest

example = Solution()
print(example.longestCommonPrefix())