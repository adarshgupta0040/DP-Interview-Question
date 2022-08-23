# Recursive 
class Solution:
    def f(self,i,j,s,t):
        if i<0:
            return j+1
        if j<0:
            return i+1
        if s[i]==t[j]:
            return 0 + self.f(i-1,j-1,s,t)
        else:
            return min((1+self.f(i-1,j,s,t)),(1+self.f(i,j-1,s,t)),(1+self.f(i-1,j-1,s,t)))
        
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        return self.f(m-1,n-1,word1,word2)

     
#Memoisation 

class Solution:
    def f(self,i,j,s,t,dp):
        if i<0:
            return j+1
        if j<0:
            return i+1
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i]==t[j]:
            dp[i][j]= 0 + self.f(i-1,j-1,s,t,dp)
        else:
            dp[i][j]= min((1+self.f(i-1,j,s,t,dp)),(1+self.f(i,j-1,s,t,dp)),(1+self.f(i-1,j-1,s,t,dp)))
        return dp[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[-1 for i in range(n)]for j in range(m)]
        return self.f(m-1,n-1,word1,word2,dp)
      
                         OR 
class Solution:
    def f(self,i,j,s,t,dp):
        if i==0:
            return j
        if j==0:
            return i
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i-1]==t[j-1]:
            dp[i][j]= 0 + self.f(i-1,j-1,s,t,dp)
        else:
            dp[i][j]= min((1+self.f(i-1,j,s,t,dp)),(1+self.f(i,j-1,s,t,dp)),(1+self.f(i-1,j-1,s,t,dp)))
        return dp[i][j]
        
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.f(m,n,word1,word2,dp)
      
      
# Tabulation :

    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        
        for j in range(n+1):
            dp[0][j]=j
        for i in range(m+1):
            dp[i][0]=i
        
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]= 0 + dp[i-1][j-1]
                else:
                    dp[i][j]= 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[m][n]
