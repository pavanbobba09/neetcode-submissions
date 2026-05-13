class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # for encoding lets add the length+#
        sol = ""
        for num in strs:
            sol += str(len(num))+"#"+ num


        return sol

    def decode(self, s: str) -> List[str]:


        result = []

        i = 0
        while i < len(s):
            j = i
            #lets check until #
            while s[j] != "#":
                j+=1
            
            #take the lenght
            length = int(s[i:j]) # here we are not taking the last element

            word = s[j+1 : j+1+length]

            result.append(word)

            i = j+1+length

        return result
