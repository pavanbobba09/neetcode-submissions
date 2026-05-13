class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        my_set = set()
        maxValue = 0
        for right in range(len(s)):
            while s[right] in my_set:
                #we need to push the elements to left until the we reaches the gith
                my_set.remove(s[left])
                left+=1

            
            my_set.add(s[right])

            maxValue = max(maxValue,right-left+1)

        return maxValue

        


            
        