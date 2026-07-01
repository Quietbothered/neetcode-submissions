class Solution:
    def trap(self, height: List[int]) -> int:
        # first we select  a bar and then we move other bar untill
        #we discover a bar greater than last one 
        #one we get new bar left is that bar next again 
        #we move forward again untill we see the bar equal or greater than 
        #current bar once we get that calc current height and move on 
        #
        # l =0 
        # r = 1
        # area = 0
        # # area = min(height[l],height[r])*abs(l-r) -sum(height[l+1:r])

        # while l<=r<len(height):
        #     if height[l]>height[r]:
        #         r+=1
        #     elif height[l]<height[r]:
        #         area += min(height[l],height[r])*abs(l-r-1) -sum(height[l+1:r])
        #         r +=1
        #         l = r-1 
        #     else :
        #         continue
        # return area
        l =0 
        r = 1
        prefix = [0]*len(height)
        prefix[0]=height[0]
        suffix = [0]*len(height)
        suffix[-1] = height[-1]
        for i in range(0,len(height)):
            prefix[i] = max(prefix[i-1],height[i])
        for i in range(-1, -len(height)-1,-1):
            suffix[i]= max(suffix[i+1],height[i])
        area = 0
        for i in range(1,len(height)):
            area += min(prefix[i],suffix[i])-height[i]
        return area






























