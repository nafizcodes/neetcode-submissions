# Brute Force

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         # res = 0

#         # for i in range(len(s)):
#         #     charSet = set()

#         #     for j in range(i, len(s)):
#         #         if s[j] in charSet:
#         #             break

#         #         charSet.add(s[j])
            
#         #     res = max(res, len(charSet))

#         # return res 


# Optimal

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # abacabc
        # l
        # r

        hashset = set()
        l = 0
        r = 0
        length = 0

        while r < len(s):
            while s[r] in hashset:

                hashset.remove(s[l])
                l += 1


            hashset.add(s[r])
            length = max(length, r-l + 1)
            r += 1

        return length

            

            
                
       
       
      
 