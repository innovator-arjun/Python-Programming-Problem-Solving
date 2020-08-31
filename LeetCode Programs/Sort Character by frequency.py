
#https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        li=list(s)
        li_count=Counter(li)
        final=li_count.most_common()
        res=''
        # print(type(final))
        for i,v in final:
            res=res+i*v
            # print(i,v)
            # print(res)
        return res