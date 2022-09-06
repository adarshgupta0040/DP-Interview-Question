# Memoisation :

class Solution:
    def f(self,index,arr,dp):
        if index==0:
            return arr[index]
        if index<0:
            return 0
        if dp[index]!=-1:
            return dp[index]
        pick=arr[index] + self.f(index-2,arr,dp)
        notpick= 0 + self.f(index-1,arr,dp)
        dp[index]= max(pick,notpick)
        print(dp)
        return dp[index]
    
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums))
        print(dp)
        return self.f(len(nums)-1,nums,dp)
      
# Tabulation :

 def rob(self, nums: List[int]) -> int:
      n=len(nums)
        dp=[0]*(n)
        dp[0]=nums[0]
        for i in range(1,n):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            nonpick=0+dp[i-1]
            dp[i]=max(pick,nonpick)
            print(dp)
        return dp[n-1]
      
