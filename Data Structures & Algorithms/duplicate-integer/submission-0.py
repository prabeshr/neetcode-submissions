class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num = set(nums)
        if len(num)<len(nums) and len(nums)>1:
            return True

        return False
        