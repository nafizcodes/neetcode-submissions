class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        vowel_set = set("aeiou")
        # vowel_set = {"a", "e", "i", "o", "u"}
        # words = ["aba","bcb","ece","aa","e"]
        prefix_cnt = [0]*(len(words)+1)
        # [0,0,0,0,0,0]
             
        # [0,1,1,2,3,4]


        # for i,w in enumerate(words):
        #     v = 0
        #     if w[0] in vowel_set and w[-1] in vowel_set:
        #         v += 1
            
        #     prefix_cnt[i+1] = prefix_cnt[i] + v

        
        prev = 0
        for i,w in enumerate(words):
            if w[0] in vowel_set and w[-1] in vowel_set:
                prev += 1
            
            prefix_cnt[i+1] = prev

        
        res = [0] * len(queries)
        
        for i, q in enumerate(queries):
            l, r = q
            res[i] = prefix_cnt[r + 1] - prefix_cnt[l]
        return res
            

