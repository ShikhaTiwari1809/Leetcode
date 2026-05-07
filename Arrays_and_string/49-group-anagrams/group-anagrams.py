from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ch_map = defaultdict(list)

        for ch in strs:
            #print(tuple(ch))
            #print(Counter(ch))
            ch_map[tuple(sorted(ch))].append(ch)
        print(ch_map)
        return list(ch_map.values())