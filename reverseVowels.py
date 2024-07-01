# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(l) - 1
        while left < right:
            if l[left] not in vowels:
                left += 1
            if l[right] not in vowels:
                right -= 1
            if l[left] in vowels and l[right] in vowels:
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1

        return "".join(l)
    
solution = Solution()
print(solution.reverseVowels("hello"))

