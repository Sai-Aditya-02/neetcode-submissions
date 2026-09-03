class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', s)

        # print(cleaned_text)
        return cleaned_text.lower() == cleaned_text[::-1].lower()
