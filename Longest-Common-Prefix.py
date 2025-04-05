class Solution(object):
    def longestCommonPrefix(self, strs):
        cont=[]
        prefix=strs[0]
        for i in range(1,len(strs)):
            if len(prefix)>len(strs[i]):
                prefix=strs[i]
               
        for i in range(len(prefix)):
            for j in range(len(strs)):
                if prefix[i] !=strs[j][i]:
                    return "".join(cont)
            cont.append(strs[j][i])
        return "".join(cont)
