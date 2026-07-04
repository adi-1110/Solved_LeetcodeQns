class Solution(object):
    def reverseString(self, s):
        
        for i in range(len(s)/2):
            
            if i != len(s)/2 or len(s)%2 == 0:
                x=s[i]
                s[i]=s[-i-1]
                s[-i-1]=x
        

        return None
        