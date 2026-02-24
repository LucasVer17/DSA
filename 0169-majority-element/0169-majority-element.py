class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        frequencia_max = 0
        resultado = nums[0]
        for i in nums:
            contagem = dic[i] = dic.get(i, 0) + 1
            if contagem > frequencia_max:
                frequencia_max = contagem
                resultado = i
        return resultado