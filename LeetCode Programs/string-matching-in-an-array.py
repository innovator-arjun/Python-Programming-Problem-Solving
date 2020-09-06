#https://leetcode.com/problems/string-matching-in-an-array/submissions/

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # words=["leetcoder","leetcode","od","hamlet","am"]
        res = []
        for i in range(0, len(words)):
            for j in range(0, len(words)):
                if i != j and words[i] in words[j]:
                    res.append(words[i])
        return list(set(res))

#         arr = ' '.join(words)
#         print(arr)
#         subStr=[]
#         for i in words:
#             if arr.count(i)>=2:
#                 print(i,arr.count(i))

#                 subStr.append(i)

#         return subStr