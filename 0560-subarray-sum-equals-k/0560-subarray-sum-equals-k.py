class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = {}
        prefix = 0
        result = 0
        for num in nums:
            count[prefix] = count.get(prefix, 0) + 1
            prefix += num
            need = prefix - k
            if(need in count):
                result += count[need]
        return result