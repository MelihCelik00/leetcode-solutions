class Solution:
    def isPalindrome(self, s: str) -> bool:
        # TODO: convert all uppercase to lowercase
        # TODO: remove all non-alphanumeric chars
        formattedString = ''.join(c for c in s if c.isalnum()).lower()

        if formattedString == formattedString[::-1]:
            return True
        
        return False