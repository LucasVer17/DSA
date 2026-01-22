# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head

        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
            if slow == fast: 
                entry = head 
                while entry != slow:
                    slow = slow.next 
                    entry = entry.next 
                return slow
        
        return None