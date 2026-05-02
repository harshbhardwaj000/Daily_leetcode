from collections import defaultdict
class Solution(object):
    def minimumDistance(self, nums):
        position = defaultdict(list)
        for i in range(len(nums)):
            position[nums[i]].append(i)
        ans = float('inf')

        for key in position:
            indices =position[key]
            if len(indices)>=3:
                for i in range(len(indices)-2):
                    dis=2*(indices[i+2]-indices[i])
                    if dis < ans:
                        ans = dis
        if ans == float('inf'):
            return -1
        return ans