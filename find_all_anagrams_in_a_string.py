class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p = ''.join(sorted(list(p)))
        res = []
        for i in range(len(s) - len(p) + 1):
            substring = s[i: i+len(p)]
            substring = ''.join(sorted(list(substring)))
            if substring == p:
                res.append(i)
        return res
