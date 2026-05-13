class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""

        for x in strs:
            sol+= str(len(x))+"#"+x

        return sol

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0 #left pointer

        while i <len(s):
            j = i

            while s[j] != "#":
                j+=1
            
            length = int(s[i:j]) #2

            word = s[j+1: j+1+length]

            result.append(word)

            i = j+1+length

        return result




