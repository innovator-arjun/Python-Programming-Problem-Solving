

#https://leetcode.com/problems/n-repeated-element-in-size-2n-array/submissions/

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        coll = collections.Counter(A)

        for i, val in coll.items():
            if val > 1:
                return i