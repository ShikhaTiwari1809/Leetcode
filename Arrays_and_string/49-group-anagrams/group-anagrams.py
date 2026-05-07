from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch_map = defaultdict(list)
        
        for ch in strs:
            count = [0] * 26
            for c in ch:
                count[ord(c) - ord('a')] += 1
            
            ch_map[tuple(count)].append(ch)
        
        return list(ch_map.values())