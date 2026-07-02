class Solution(object):
    def firstMissingPositive(self, nums):
        nums=sorted(nums)
        if len(nums)==0:
            return 1
        one=False
        for i in range(len(nums)):
            if nums[i]==1:
                one=True
        if not one:
            return 1
            
        
        for i in range(len(nums)-1):

            if nums[i]>=0:
                if nums[i] == nums[i+1]:
                    pass
                elif nums[i]+1 != nums[i+1]:
                    return nums[i]+1
                

        if nums[-1]<=0 :
            return 1
        else:
            return nums[-1]+1
        