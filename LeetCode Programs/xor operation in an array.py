#https://leetcode.com/problems/xor-operation-in-an-array/submissions/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        res=start
        for i in range(1,n):
            val=start+2*i
            res=res^val
            # print(val)
        return res

