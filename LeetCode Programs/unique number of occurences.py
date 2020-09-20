#https://leetcode.com/problems/unique-number-of-occurrences/submissions/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        col=collections.Counter(arr)
        if len(set(col.values()))==len(col.values()):
            return True
        return False