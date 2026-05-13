class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #let check if the element is already present

        elementPresent = {}

        for x in strs:
            sortedValue = ''.join(sorted(x))


            #lets check elements is already present in the list

            if sortedValue not in elementPresent:
                #when the element is not there 
                #lets create an new list for it
                elementPresent[sortedValue] = []

            elementPresent[sortedValue].append(x)


        #we need to return the value of list
        return list(elementPresent.values())