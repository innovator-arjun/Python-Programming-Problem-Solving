#https://leetcode.com/problems/unique-morse-code-words/submissions/

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        pattern = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                   "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        temp = ''
        for i in words:
            for j in i:
                temp = temp + pattern[ord(j) - 97]
            res.add(temp)
            temp = ''
        return len(res)

