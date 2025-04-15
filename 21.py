# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # initialize both temp and dummy to be ListNode class
        temp = dummy = ListNode()
        # while list1 and list2 both have values in them
        while list1 and list2:
            # if the value of the head of list1 is less than the value of the head of list2
            if list1.val < list2.val:
                # change value of temp.next from None to list1
                temp.next = list1
                # change value of list1 to be the next element in the list
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            # change value of temp to reflect temp.next's value, we don't need temp.next anymore can consider it None
            temp = temp.next
        # after exiting the while loop, either list1 or list2 is now empty, so point towards the list with elements remaining in it
        temp.next = list1 or list2
        # since dummy equals temp, dummy returns whatever temp returns
        return dummy.next


list1 = [1,2,4]
list2 = [1,3,4]
example = Solution()
example.mergeTwoLists(list1,list2)