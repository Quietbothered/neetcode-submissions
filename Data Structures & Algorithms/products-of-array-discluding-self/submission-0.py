class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):  # j is now an INDEX
                if i == j:
                    continue
                product *= nums[j]
            result.append(product)
        return result