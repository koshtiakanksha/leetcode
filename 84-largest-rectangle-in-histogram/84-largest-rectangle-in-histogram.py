class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # to hold (i,h)->(index, height)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start, h))
        for index, height in stack:
            maxArea = max(maxArea, height*(len(heights)-index))
        return maxArea