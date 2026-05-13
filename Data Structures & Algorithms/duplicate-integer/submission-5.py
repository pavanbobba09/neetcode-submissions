class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqueElements = set()

        for x in nums:
            if x in uniqueElements:
                return True
            else:
                uniqueElements.add(x)
            
        

        return False
        