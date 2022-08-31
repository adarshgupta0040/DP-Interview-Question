# Memoisation : TLE

class Solution:
    def f(self,i,j,cuts,dp):
        if i>j:
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=float("inf")
        for ind in range(i,j+1):
            cost=(cuts[j+1]-cuts[i-1]) +self.f(i,ind-1,cuts,dp) + self.f(ind+1,j,cuts,dp)
            mini=min(mini,cost)
            dp[i][j]=mini
        return dp[i][j]

        
    def minCost(self, N: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(0)
        cuts.append(N)
        cuts.sort()
        dp=[[-1 for i in range(c+1)]for j in range(c+1)]  
		return self.f(1,c,cuts,dp)
    
 
 # Tabulation : Accepted
 
 
    def minCost(self, N: int, cuts: List[int]) -> int:
        c=len(cuts)
        cuts.append(0)
        cuts.append(N)
        cuts.sort()
        dp=[[0 for i in range(c+2)]for j in range(c+2)]  
        for i in range(c,0,-1):
            for j in range(1,c+1):
                if i>j:
                    continue
                mini=float("inf")
                for ind in range(i,j+1):
                    cost=cuts[j+1]-cuts[i-1] +dp[i][ind-1] + dp[ind+1][j]
                    mini=min(mini,cost)
                dp[i][j]=mini
        return dp[1][c]
