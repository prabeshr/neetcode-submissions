class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if len(s) != len(t):
            return False

        for sa in s:

            if sa not in s_dict:
                s_dict[sa] = 1
            else:
                s_dict[sa] +=1

        for ta in t:

            if ta not in t_dict:
                t_dict[ta] = 1
            else:
                t_dict[ta] +=1

        if len(t_dict) != len(s_dict):
            return False

        for sa in s:
            if sa not in t_dict:
                return False
            if s_dict[sa] != t_dict[sa]:
                return False

        return True
    

