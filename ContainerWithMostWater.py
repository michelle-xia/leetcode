class Solution:
    def maxArea(self, height):
        maxval = 0
        left, right = 0, len(height) - 1
        while left < right:
            maxval = max(maxval, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxval