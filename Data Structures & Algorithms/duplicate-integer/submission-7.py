class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        ue = set()

        for x in nums:
            if x in ue:
                return True

            else:
                ue.add(x)


        return False
        
        