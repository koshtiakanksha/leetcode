class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []                             # to hold (i,h)->(index, height)
        for i, h in enumerate(heights):    
            start = i
            while stack and stack[-1][1]>h:# stack[-1][1]= height of last ele in stack
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start, h))
        for index, height in stack: # those height that can go all the way to the last
            maxArea = max(maxArea, height*(len(heights)-index))
        return maxArea
    
    # time complexity = O(N)
    # space complexity = O(N)
    