class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # If left is not alphanumeric, increment left pointer by one step
            if not s[left].isalnum():
                left += 1
                continue
            # If right is not alphanumeric, decrement right pointer by one step
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
        
