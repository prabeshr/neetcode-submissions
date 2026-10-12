class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] =1
            else:
                num_dict[num] +=1
        b = len(nums)
        a = b//3 + ((b//3) > int(b/3))

        result = []
        
        for key, value in num_dict.items():

            if value > a:
                result.append(key)

        return result


        