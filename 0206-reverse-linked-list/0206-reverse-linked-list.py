# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curNode = head
        nextNode =  head
        prevNode = None
        while(curNode != None):
            nextNode = nextNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
        head = prevNode
        return head