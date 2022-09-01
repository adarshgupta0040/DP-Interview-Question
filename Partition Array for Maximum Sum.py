# Memoisation :

class Solution:
    def f(self,ind,arr,n,k,dp):
        if ind==n:
            return 0
        if dp[ind]!=-1:
            return dp[ind]
        maxi=float("-inf")
        length=0
        maxans=float("-inf")
        for j in range(ind,min(n,ind+k)):       #j for partition
            length+=1
            maxi=max(maxi,arr[j])
            summ=length*maxi + self.f(j+1,arr,n,k,dp)
            maxans=max(maxans,summ)
            dp[ind]=maxans
        return dp[ind]
    
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[-1 for i in range(n)]
        return self.f(0,arr,n,k,dp)
        
# Tabulation :

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n=len(arr)
        dp=[0]*(n+1)
        dp[n]=0
        for ind in range(n-1,-1,-1):
            maxi=float("-inf")
            length=0
            maxans=float("-inf")
            for j in range(ind,min(n,ind+k)):       #j for partition
                length+=1
                maxi=max(maxi,arr[j])
                summ=length*maxi + dp[j+1]
                maxans=max(maxans,summ)
            dp[ind]=maxans
        return dp[0]
        
