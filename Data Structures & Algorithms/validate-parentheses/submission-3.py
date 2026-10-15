class Solution:
    def isValid(self, s: str) -> bool:

        stackk = []

        for i in range(len(s)):

            if s[i] == '{' or s[i] == '[' or  s[i] =='(':
                stackk.append(s[i])
            
            else:
                if len(stackk) == 0:
                    return False
                else:
                    if s[i]=='}' and stackk[-1] == '{': 
                        stackk.pop() 

                    elif s[i]==']' and stackk[-1] == '[': 
                        stackk.pop() 
                    elif s[i]==')' and stackk[-1] == '(': 
                        stackk.pop()
                    else:
                        return False

        if len(stackk) >0:
            return False
        return True
        