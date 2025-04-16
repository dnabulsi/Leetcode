# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # three scenarios:
        # 1. curr node is first node => prev is None, cannot be dupe
        # 2. curr node is somewhere in middle => prev and next are not None
        # 3. curr node is last node => next is None
        
        curr = head
                
        while curr:
            if curr.next is not None and curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            curr = curr.next
            
        return head
    
nums = [1, 1, 2, 3, 3]
head = None
next = None
for index, num in enumerate(nums[::-1]):
    obj = ListNode(num, next)
    next = obj
    if index == len(nums) - 1:
        head = obj

soln = Solution().deleteDuplicates(head)

while head:
    print(f"val: {head.val}")
    head = head.next