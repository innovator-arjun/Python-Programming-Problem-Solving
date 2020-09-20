#https://leetcode.com/problems/squares-of-a-sorted-array/solution/

import numpy as np
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res=[i**2 for i in A]
        res.sort()
        return res
#         arr=np.array(A)
#         return np.sort(np.power(arr,2))