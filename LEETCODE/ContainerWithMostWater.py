#bruteforce
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                left_h=height[i]
                right_h=height[j]
                area=min(left_h,right_h)*(j-i)
                max_area=max(area,max_area)
        return max_area
#optimal
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while left<right:
            area=min(height[left],height[right])*(right-left)
            max_area=max(max_area,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area
     