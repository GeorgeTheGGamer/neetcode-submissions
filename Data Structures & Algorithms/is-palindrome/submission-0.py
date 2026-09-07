class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n)
        # Two pointers means going from left to right and right to left at the same time
        # Pre process the string

        input = []
        for letter in s:
            if letter.isalnum():
                input.append(letter.lower())

        i = 0
        j = len(input)-1

        while i <= j:
            if input[i] != input[j]:
                return False
            i += 1
            j -= 1
    
        return True
        