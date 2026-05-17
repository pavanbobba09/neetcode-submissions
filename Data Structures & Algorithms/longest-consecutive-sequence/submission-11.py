class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        maxLength = 0

        elements = set(nums)

        for x in elements:
            if x-1 not in elements:
                currentElements = x
                maxL = 1

                while (currentElements+1) in elements:
                    currentElements+=1
                    maxL+=1
                
                maxLength = max(maxL,maxLength )


        return maxLength

        