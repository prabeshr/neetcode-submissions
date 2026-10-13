class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        word = ""
        for a, b in zip(word1, word2):
            word += a+b

        if len(word1) > len(word2):
            word += word1[len(word2):]
        else :
            word += word2[len(word1):]

        return word
