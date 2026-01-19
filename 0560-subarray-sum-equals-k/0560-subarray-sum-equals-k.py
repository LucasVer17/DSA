class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = 0
        hashmap = {0:1}
        ans = 0
        for num in nums:
            currSum += num
            val = currSum - k
            if val in hashmap:
                ans += hashmap[val]
            if currSum in hashmap:
                hashmap[currSum] += 1
            else:
                hashmap[currSum] = 1

        return ans