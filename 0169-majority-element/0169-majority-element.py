class Solution(object):
    def majorityElement(self, nums):
        dic={}
        

        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1

        for n in dic:
            if dic[n]==max(dic.values()):
                ans=n
                break

        return ans


        

        