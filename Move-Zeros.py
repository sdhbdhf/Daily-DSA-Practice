class Solution(object):
    def moveZeroes(self, nums):
        if len(l)==1 or len(l)==0:
            return l
        le=0
        ri=len(l)-1
        while le<=ri:
            if l[le]==0 or len[ri]==0:
                l[le],l[ri]=l[ri],l[le]
                ri-=1
                le+=1
        return l
