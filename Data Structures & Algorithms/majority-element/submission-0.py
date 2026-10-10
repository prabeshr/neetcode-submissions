class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        s_dict = {}

        for sa in nums:
            if sa not in s_dict:
                s_dict[sa] = 1
            else:
                s_dict[sa] +=1

        return(max(s_dict, key =s_dict.get))
        