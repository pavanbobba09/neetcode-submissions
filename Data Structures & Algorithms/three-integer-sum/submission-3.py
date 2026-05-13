class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        for i in range(len(nums)):
        

            if i>0 and nums[i] == nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            #lets get the total value
            while l<r:
                total = nums[i]+nums[l]+nums[r]

                if total<0:
                    l+=1
                elif total>0:
                    r= r-1

                else:
                    sol.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    r = r-1

                    while l<r and nums[l] == nums[l-1]:
                        l = l+1
                    while l<r and nums[r] == nums[r+1]:
                        r = r-1

        return sol




        






        

