import heapq
class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        h = len(heights)
        queue = []
        for i in range(h-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(queue,diff)
                if len(queue) > ladders:
                    small_jump =heapq.heappop(queue)
                    bricks -= small_jump
                if bricks < 0:
                    return i
        return len(heights) - 1
            





        
        