class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = []
        maxlen = 0

        for ch in s:
            while ch in substr:          # keep removing until duplicate is gone
                substr.pop(0)            # remove from left
            substr.append(ch)
            maxlen = max(maxlen, len(substr))

        return maxlen