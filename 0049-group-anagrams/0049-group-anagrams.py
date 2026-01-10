class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if(sorted_string in d):
                d[sorted_string].append(string)
            else:
                d[sorted_string] =  [string]
        return list(d.values())
 