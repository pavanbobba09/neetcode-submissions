class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        elements = set()

        for x in nums:
            if x in elements:
                return True
            
            elements.add(x)
            

        return False
        