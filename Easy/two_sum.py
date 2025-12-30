"""
LeetCode Problem #1: Two Sum
Difficulty: Easy

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Using hash map to store the complement of each number
        """
        num_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test case 1 passed: [2,7,11,15], target=9 -> [0,1]")
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    print("Test case 2 passed: [3,2,4], target=6 -> [1,2]")
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    print("Test case 3 passed: [3,3], target=6 -> [0,1]")
    
    print("\nAll test cases passed!")
