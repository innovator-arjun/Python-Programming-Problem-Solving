#https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/submissions/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li=sentence.split(' ')
        for i in range(0,len(li)):
            if li[i].startswith(searchWord):
                return i+1
        return -1
        #print("burger".find('burg'))