class Solution:
    def countSquares(self, arr: List[List[int]]) -> int:
        n=len(arr)
        m=len(arr[0])
        dp=[[0 for i in range(m)]for j in range(n)]
        for i in range(n):
            dp[i][0]=arr[i][0]
        for j in range(m):
            dp[0][j]=arr[0][j]
        for i in range(1,n):
            for j in range(1,m):
                if arr[i][j]==1:
                    dp[i][j]= 1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
                else:
                    dp[i][j]=0
                    
        ans=0
        for i in range(n):
            ans+=sum(dp[i])
        return ans
