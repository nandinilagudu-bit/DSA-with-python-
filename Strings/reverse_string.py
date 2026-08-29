# ---------------------------------------------------------
# DSA Problem 11: Reverse a String
# ---------------------------------------------------------
# Problem:
# Given a string, reverse it without using
# Python's built-in reversed() function.
#
# Example:
# Input:  "hello"
# Output: "olleh"
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to reverse the string
def reverse_string(text):

    # Create an empty string to store the reversed result
    reversed_text = ""

    # Traverse the string from the last character
    # to the first character
    for i in range(len(text) - 1, -1, -1):

        # Add each character to the result
        reversed_text += text[i]

    # Return the reversed string
    return reversed_text


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

text = "hello"

result = reverse_string(text)

print("Original string:", text)
print("Reversed string:", result)