from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = defaultdict(list)
        for st in strs:
            #print(''.join(sorted(set(st)))
            cur_key = ''.join(sorted(st))
            ans[cur_key].append(st)

        final_op = list(ans.values())
        print(final_op)
        return final_op
