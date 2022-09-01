mod=1000000007
def f(i,j,isTrue,s,dp):
    if i>j:
        return 0
    if i==j:
        if isTrue:
            return s[i]=="T"
        else:
            return s[i]=="F"
    if dp[i][j][isTrue]!=-1:
        return dp[i][j][isTrue]
    ways=0
    for ind in range(i+1,j,2):
        LT=f(i,ind-1,1,s,dp)
        LF=f(i,ind-1,0,s,dp)
        RT=f(ind+1,j,1,s,dp)
        RF=f(ind+1,j,0,s,dp)
        if s[ind]=="&": 
            if isTrue:
                ways=(ways+(LT*RT)%mod)%mod
            else:
                ways=(ways+(LF*RT)%mod + (LT*RF)%mod + (LF*RF)%mod) %mod
                
        elif s[ind]=="|":
            if isTrue:
                ways=(ways+(LF*RT)%mod + (LT*RF)%mod + (LT*RT)%mod) %mod
            else:
                ways=(ways+(LF*RF)%mod)%mod

        else:
            if isTrue:
                ways=(ways+(LT*RF)%mod + (LF*RT)%mod)%mod
            else:
                ways=(ways+(LT*RT)%mod + (LF*RF)%mod)%mod
        dp[i][j][isTrue]=ways
  
    return dp[i][j][isTrue]
        
 
def evaluateExp(exp):
    n=len(exp)
    dp=[[[-1 for i in range(2)]for j in range(n)]for k in range(n)]
    return f(0,n-1,1,exp,dp)
  
