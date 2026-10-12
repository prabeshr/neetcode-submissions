class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        a = len(nums)
        prefix = [1]* a
        suffix = 1
        for i in range(1,len(nums)):

            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(a-1, -1, -1):

            prefix[i] = prefix[i] * suffix

            suffix *= nums[i]

        return prefix



        