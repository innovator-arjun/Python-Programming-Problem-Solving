#https://leetcode.com/problems/uncommon-words-from-two-sentences/submissions/
from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        combine = A +"  " +B
        val =combine.split(' ')
        count_val =Counter(val)
        res =[]
        for i ,val in count_val.items():
            if val==1:
                res.append(i)

        return res