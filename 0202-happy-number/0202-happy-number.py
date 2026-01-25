class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            total = 0
            x = n

            while x > 0:
                d = x % 10
                total += d * d
                x //= 10

            if total in seen:
                return False

            seen.add(total)
            n = total

        return True