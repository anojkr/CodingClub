# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        stack=[]
        currNode = head
        currNodePtr = head
        while currNode!=None:
            stack.append(currNode.val)
            currNode =  currNode.next
        while currNodePtr!=None:
            if currNodePtr.val == stack[-1]:
                stack.pop()
            currNodePtr =  currNodePtr.next
        if len(stack) == 0:
            return True
        else:
            return False