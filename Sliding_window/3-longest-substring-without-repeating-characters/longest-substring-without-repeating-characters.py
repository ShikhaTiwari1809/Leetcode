class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_set = set()
        l = 0
        longest_len = 0

        for r in range(len(s)):
            # Shrink window if duplicate found
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            
            # Add current char
            char_set.add(s[r])

            # Update longest length
            longest_len = max(longest_len, r - l + 1)

        return longest_len
