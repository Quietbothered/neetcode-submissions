class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = sorted(nums)
        if len(nums)==1 or nums == []:
            return False
        else:
            for i in range (len(nums)):
                if a[i-1]==a[i] :
                    x= True
                    break 
                else:
                    x = False
                    continue
            return x
            
