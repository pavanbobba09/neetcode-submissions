class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for x in strs:
            #sorting the elements
            sortedValue = ''.join(sorted(x))

            #check sorted value
            #add to list

            if sortedValue not in seen:
                seen[sortedValue] = []
            seen[sortedValue].append(x)

            
        return list(seen.values())

        