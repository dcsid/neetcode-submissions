class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        j = len(nums) - 1

        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if x + y == target and i != j:
                    return [i, j]
    

        