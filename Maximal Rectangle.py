class Solution:
    def largestRectangleArea(self, h):
        stack=[]
        n=len(h)
        left=[0]*n
        right=[0]*n
        for i in range(n):
            if len(stack)==0:
                left[i]=0
            else:
                while(len(stack)!=0 and h[stack[-1]]>=h[i]):
                    stack.pop()
                if len(stack)==0:
                    left[i]=0
                else:
                    left[i]=stack[-1]+1
            stack.append(i)
        while(stack):
            stack.pop()
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                right[i]=n-1
            else:
                while(len(stack)!=0 and h[stack[-1]]>=h[i]):
                    stack.pop()
                if len(stack)==0:
                    right[i]=n-1
                else:
                    right[i]=stack[-1]-1
            stack.append(i)
        area=0
        for i in range(n):
            area=max(area,h[i]*(right[i]-left[i]+1))
        return area
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m,n=len(matrix),len(matrix[0])
        maxarea=0
        height=[0]*n
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]=="1":
                    height[j]+=1
                else:
                    height[j]=0
            print(height)
            area=self.largestRectangleArea(height)
            maxarea=max(maxarea,area)
        return maxarea
