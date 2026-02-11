class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        win = set()
        L = 0
        for R in range(len(nums)):
            if nums[R] in win:
                return True
            win.add(nums[R])
            if len(win)>k:
                win.remove(nums[L])
                L+=1
        return False
            

        
        