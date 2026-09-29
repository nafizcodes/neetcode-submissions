class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # charSet = {}

        # res = 0

        # l = 0 


        # for r in range(len(s)):
        #     charSet[s[r]] = 1 + charSet.get(s[r], 0)

        #     while (r-l+1) - max(count.a)
        #     res = max(res, r-l+1)



        
        # s="ABAB"
        #    l
        #    r

        #    A: 2 
        #    B: 2

        #    count = 1


        res = 0
        charSet = set(s)

        for c in charSet:
            count = 0
            l = 0

            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r-l+1) - count > k:
                    if s[l] == c:
                        count -= 1
                
                    l += 1
                res = max(res, r-l + 1)
            

        return res

                
