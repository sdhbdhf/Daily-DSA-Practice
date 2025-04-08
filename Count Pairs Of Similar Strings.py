#Best solution
class Solution(object):
    def similarPairs(self, words):
        freq = {}
        count = 0
        for word in words:
            key = frozenset(word)
            if key in freq:
                count += freq[key]
            if key not in freq:
                freq[key] = 0
            freq[key] += 1

        return count
#Worest solution
# class Solution(object):
#   def similarPairs(self, words):
#       count = 0

#       for i in range(len(words)):
#           for j in range(i + 1, len(words)):
#               w1 = words[i]
#               w2 = words[j]

#               # Check if all letters in w1 are in w2 and vice versa
#               all_in = True
#               for ch in w1:
#                   if ch not in w2:
#                       all_in = False
#                       break
#               for ch in w2:
#                   if ch not in w1:
#                       all_in = False
#                       break

#               if all_in:
#                   count += 1

#       return count

