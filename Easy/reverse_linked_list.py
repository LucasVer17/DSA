"""
LeetCode Problem #206: Reverse Linked List
Difficulty: Easy

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        Iterative approach using three pointers
        """
        prev = None
        current = head
        
        while current:
            next_temp = current.next
            current.next = prev
            prev = current
            current = next_temp
        
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n) due to recursion stack
        
        Recursive approach
        """
        if not head or not head.next:
            return head
        
        new_head = self.reverseListRecursive(head.next)
        head.next.next = head
        head.next = None
        
        return new_head


# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    """Convert linked list to Python list for easy comparison"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    reversed1 = solution.reverseList(head1)
    assert linked_list_to_list(reversed1) == [5, 4, 3, 2, 1]
    print("Test case 1 passed: [1,2,3,4,5] -> [5,4,3,2,1]")
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    reversed2 = solution.reverseList(head2)
    assert linked_list_to_list(reversed2) == [2, 1]
    print("Test case 2 passed: [1,2] -> [2,1]")
    
    # Test case 3
    head3 = create_linked_list([])
    reversed3 = solution.reverseList(head3)
    assert linked_list_to_list(reversed3) == []
    print("Test case 3 passed: [] -> []")
    
    # Test recursive approach
    head4 = create_linked_list([1, 2, 3, 4, 5])
    reversed4 = solution.reverseListRecursive(head4)
    assert linked_list_to_list(reversed4) == [5, 4, 3, 2, 1]
    print("Test case 4 (recursive) passed: [1,2,3,4,5] -> [5,4,3,2,1]")
    
    print("\nAll test cases passed!")
