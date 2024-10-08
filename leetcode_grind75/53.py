# 53. Maximum Subarray

#nc solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0] #we don't actually need the elements of the subarray themselves, just the sum
        cur = 0

        for n in nums:
            if cur < 0:
                cur = 0 #resets the sum back to 0
            cur += n
            maxSub = max(maxSub, cur) #only keeps the max value
        
        return maxSub
    
#take 2 from memory
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxsum, cur = nums[0], 0
        for i in range(0, len(nums)):
            if cur < 0:
                cur = 0
            
            cur += nums[i]
            maxsum = max(maxsum, cur)
        
        return maxsum