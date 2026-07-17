class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]* 26   # 26 alphbets

            for c in s:
                count[ord(c) - ord('a')] += 1    #80-80-> 0 for character a 
            res[tuple(count)].append(s)
        
        return list(res.values())