class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count=0
        target=threshold*k
        win_sum=sum(arr[:k])
        if win_sum >=target:
            count+=1
        for i in range(k,len(arr)):
            win_sum +=arr[i]
            win_sum -=arr[i-k]
            if win_sum >= target:
                count+=1
        return count

        