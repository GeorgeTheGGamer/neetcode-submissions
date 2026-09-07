class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Ignore all case and non-alphanumeric values
        result = ''
        for c in s:
            if c.isalnum():
                result += c.lower()
        return result == result[::-1]

        
        