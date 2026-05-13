class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Edge case: empty array
        if not nums:
            return 0
        
        uniqueElement = set(nums)  # This already handles everything!
        maxLength = 0  # Initialize max length
        
        # Loop through each unique number
        for num in uniqueElement:
            # Check if this is the START of a sequence
            if (num - 1) not in uniqueElement:
                currentElement = num
                currentLength = 1
                
                # Count how long the sequence goes
                while (currentElement + 1) in uniqueElement:
                    currentElement += 1
                    currentLength += 1
                
                # Update the maximum length
                maxLength = max(maxLength, currentLength)
        
        return maxLength