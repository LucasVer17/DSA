class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        soma_window = sum(nums[:k])
        max_sum = soma_window
        for i in range(k, len(nums)):
             soma_window += nums[i]
             soma_window -= nums[i - k]
             max_sum = max(max_sum, soma_window)
        return max_sum / k