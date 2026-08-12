# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = ""

#         for c in s:
#             if c.isalnum():
#                 newStr += c.lower()
        
#         return newStr == newStr[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.isalNum(s[l]):
                l += 1
            while r > l and not self.isalNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l+1
            r = r-1
        return True



    def isalNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
