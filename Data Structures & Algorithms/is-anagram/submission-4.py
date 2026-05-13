from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyOfEle = defaultdict(int)

         #condition one if both of lenght aerw not same then it not an anagram

        if len(s) != len(t):
            return False

        # increase the counting in the frequency
        for x in s:
            if x in frequencyOfEle:
                frequencyOfEle[x]+=1
            else:
                frequencyOfEle[x] = 1

        for y in t:
            if y in frequencyOfEle:
                frequencyOfEle[y]-=1


        for x in frequencyOfEle:
            if frequencyOfEle[x] != 0:
                return False
            
            

        return True
            
            

        