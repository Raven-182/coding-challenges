def maxArea(self, height: list[int]) -> int:
    left = 0 
    right = len(height) - 1

    maxArea = 0
    while left < right:
        #area is right - left * the shorter height
        shorter = height[left] if height[left] < height[right] else height[right]
        area = (right - left) * shorter
        maxArea = max(area, maxArea)
        #move the smaller height 
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return maxArea
