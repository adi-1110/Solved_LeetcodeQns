class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s_list=[]
        existing=""
        ans=""

        for ch in s:
            if ch.isalpha() or ch.isdigit():
                s_list.append(ch)
            
        for ch in reversed(s_list):

            ans+=ch
        for ch in s_list:

            existing+=ch

        if existing == ans:
            return True
        else:
            return False


        