class Solution:
    def solve(self,nums):
        n=len(nums)
        dp=[-1]*(n)
        dp[0]=nums[0]
        neg=0
        for i in range(1,n):
            pick=nums[i]+0
            if i>1:
                pick+=dp[i-2]
            nonpick=0+dp[i-1]
            dp[i]=max(pick,nonpick)
        return dp[n-1]
    
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        temp1=nums[1:]
        temp2=nums[:-1]
        return max(self.solve(temp1),self.solve(temp2))
