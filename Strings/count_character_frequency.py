# ---------------------------------------------------------
# DSA Problem 13: Count Character Frequency
# ---------------------------------------------------------
# Problem:
# Count how many times each character appears
# in a string.
#
# Example:
# Input:  "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to count character frequency
def character_frequency(text):

    # Create an empty dictionary.
    # It will store:
    # character -> number of occurrences
    frequency = {}

    # Traverse every character in the string
    for char in text:

        # Check whether the character already exists
        if char in frequency:

            # If it exists, increase its count by 1
            frequency[char] += 1

        else:

            # If it doesn't exist, start its count at 1
            frequency[char] = 1

    # Return the frequency dictionary
    return frequency


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

text = "hello"

result = character_frequency(text)

print("String:", text)
print("Character frequency:", result)