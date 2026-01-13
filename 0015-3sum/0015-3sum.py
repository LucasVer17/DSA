class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n - 2):
            a = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                s = a + nums[left] + nums[right]

                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.add((a, nums[left], nums[right]))
                    left += 1
                    right -= 1

        return list(res)
