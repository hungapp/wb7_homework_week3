class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for i, char in enumerate(t):
            if char == s[0]:
                s = s[1:]
            if len(s) == 0:
                return True
        if s:
            return False
        return True
                
                
