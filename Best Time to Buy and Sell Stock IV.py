# Recursive :

class Solution:
    def f(self,ind,transNo,n,k,price):
        if ind==n or transNo==2*k:
            return 0

        if transNo%2==0:    #buy
            profit=max(-price[ind] + self.f(ind+1,transNo+1,n,k,price),
                            0      + self.f(ind+1,transNo,n,k,price))
        else:
            profit=max(price[ind] + self.f(ind+1,transNo+1,n,k,price),
                            0     + self.f(ind+1,transNo,n,k,price))

        return profit
            
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        return self.f(0,0,n,k,prices)
      
      
#Memoisation :

class Solution:
    def f(self,ind,transNo,n,k,price,dp):
        if ind==n or transNo==2*k:
            return 0
        if dp[ind][transNo]!=-1:
            return dp[ind][transNo]
        if transNo%2==0:    #buy
            profit=max(-price[ind] + self.f(ind+1,transNo+1,n,k,price,dp),
                            0      + self.f(ind+1,transNo,n,k,price,dp))
        else:
            profit=max(price[ind] + self.f(ind+1,transNo+1,n,k,price,dp),
                            0     + self.f(ind+1,transNo,n,k,price,dp))
        dp[ind][transNo]= profit
        return dp[ind][transNo]
            
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)
        dp=[[-1 for i in range(2*k)]for j in range(n)]
        return self.f(0,0,n,k,prices,dp)
      
      
# Tabulation :

def maxProfit(self, k: int, prices: List[int]) -> int:
    n=len(prices)
    dp=[[0 for i in range(2*k+1)]for j in range(n+1)]
    
    for ind in range(n-1,-1,-1):
        for transNo in range(2*k-1,-1,-1):
            if transNo%2==0:    # buy
                profit=max(-prices[ind] + dp[ind+1][transNo+1],
                        0      + dp[ind+1][transNo])
            else:
                profit=max(prices[ind] + dp[ind+1][transNo+1],
                        0      + dp[ind+1][transNo])
            dp[ind][transNo]=profit
            
    return dp[0][0]

# Space Optimistion :

    def maxProfit(self, k: int, prices: List[int]) -> int:
        n=len(prices)

        after=[0]*(2*k+1)
        curr=[0]*(2*k+1)
        
        for ind in range(n-1,-1,-1):
            for transNo in range(2*k-1,-1,-1):
                if transNo%2==0:    # buy
                    profit=max(-prices[ind] + after[transNo+1],
                                     0      + after[transNo])
                else:
                    profit=max(prices[ind] + after[transNo+1],
                                    0      + after[transNo])
                curr[transNo]=profit
            after=curr
                
        return after[0]
