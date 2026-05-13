from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        elementAlreadyPresent = defaultdict(int)

        for x in range(len(nums)):
            value = target - nums[x]

            if value in elementAlreadyPresent:
                return [elementAlreadyPresent[value], x]
            else:
                elementAlreadyPresent[nums[x]] = x

        return [0,0]
                
        