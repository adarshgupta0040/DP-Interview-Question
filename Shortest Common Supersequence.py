class Solution:
    def LCS(self,s,t):
        m=len(s)
        n=len(t)
        dp=[[0 for i in range(n+1)]for j in range(m+1)]
        for i in range(m+1):
            dp[i][0]=0
        for j in range(n+1):
            dp[0][j]=0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp
    
    def shortestCommonSupersequence(self, s: str, t: str) -> str:
        dp=self.LCS(s,t)
        m=len(dp)-1
        n=len(dp[0])-1
        ans=""
        i=m
        j=n
        while(i>0 and j>0):
            if s[i-1]==t[j-1]:
                ans+=s[i-1]
                i-=1
                j-=1
            elif dp[i-1][j]>dp[i][j-1]:
                ans+=s[i-1]
                i-=1
            else:
                ans+=t[j-1]
                j-=1
        while(i>0):
            ans+=s[i-1]
            i-=1
        while(j>0):
            ans+=t[j-1]
            j-=1
        return ans[::-1]
