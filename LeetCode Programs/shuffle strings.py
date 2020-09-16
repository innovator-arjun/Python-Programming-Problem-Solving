#https://leetcode.com/problems/shuffle-string/submissions/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [0] * len(indices)

        for i in range(0, len(indices)):
            res[indices[i]] = s[i]
        return ''.join(res)

        # for i in range(0,len(indices)):
        #     res=res+ s[indices.index(i)]
        # return res