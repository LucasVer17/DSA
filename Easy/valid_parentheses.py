"""
LeetCode Problem #20: Valid Parentheses
Difficulty: Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Using stack to match opening and closing brackets
        """
        stack = []
        closing_to_opening = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            if char in closing_to_opening:
                # It's a closing bracket
                if not stack or stack[-1] != closing_to_opening[char]:
                    return False
                stack.pop()
            else:
                # It's an opening bracket
                stack.append(char)
        
        return len(stack) == 0


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.isValid("()") == True
    print("Test case 1 passed: '()' -> True")
    
    # Test case 2
    assert solution.isValid("()[]{}") == True
    print("Test case 2 passed: '()[]{}' -> True")
    
    # Test case 3
    assert solution.isValid("(]") == False
    print("Test case 3 passed: '(]' -> False")
    
    # Test case 4
    assert solution.isValid("([)]") == False
    print("Test case 4 passed: '([)]' -> False")
    
    # Test case 5
    assert solution.isValid("{[]}") == True
    print("Test case 5 passed: '{[]}' -> True")
    
    # Test case 6
    assert solution.isValid("") == True
    print("Test case 6 passed: '' -> True")
    
    print("\nAll test cases passed!")
