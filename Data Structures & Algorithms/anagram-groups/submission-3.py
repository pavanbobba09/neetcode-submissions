class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashmap = {}

        for x in strs:
            sortedValue = ''.join(sorted(x))

            if sortedValue not in hashmap:
                hashmap[sortedValue] = []

            hashmap[sortedValue].append(x)

        return list(hashmap.values())        