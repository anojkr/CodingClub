# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = ListNode(-1)

        H = []
        for i, headPtr in enumerate(lists):
            if headPtr:
                H.append((headPtr.val, i))
        heapq.heapify(H)

        curr = head
        while H:
            value, index = heapq.heappop(H)
            curr.next = ListNode(value)
            curr = curr.next
            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(H, (lists[index].val, index))
        return head.next