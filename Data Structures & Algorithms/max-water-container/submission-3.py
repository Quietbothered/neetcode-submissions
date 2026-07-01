class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 1, 1
        ans = 1
        # mul  = min(l,r)*(abs(heights.index(l)-heights.index(l)))
        if len(heights) ==1 or ( 0 in heights and len(heights) == 2 ):
            ans = 0
        else:
            for l in range(len(heights)):
                for r in range(1,len(heights)):
                    mul  = min(heights[l],heights[r])*(abs(l - r))
                    if ans < mul :
                        ans = mul 
                    else :
                        continue
        return ans