class Solution:
    def maxArea(self, heights: List[int]) -> int:
       
        sol = 0

        #since we are comparing from the both the ends we need to focus on the rectangle formulae and the two pointer approach

        l , r = 0, len(heights)-1

        while l<r:
            area = (r-l)*min(heights[l], heights[r])
            sol = max(area,sol)

            if heights[l]<heights[r]:
                l +=1 
            elif heights[l]>heights[r]:
                r -= 1
            else:
                l=l+1
                r=r-1
            
        
        return sol




