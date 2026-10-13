class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        length_1 = len(word1)
        length_2 = len(word2)

        length = min(length_1, length_2)
        word = ""
        for i in range(length):

            word+=word1[i]
            word+=word2[i]

        if length_1 > length_2:
            word += word1[length_2:]
        if length_2> length_1:
            word += word2[length_1:]

        return word
