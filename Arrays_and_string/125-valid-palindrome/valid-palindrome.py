class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_text = []
        for i in range(len(s)):
            
            if (ord(s[i])>=ord('A') and ord(s[i])<=ord('Z')) or (ord(s[i])>=ord('a') and ord(s[i])<=ord('z'))or (ord(s[i])>=ord('0') and ord(s[i])<=ord('9')):
                clean_text.append(s[i].lower())
        print(clean_text)
        return clean_text == clean_text[::-1]
       
       #clean_text = re.sub(r'[^a-zA-Z0-9]','',s).lower()
       #clean_text = list(clean_text)
       #return clean_text == clean_text[::-1]

       #cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
       
        