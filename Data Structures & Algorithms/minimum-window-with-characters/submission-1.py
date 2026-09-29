class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        S = len(s)
        T = len(t)

        if S < T:
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        # for c in t:
        #     if c not in countT:
        #         countT[c] = 1
        #     else:
        #         countT[c] += 1 

        minWin = 10**6
        start = -1

        l = 0

        def valid():
            # O(52)
            for key in countT:
                if key not in window:
                    return False
                elif window[key] < countT[key]:
                    return False

            return True


        for r in range(S):
            if s[r] not in window:
                window[s[r]] = 1
            else:
                window[s[r]] += 1

            while valid():
                w = r - l + 1

                if w < minWin:
                    start = l
                    minWin = w
                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1

                l += 1

            
        if minWin == 10**6:
            return ""

        else:
            return s[start:start+minWin]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        S = len(s)
        T = len(t)

        if S < T:
            return ""

        countT = {}
        window = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        # for c in t:
        #     if c not in countT:
        #         countT[c] = 1
        #     else:
        #         countT[c] += 1 

        minWin = 10**6
        start = -1

        l = 0
        have = 0
        need = len(countT)

        # def valid():
        #     # O(52)
        #     for key in countT:
        #         if key not in window:
        #             return False
        #         elif window[key] < countT[key]:
        #             return False

        #     return True


        for r in range(S):
            if s[r] not in window:
                window[s[r]] = 1
            else:
                window[s[r]] += 1


            if s[r] in countT and window[s[r]] == countT[s[r]]:
                have += 1

            while have  == need :

                w = r - l + 1

                if w < minWin:
                    start = l
                    minWin = w

                leftchar = s[l]
                if leftchar in countT and window[leftchar] == countT[leftchar]:
                    have -= 1


                if window[s[l]] == 1:
                    del window[s[l]]
                else:
                    window[s[l]] -= 1

                l += 1

            
        if minWin == 10**6:
            return ""

        else:
            return s[start:start+minWin]


          