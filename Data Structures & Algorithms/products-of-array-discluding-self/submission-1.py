class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        a = len(nums)
        prefix = [1]* a
        suffix = [1]* a
        for i in range(1,len(nums)):

            prefix[i] = prefix[i-1] * nums[i-1]

            suffix[a-1-i] = suffix[a-i]*nums[a-i]

        for i in range(a):

            prefix[i] = prefix[i] * suffix[i]

        return prefix



        