class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        result_arr = []
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        for num in nums2:
            if num in d:
                if d[num] > 0:
                    result_arr.append(num)
                    d[num] -= 1
        return result_arr