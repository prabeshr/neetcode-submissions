class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = sorted(s)
        t_dict = sorted(t)
        return s_dict == t_dict
    

