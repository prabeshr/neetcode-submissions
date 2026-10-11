class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] +=1
        
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in num_dict.items():
            bucket[value].append(key)

        result = []

        i = len(nums)
        while i > 0 and len(result)<k:

            for num in bucket[i]:
                result.append(num)
                if len(result) ==k:
                    break
            i -=1

        return result



        