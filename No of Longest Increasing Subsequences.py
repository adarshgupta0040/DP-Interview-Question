
def findNumberOfLIS(arr: List[int]) -> int:
    n=len(arr)
    dp=[1]*n
    count=[1]*n
    maxi=0
    for i in range(n):
        for prev in range(0,i):
            if arr[i]>arr[prev] and dp[i] < 1+dp[prev]:
                dp[i]=1+dp[prev]  #Inherit
                count[i] = count[prev]
            elif arr[i]>arr[prev] and dp[i]==1+dp[prev]:
                count[i] += count[prev]
            maxi=max(maxi,dp[i])
#     print(maxi)
#     print(dp)
#     print(count)
    nos=0
    for i in range(n):
        if dp[i] == maxi:
            nos+=count[i]
    return nos
