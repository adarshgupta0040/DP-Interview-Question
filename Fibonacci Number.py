# Recursive :

class Solution:
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n==0:
            return 0
        return self.fib(n-1)+self.fib(n-2)
      
# Memoisation:

class Solution:
    def f(self,n,dp):
        if n==1:
            return 1
        if n==0:
            return 0
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.f(n-1,dp)+self.f(n-2,dp)
        return dp[n]
    def fib(self, n: int) -> int:
        dp=[-1]*(n+1)
        return self.f(n,dp)
 
# Tabulation :

class Solution:
    def fib(self, n: int) -> int:
            if n==0:
                return 0
            dp=[0]*(n+1)
            dp[0]=0
            dp[1]=1
            for i in range(2,n+1):
                dp[i]=dp[i-1]+dp[i-2]
            return dp[n]

# Space Optimisation :

def fibonacciNumber(n):
        if n==0:
            return 0
        if n==1:
            return 1
        prev2=0
        prev1=1
        for i in range(2,n+1):
            curr=prev1+prev2
            prev2=prev1
            prev1=curr
        return prev1%(10**9+7)
          
          
        
