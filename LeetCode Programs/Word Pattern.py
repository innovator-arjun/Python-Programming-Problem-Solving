#https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        # pattern = "abba"
        # str = "dog dog dog dog"

        seen={}
        li_words=list(str.split(' '))
        li_pattern=list(pattern)
        if len(li_words)!=len(li_pattern):
            return False
        for i in range(0,len(li_pattern)):
            # print(seen)
            try:
                if li_pattern[i] not in seen.keys() and li_words[i] not in seen.values():
                    seen[li_pattern[i]]=li_words[i]
                elif seen[li_pattern[i]]!=li_words[i]:
                    # print(seen)
                    return False

            except:
                return False
        # print(seen)
        return True