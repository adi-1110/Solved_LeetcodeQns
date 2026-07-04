class Solution(object):
    def findErrorNums(self, nums):
        ans=[]
        nums_set=set(nums)
        ans.append( sum(nums)- sum(nums_set) )

        ans.append( (len(nums)*(len(nums)+1)/2) - sum(nums_set))
        
        return ans