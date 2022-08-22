class Solution:
    def f(self,n,arr,target):
        dp=[[0 for i in range(target+1)] for j in range(n)]
        if arr[0]==0:
            dp[0][0]=2
        else:
            dp[0][0]=1
        if arr[0]!=0 and arr[0]<=target:
            dp[0][arr[0]]=1
        for ind in range(1,n):
            for sum in range(0,target+1):
                Nottake=dp[ind-1][sum]
                take=0
                if arr[ind]<=sum:
                    take=dp[ind-1][sum-arr[ind]]
                dp[ind][sum]=(take+Nottake)%(10**9+7)
        return dp[-1][-1]
    
    def countPartitions(self,n,arr,d):  # From Formula gen from Partition with given diffrnce
        totalsum=0
        for i in arr:
            totalsum+=i
        if totalsum-d<0 or (totalsum-d)%2:
            return 0
        target=(totalsum-d)//2
        return self.f(n,arr,target)

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.countPartitions(len(nums),nums,target)
