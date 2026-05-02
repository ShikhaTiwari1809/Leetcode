from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        countt = Counter(t)

        print(counts)
        print(countt)

        return counts == countt