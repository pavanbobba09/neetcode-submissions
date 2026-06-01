class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        maxLength = 0
        elements = set()

        for right in range(len(s)):
            while s[right] in elements:
                elements.remove(s[left])
                left+=1


            
            elements.add(s[right])
            maxLength = max(maxLength,right-left+1)

        return maxLength
        