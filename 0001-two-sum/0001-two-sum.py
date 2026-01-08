class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(nums)):
            faltando = target - nums[i]

            if faltando in hash_map:
                return [hash_map[faltando], i]
            
            hash_map[nums[i]] = i

        
        