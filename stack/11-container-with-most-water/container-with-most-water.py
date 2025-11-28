class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height) -1
        area = 0
        while l < r:
            area = max(area, min(height[l],height[r]) * (r -l))
            if height[l] <= height [r]:
                l = l + 1
      
            else:
                r = r - 1
            
        return area

        