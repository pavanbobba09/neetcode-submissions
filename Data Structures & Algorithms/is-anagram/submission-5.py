class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #size:
        if len(s) != len(t):
            return False
        
        counter = Counter(s)

        for x in t:
            if counter[x] <=0:
                return False
            else:
                counter[x] -=1

        
        return True
        
        