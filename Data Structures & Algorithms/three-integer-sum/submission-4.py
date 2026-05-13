class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()  # sort() returns None, don't assign it
        n = len(nums) - 1

        for i in range(len(nums) - 2):
            
            # Skip duplicates for i
            if i > 0 and nums[i] == nums[i-1]:
                continue  # ✅ Fixed typo

            left = i + 1
            right = n

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1  # ✅ Fixed capitalization
                    right -= 1

                    # Skip duplicates - compare with PREVIOUS position
                    while left < right and nums[left] == nums[left-1]:  # ✅ Fixed
                        left += 1
                    while left < right and nums[right] == nums[right+1]:  # ✅ Fixed
                        right -= 1  # ✅ Fixed direction

                elif total < 0:  # ✅ Fixed <= to 
                    left += 1
                else:
                    right -= 1

        return result  # ✅ OUTSIDE the for loop!