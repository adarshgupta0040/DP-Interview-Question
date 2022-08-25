# Recursive- Memoisation : TLE

class Solution:
    def f(self,ind,buy,cap,n,price,dp):
        if ind==n:
            return 0
        if cap==0:
            return 0
        if dp[ind][buy][cap]!=-1:
            return dp[ind][buy][cap]
        if buy:
            profit=max(-price[ind]+self.f(ind+1,0,cap,n,price,dp),0+self.f(ind+1,1,cap,n,price,dp))
        else:
            profit=max(price[ind]+self.f(ind+1,1,cap-1,n,price,dp),0+self.f(ind+1,0,cap,n,price,dp))
        dp[ind][buy][cap]=profit
        return dp[ind][buy][cap]
    
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[[-1 for i in range(3)]for j in range(2)]for k in range(n)]
        return self.f(0,1,2,n,prices,dp)
      
      
      
# Tabulation :
def maxProfit(prices, n):
    dp=[[[0 for i in range(3)]for j in range(2)]for k in range(n+1)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,3):
                if buy==1:
                    dp[ind][buy][cap]=max(-prices[ind]+dp[ind+1][0][cap],0+dp[ind+1][1][cap])
                else:
                    dp[ind][buy][cap]=max(prices[ind]+dp[ind+1][1][cap-1],0+dp[ind+1][0][cap])
    return dp[0][1][2]
  
  
  
#Tabulation : Space Optimisation O(Nx2x3) Accepted

    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        after=[[0 for i in range(3)]for j in range(2)]
        curr=[[0 for i in range(3)]for j in range(2)]
        for buy in range(2):          #Base case 1
            for cap in range(3):
                curr[buy][cap]=0
        for ind in range(n):          #Base case 2
            for buy in range(2):
                curr[buy][0]=0

        for ind in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3):
                    if buy==1:
                        curr[buy][cap]=max(-prices[ind]+after[0][cap],0+after[1][cap])
                    else:
                        curr[buy][cap]=max(prices[ind]+after[1][cap-1],0+after[0][cap])
            after=curr
        return after[1][2]
      
      
