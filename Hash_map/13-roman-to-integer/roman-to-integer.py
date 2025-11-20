class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        prev = 0
        char_values = []
        for char in reversed(s):
            char_value = roman_value[char]
            if char_value < prev:
                total -= char_value
            else:
                total += char_value
            prev = char_value

        return total

       
        return total_value

        