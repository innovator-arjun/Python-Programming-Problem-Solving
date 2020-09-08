#https://leetcode.com/problems/fair-candy-swap/submissions/

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:

        diff =int((sum(A ) -sum(B) ) /2)
        set_A =set(A)
        set_B =set(B)
        for i in B:
            if i+ diff in A:
                return [i + diff, i]
