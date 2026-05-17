class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        counter = Counter(nums)

        buckets = []

        for i in range(len(nums)+1):
            buckets.append([])


        #lets fill the buckes:

        for num in counter:
            value = counter[num]
            buckets[value].append(num)

        
        result = []

        for x in range(len(buckets)-1,-1,-1):
            for num in buckets[x]:
                result.append(num)

            if len(result) == k:
                return result

