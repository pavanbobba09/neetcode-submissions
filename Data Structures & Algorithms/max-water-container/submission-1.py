class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights)-1
        maximumWater = 0


        while left<right:
            lowestheight = min(heights[left],heights[right])

            maximumWater = max(maximumWater,lowestheight*(right-left))

            #for moving the pointers lets focus on the height
            if heights[left]>heights[right]:
                right -=1
            else:
                left+=1

        
        return maximumWater




            
