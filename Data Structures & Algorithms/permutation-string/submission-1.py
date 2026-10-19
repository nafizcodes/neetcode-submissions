# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
        
#         s1Count = [0]*26
#         s2Count = [0]*26

#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1

#         matches = 0
#         for i in range(26):
#             matches += (1 if s1Count[i] == s2Count[i] else 0)

#         l = 0
#         for r in range(len(s1), len(s2)):
#             if matches == 26:
#                 return True

#             index = ord(s2[r]) - ord('a')
#             s2Count[index] += 1

#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] + 1 == s2Count[index]:  
#                 matches -= 1

#             index = ord(s2[l]) - ord('a')
#             s2Count[index] -= 1
#             if s1Count[index] == s2Count[index]:
#                 matches += 1
#             elif s1Count[index] - 1 == s2Count[index]:  
#                 matches -= 1
#             l += 1

#         return matches == 26

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:

#         if len(s1) > len(s2):
#             return False

#         s1Count = [0] * 26
#         s2Count = [0] * 26

#         # Build frequency counts for initial window
#         for i in range(len(s1)):
#             s1Count[ord(s1[i]) - ord('a')] += 1
#             s2Count[ord(s2[i]) - ord('a')] += 1

#         if s1Count == s2Count:
#             return True

#         # Slide the window across s2
#         for r in range(len(s1), len(s2)):

#             # Add new right character
#             s2Count[ord(s2[r]) - ord('a')] += 1

#             # Remove old left character
#             s2Count[ord(s2[r - len(s1)]) - ord('a')] -= 1
#                     #index of the left most char
#             # Check if window is a permutation
#             if s1Count == s2Count:
#                 return True

#         return False
        
# s1="ab"
# s2="eidbaooo"


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1C = [0]*26
        s2C = [0]*26

        for i in range(len(s1)):
            s1C[ord(s1[i])- ord('a')] += 1
            s2C[ord(s2[i])- ord('a')] += 1


        if s1C == s2C:
            return True

        for r in range(len(s1), len(s2)):

            s2C[ord(s2[r]) - ord('a')] += 1

            s2C[ord(s2[r-len(s1)]) - ord('a')] -= 1

            if s1C == s2C:
                return True

        return False