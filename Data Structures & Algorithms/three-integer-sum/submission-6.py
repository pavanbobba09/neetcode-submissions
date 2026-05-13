class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #lets sort the array so i can move the left and right pointer

        result = []

        sortedArray = nums.sort()

        n = len(nums)

        for i in range((n)-2):
            if i >0 and nums[i] == nums[i-1]: #checking the duplicate elements
                continue

            left = i+1
            right = n-1

            while left<right:

                total = nums[i]+nums[left]+nums[right]

                if total == 0:
                    result.append([nums[i],nums[left],nums[right]])

                    left = left+1
                    right = right-1

                    while nums[left] == nums[left-1] and left<right:
                        left = left+1
                    while nums[right] == nums[right+1] and left<right:
                        right= right-1

                

                elif total<0:
                    left+=1
                else:
                    right-=1

        
        return result


        

