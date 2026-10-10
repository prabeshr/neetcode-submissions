class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        b = strs[0]
        count = 0
        for i in range(len(b)):
            print("value of i: ",i)
            for j in range(1,len(strs)):

                print("Value of j: ",j)
                if len(strs[j]) <=count:
                     return b[0:count]
                if strs[j][count] != b[count]:
                    return b[0:count]
            count +=1

        return b[0:count]


        