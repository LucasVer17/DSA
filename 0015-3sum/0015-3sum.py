class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_array = sorted(nums)
        return_arr = set()
        for i in range(len(sorted_array) - 2):
            if i > 0 and sorted_array[i] == sorted_array[i-1]:
                continue
            left = i + 1
            right = len(sorted_array) - 1
            while(left < right):
                sum_num = sorted_array[i] + sorted_array[left] + sorted_array[right]
                if(sum_num < 0):
                    left += 1
                elif(sum_num > 0):
                    right -= 1
                elif(sum_num == 0):
                    return_arr.add((sorted_array[i], sorted_array[left], sorted_array[right]))
                    left += 1
                    right -= 1
                    
        return list(return_arr)
        
