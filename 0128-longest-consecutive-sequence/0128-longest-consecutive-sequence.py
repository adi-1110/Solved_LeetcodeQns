 
class Solution(object):
    def longestConsecutive(self, nums):
        numset=set(nums)
        longest=0

        for num in numset:

            if num-1  not in numset:
                length=1
                while num+1  in numset:
                    num+=1
                    length+=1
                longest=max(longest,length)
        
        return longest
                    


        
        