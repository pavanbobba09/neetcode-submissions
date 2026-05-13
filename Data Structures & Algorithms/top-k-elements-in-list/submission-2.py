class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num]+=1
            else:
                frequency[num] = 1

            
        #lets create buckets
        buckets = []

        for i in range(len(nums)+1):
            buckets.append([])

        # as per the frequency lets arrange add the value into the bucket

        for num in frequency:
            value = frequency[num]
            buckets[value].append(num) 

        #lets collect top k elements

        result = []

        for i in range(len(buckets) -1,0,-1):
            for num in buckets[i]:
                result.append(num)

            if len(result) == k:
                return result

        return result



        