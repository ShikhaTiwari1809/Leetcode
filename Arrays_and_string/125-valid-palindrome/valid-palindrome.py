class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def check_alphanum(ch):
            if (ord(ch)>=ord('A') and ord(ch)<=ord('Z')) or (ord(ch)>=ord('a') and ord(ch)<=ord('z')) or (ord(ch)>=ord('0') and ord(ch)<=ord('9')):
                return True
        left =0
        right = len(s)-1

        while left<right:
            while left<right and not check_alphanum(s[left]):
                left +=1
            while left<right and not check_alphanum(s[right]):
                right -=1  
            
            if s[left].lower()!=s[right].lower():
                return False
            left +=1
            right -=1 
        return True
       
       #clean_text = re.sub(r'[^a-zA-Z0-9]','',s).lower()
       #clean_text = list(clean_text)
       #return clean_text == clean_text[::-1]

       #cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
       
        