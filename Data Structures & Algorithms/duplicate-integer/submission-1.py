class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        currentValues = []

        for x in nums:
            for y in currentValues:
                if x == y:
                    return True
            currentValues.append(x)

        return False
