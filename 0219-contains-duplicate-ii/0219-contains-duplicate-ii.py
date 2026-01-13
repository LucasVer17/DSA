class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        i = 0
        for num in nums:
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i
            i += 1
        return False