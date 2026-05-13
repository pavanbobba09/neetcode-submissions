class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        freq = {}

        for i in s:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1

        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -=1
            if freq[ch] < 0:
                return False

        return True
        

        