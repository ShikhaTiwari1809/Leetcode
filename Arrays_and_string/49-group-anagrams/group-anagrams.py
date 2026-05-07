from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch_map = defaultdict(list)

        for ch in strs:
            
            ch_map[tuple(sorted(ch))].append(ch)
        
        return list(ch_map.values())