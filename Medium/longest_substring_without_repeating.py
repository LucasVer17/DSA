"""
LeetCode Problem #3: Longest Substring Without Repeating Characters
Difficulty: Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time Complexity: O(n)
        Space Complexity: O(min(m, n)) where m is the size of the charset
        
        Using sliding window with hash map
        """
        char_index = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If char is in the map and its index is >= start,
            # move start to the right of the previous occurrence
            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1
            
            # Update the character's latest index
            char_index[char] = end
            
            # Update max_length
            max_length = max(max_length, end - start + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    print("Test case 1 passed: 'abcabcbb' -> 3")
    
    # Test case 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    print("Test case 2 passed: 'bbbbb' -> 1")
    
    # Test case 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    print("Test case 3 passed: 'pwwkew' -> 3")
    
    # Test case 4
    assert solution.lengthOfLongestSubstring("") == 0
    print("Test case 4 passed: '' -> 0")
    
    # Test case 5
    assert solution.lengthOfLongestSubstring(" ") == 1
    print("Test case 5 passed: ' ' -> 1")
    
    # Test case 6
    assert solution.lengthOfLongestSubstring("au") == 2
    print("Test case 6 passed: 'au' -> 2")
    
    # Test case 7
    assert solution.lengthOfLongestSubstring("dvdf") == 3
    print("Test case 7 passed: 'dvdf' -> 3")
    
    print("\nAll test cases passed!")
