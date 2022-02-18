# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        # If the current rectangle does not contain any ships, return 0.         
        if (bottomLeft.x > topRight.x) or (bottomLeft.y > topRight.y):
            return 0
        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # If the rectangle represents a single point, a ship is located.
        if (topRight.x == bottomLeft.x) and (topRight.y == bottomLeft.y):
            return 1

        # Recursively check each of the 4 sub-rectangles for ships.
        mid_x = (topRight.x + bottomLeft.x) // 2
        mid_y = (topRight.y + bottomLeft.y) // 2
        return self.countShips(sea, Point(mid_x, mid_y), bottomLeft) + \
               self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1)) + \
               self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1)) + \
               self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
