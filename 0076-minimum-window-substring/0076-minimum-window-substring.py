class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        wmap, tmap = {}, {}

        for char in t:
            tmap[char] = tmap.get(char, 0) + 1

        have, need = 0, len(tmap)
        start, end = 0, 0

        min_len = float("inf")
        result = ""

        while end < len(s):
            char = s[end]

            wmap[char] = wmap.get(char, 0) + 1

            if char in tmap and wmap[char] == tmap[char]:
                have += 1

            while start <= end and have == need:
                char = s[start]

                current_window = end - start + 1
                if current_window < min_len:
                    min_len = current_window
                    result = s[start:end+1]

                wmap[char] -= 1
                if char in tmap and wmap[char] < tmap[char]:
                    have -= 1

                start += 1

            end += 1

        return result