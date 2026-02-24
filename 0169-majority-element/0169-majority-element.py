class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        total = 0
        total_return = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for k, v in dic.items():
            if v > total:
                total = v
                total_return = k
        return total_return