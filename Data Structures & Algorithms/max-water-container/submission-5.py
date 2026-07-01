class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l ---- right me jayega 
        # or r ---- left me jayega 
        l = 0
        r = len(heights)-1
        ans = 0
        while l<r:
            mul  = min(heights[l],heights[r])*(abs(l-r))
            ans = max(mul,ans)
            if (heights[l]<heights[r]):
                l+=1
            else:
                r-=1
        return ans