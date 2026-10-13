class Solution:
    def validPalindrome(self, s: str) -> bool:

        b = len(s)-1

        for i in range(len(s)//2):

            if s[i] != s[b-i]:

                a = s[:i] + s[i +1:]

                b = s[: b-i] + s[b-i+1:]
                
                count_a = 0
                count_b = 0
                for j in range(len(a)//2):

                    if a[j] != a[len(a)-1-j]:
                        count_a +=1

                

                for k in range(len(b)//2):

                    if b[k] != b[len(b)-1-k]:
                        count_b +=1

                if count_a ==0 or count_b ==0:
                    return True
                else:
                    return False
                
        return True
        