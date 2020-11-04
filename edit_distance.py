class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cols = len(word1) + 1
        rows = len(word2) + 1
        dp = [[0] * cols for _ in range (rows)]
        
        for i in range(cols):
            dp[0][i] = i
        for i in range(rows):
            dp[i][0] = i
            
        for i in range(1, rows): #word2
            for j in range(1, cols): #word1
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
#                   insert -> word1 word2[1:], 
# del -> word1[1:] word2
# replace  
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j - 1], dp[i-1][j-1])
        return dp[-1][-1]                   
            
            
