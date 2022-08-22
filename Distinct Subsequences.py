# Recursion --> Memoisation

class Solution:
    def f(self,i,j,s,t,dp):
        if j==0:
            return 1
        if i==0:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        if s[i-1]==t[j-1]:
            dp[i][j]= self.f(i-1,j-1,s,t,dp)+self.f(i-1,j,s,t,dp)
        else:
            dp[i][j]= self.f(i-1,j,s,t,dp)
        return dp[i][j]
	
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.f(m,n,s,t,dp)
	
	
#Tabulation DP :

    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[ 0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            dp[i][0]=1
        for j in range(1,n+1):
            dp[0][j]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]= dp[i-1][j-1]+dp[i-1][j]
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[m][n]

# Space Optimisation :

    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        # dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        # return self.f(m,n,s,t,dp)
        prev=[0]*(n+1)
        prev[0]=1
        for i in range(1,m+1):
            curr=[0]*(n+1)
            curr[0]=1
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    curr[j]= prev[j-1]+prev[j]
                else:
                    curr[j]= prev[j]
            prev=curr
        return prev[n]
	
# Single Array 

    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        prev=[0]*(n+1)
        prev[0]=1
        for i in range(1,m+1):
            for j in range(n,0,-1):
                if s[i-1]==t[j-1]:
                    prev[j]= prev[j-1]+prev[j]
        return prev[n]
