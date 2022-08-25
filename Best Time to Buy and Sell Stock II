# Memoisation :

class Solution:
    def f(self,ind,buy,n,price,dp):
        if ind==n:
            return 0
        if dp[ind][buy]!=-1:
            return dp[ind][buy]
        
        if (buy):
            dp[ind][buy]=max(-price[ind]+self.f(ind+1,0,n,price,dp),0+self.f(ind+1,1,n,price,dp))
        else:
            dp[ind][buy]=max(price[ind]+self.f(ind+1,1,n,price,dp),0+self.f(ind+1,0,n,price,dp))
        return dp[ind][buy]
    
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for i in range(2)]for j in range(n)]
        return self.f(0,1,n,prices,dp)


#Tabulation :

    def maxProfit(self, price: List[int]) -> int:
        n=len(price)
        dp=[[-1 for i in range(2)]for j in range(n+1)]
        dp[n][0]=0
        dp[n][1]=0
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if (buy):
                    dp[ind][buy]=max(-price[ind]+dp[ind+1][0] , 0+dp[ind+1][1])
                else:
                    dp[ind][buy]=max(price[ind]+dp[ind+1][1],0+dp[ind+1][0])
        return dp[0][1]
        
# Space Optimisation :

    def maxProfit(self, price: List[int]) -> int:
        n=len(price)
        ahead=[0]*2
        curr=[0]*2
        
        ahead[0]=ahead[1]=0
            
        for ind in range(n-1,-1,-1):
            for buy in range(2):
                if (buy):
                    curr[buy]=max(-price[ind]+ahead[0] , 0+ahead[1])
                else:
                    curr[buy]=max(price[ind]+ahead[1],0+ahead[0])
                ahead=curr
        return ahead[1]
