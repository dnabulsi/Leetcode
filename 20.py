class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        my_dict = {'[':']','(':')','{':'}'}
        need = []

        for symbol in s:
            # if the symbol is an opening symbol
            if symbol in my_dict.keys():
                # append its closing symbol to need
                need.append(my_dict[symbol])
            # if the symbol is a closing symbol
            elif symbol in my_dict.values():
                # if need is empty or the symbol does not match with .pop return false
                if len(need) == 0 or symbol != need.pop():
                    return False
            # any other cases return false
            else:
                return False
        # if need is empty return true
        return not need
        

example = Solution()
print(example.isValid("[]{}()"))