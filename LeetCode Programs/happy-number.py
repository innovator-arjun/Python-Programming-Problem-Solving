#https://leetcode.com/problems/happy-number/submissions/

class Solution:
    def isHappy(self, n):

        seen = set()
        while n not in seen:
            seen.add(n)
            res = list(map(int, str(n)))
            n = sum([i * i for i in res])

            if n == 1:
                return True
        return False