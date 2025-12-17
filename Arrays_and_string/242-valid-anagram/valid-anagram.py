from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        print(count_s)
        print(count_t)
        return count_s == count_t
        