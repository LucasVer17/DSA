class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        arr = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            d[num] = d.get(num, 0) + 1

        for value, freq in d.items():
            arr[freq].append(value)
        
        result = []
        for i in reversed(range(len(arr))):
            if arr[i]:
                for v in arr[i]:
                    if len(result) < k:
                        result.append(v)
                    if len(result) == k:
                        return result

