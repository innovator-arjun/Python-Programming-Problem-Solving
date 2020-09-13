#https://leetcode.com/problems/first-unique-character-in-a-string/submissions/
class Solution:
    def firstUniqChar(self, s: str) -> int:

        li_count =collections.Counter(s)
        for i ,v in enumerate(s):

            if li_count[v ]==1:
                return i
        return -1
