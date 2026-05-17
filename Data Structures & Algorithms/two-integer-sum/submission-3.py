class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        hashmap = {}

        for index, value in enumerate(nums):
            remainingValue = target - value

            if remainingValue in hashmap:
                return [hashmap[remainingValue], index]

            
            hashmap[value] = index

        return [0,0]