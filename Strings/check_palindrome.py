# ---------------------------------------------------------
# DSA Problem 12: Check if a String is a Palindrome
# ---------------------------------------------------------
# Problem:
# A palindrome is a string that reads the same
# forward and backward.
#
# Example:
# Input:  "madam"
# Output: True
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to check for palindrome
def is_palindrome(text):

    # Set two pointers:
    # left starts at the beginning
    left = 0

    # right starts at the end
    right = len(text) - 1

    # Continue until the pointers meet
    while left < right:

        # Compare characters from both ends
        if text[left] != text[right]:

            # If they are different,
            # the string is not a palindrome
            return False

        # Move left pointer forward
        left += 1

        # Move right pointer backward
        right -= 1

    # If all characters matched,
    # the string is a palindrome
    return True


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

text = "madam"

result = is_palindrome(text)

print("String:", text)
print("Is palindrome:", result)