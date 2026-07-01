class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        set1 = [i for i in numbers]
        for i in range(len(numbers)):
            if (target - numbers[i]) in set1:
                C = [i+1,numbers.index(target-numbers[i])+1]
        return sorted(C)

