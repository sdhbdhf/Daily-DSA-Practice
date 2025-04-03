# Q. Palindrome Number
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution(object):
    def isPalindrome(self, x):
        reversed=0
        temp2=x
        while x>0:
            temp=x%10
            reversed=reversed*10+temp
            x//=10
        if temp2==reversed:
            return True 
        else:
            return False 

        
