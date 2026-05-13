class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_lenght = 0
        uniqueElements = set()

        for right in range(len(s)):
            while s[right] in uniqueElements:
                #if the elements is found lets remove it increase the left pointer

                uniqueElements.remove(s[left])
                left+=1


            

            #add to set
            uniqueElements.add(s[right])

            #max_lenght
            max_lenght = max(max_lenght,right-left+1)


        return max_lenght


        