# Memoisation :

def f(i,n,s,dp):
    if i==n:
        return 0

    if dp[i]!=-1:
        return dp[i]

    minicost=float("inf")
    for j in range(i,n):
        if s[i:j+1]==s[i:j+1][::-1]:
            cost=1+f(j+1,n,s,dp)
            minicost=min(minicost,cost)
            dp[i]=minicost
    return dp[i]
    
def palindromePartitioning(s):
  n=len(s)
  # return self.f(0,n,s)-1
  dp=[-1 for i in range(n)]
  return f(0,n,s,dp)-1
    
    
    
# Tabulation : Accepted

def minCut(self, s: str) -> int:
    n=len(s)
    # return self.f(0,n,s)-1
    dp=[0 for i in range(n+1)]
    dp[n]=0
    for i in range(n-1,-1,-1):
        minicost=float("inf")
        for j in range(i,n):
            if s[i:j+1]==s[i:j+1][::-1]:
                cost=1+ dp[j+1]
                minicost=min(minicost,cost)
        dp[i]=minicost
    return dp[0]-1
