class Solution:
    def trap(self, height: List[int]) -> int:

        water = 0
        leftt = 0

        if len(height) < 3:
            return 0

        rightt = len(height)-1
        leftmax = height[leftt]

        rightmax = height[rightt]

        while leftt < rightt:

            if height[leftt] <= height[rightt]:

                if height[leftt] > leftmax:

                    leftmax = height[leftt]
                else:
                    water += leftmax - height[leftt] 

                leftt +=1

            else:


                if height[rightt] > rightmax:

                    rightmax = height[rightt]

                else:

                    water += rightmax - height[rightt]

                rightt -=1

        return water









            
        