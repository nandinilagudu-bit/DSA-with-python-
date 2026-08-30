# ---------------------------------------------------------
# DSA Problem 14: Check if Two Strings are Anagrams
# ---------------------------------------------------------
# Problem:
# Two strings are anagrams if they contain the same
# characters with the same frequency.
#
# Example:
# Input:
# "listen"
# "silent"
#
# Output:
# True
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to check whether two strings are anagrams
def are_anagrams(text1, text2):

    # If the strings have different lengths,
    # they cannot be anagrams
    if len(text1) != len(text2):
        return False

    # Create a dictionary for the first string
    frequency = {}

    # Count each character in the first string
    for char in text1:

        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Traverse through the second string
    for char in text2:

        # If the character doesn't exist in the dictionary,
        # the strings cannot be anagrams
        if char not in frequency:
            return False

        # Reduce the frequency
        frequency[char] -= 1

        # If frequency becomes negative,
        # there are too many occurrences of that character
        if frequency[char] < 0:
            return False

    # If all character counts match,
    # the strings are anagrams
    return True


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

text1 = "listen"
text2 = "silent"

result = are_anagrams(text1, text2)

print("First string:", text1)
print("Second string:", text2)
print("Are anagrams:", result)