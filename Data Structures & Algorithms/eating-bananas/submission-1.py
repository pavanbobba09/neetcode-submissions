class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = right
        

        while left<=right:
            mid = (left+right)//2
            totat_hours = 0
            for pile in piles:
                totat_hours+=math.ceil(pile/mid)
            
            if totat_hours<=h:
                answer = mid
                right = mid-1
            else:
                left = mid+1

        return answer

        