class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #we can use the fast and slow pointer approch 

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

            #in above we found a ccycle


        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow