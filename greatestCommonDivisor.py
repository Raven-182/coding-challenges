# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        #gcd of string 
        #if commutative law not followed then return the empty string
        if str1 + str2 != str2 + str1:
            return ''
        else:
            length = self.hcf(len(str1), len(str2))
            return str1[:length]
        
    def hcf(self, num1, num2):
        #remainder of one divides the other until you hit 0

        return num2 if num1 == 0 else self.hcf(num2% num1, num1)
    
