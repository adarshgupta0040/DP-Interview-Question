# Recursion and Memoisation :  TLE
  
class Solution:
    def f(self,i,j,A,dp):
        if i==j:  #Single matrix
            return 0
        if dp[i][j]!=-1:
            return dp[i][j]
        mini=float("inf")
        for k in range(i,j):
            steps=(A[i-1]*A[k]*A[j]) + self.f(i,k,A,dp) + self.f(k+1,j,A,dp)
            mini=min(mini,steps)
            dp[i][j]=mini
        return dp[i][j]
    def matrixMultiplication(self, N, arr):
        dp=[[-1 for i in range(N)]for j in range(N)]
        return self.f(1,N-1,arr,dp)
      
 
# Tabulation : Accepted

    def matrixMultiplication(self, n, arr):
        dp=[[0 for i in range(n)]for j in range(n)]
        for i in range(n):
            dp[i][i]=0
        for i in range(n-1,0,-1):
            for j in range(i+1,n):
                mini=float("inf")
                for k in range(i,j):
                    steps=arr[i-1]*arr[k]*arr[j] + dp[i][k] + dp[k+1][j]
                    mini=min(mini,steps)
                dp[i][j]=mini
        return dp[1][n-1]
