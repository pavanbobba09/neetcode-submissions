class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        values =  []

        for i in nums:
            if i in values:
                return True
           
            values.append(i)

        return False
        