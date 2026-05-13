class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        maxLenght = 0

        uniqueElements= set(nums)

        for nums in uniqueElements:
            if (nums-1) not in uniqueElements:
                cuurentEle = nums
                maxl = 1

                while (cuurentEle+1) in uniqueElements:
                    cuurentEle +=1
                    maxl+=1

                maxLenght = max(maxl,maxLenght)

        return maxLenght