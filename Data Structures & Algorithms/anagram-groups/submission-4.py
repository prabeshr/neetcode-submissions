class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        sorted_dict = {}
        for i in range(len(strs)):
            s = strs[i]
            key = "".join(sorted(s))
            if key not in sorted_dict:
                sorted_dict[key] = []
            sorted_dict[key].append(i)

        result = []
        for indices in sorted_dict.values():
            temp = []
            for i in indices:
                temp.append(strs[i])
            result.append(temp)

        return(result)

        