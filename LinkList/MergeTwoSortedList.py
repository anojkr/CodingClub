# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = ListNode()
        head = curr

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                curr, list1 = curr.next, list1.next
            else:
                curr.next = list2
                curr, list2 = curr.next, list2.next

        if list1 == None:
            curr.next = list2
        else:
            curr.next = list1
        return head.next
