class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        total = 0
        total_return = 0
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        return Counter(nums).most_common(1)[0][0]