class Solution(object):
    def longestOnes(self, nums, k):
        window=0
        Left=0
        count=0
        for R in range(len(nums)):
            if nums[R] == 0:
                count += 1
            while(count > k):
                if nums[Left] == 0:
                    count -=1
                Left +=1
            win =R - Left +1
            window = max(window,win)
        return window


    '''window aage badhate raho aur zero count karte raho , agar zero count >k hai to max length rkho,
     zero count kam krte raho aur window start aage badhate raho'''
    
        
        