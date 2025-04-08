# Decrypt String from Alphabet to Integer Mapping
# You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
# Return the string formed after mapping.

# The test cases are generated so that a unique mapping will always exist.

 

# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"
class Solution(object):
    def freqAlphabets(self, s):
        alpha=" abcdefghijklmnopqrstuvwxyz"
        letter,m,n=alpha,{},len(s)
        for i in range(1,27):
            if i<10:
                m[str(i)]=letter[i]
            else:
                m[str(i)+"#"]=letter[i]
        res,index="",0
        while index<n:
            if index+2<n and s[index+2]=="#":
                res+=m[s[index:index+3]]
                index+=3
            else:
                res+=m[s[index]]
                index+=1
        return res
