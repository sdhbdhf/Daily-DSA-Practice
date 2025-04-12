# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 
class Solution(object):
    def commonChars(self, words):
        list1=[]
        temp=words[0]
        for i in range(len(words)):
            if len(words[i])<len(temp):
                temp=words[i]
        for i in range(len(temp)):
            found = True
            char = temp[i]


            for j in range(len(words)):
                if char in words[j]:
                    words[j] = words[j].replace(char, '', 1)
                else:
                    found = False
                    break

            if found:
                list1.append(char)

        return list1
        
