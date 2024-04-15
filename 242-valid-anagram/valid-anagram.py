from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        counterS = Counter(s)
        counterT = Counter(t)

        for char in s:
            if counterS[char] != counterT[char]:
                return False

        return True 