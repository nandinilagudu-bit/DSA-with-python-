# ---------------------------------------------------------
# DSA Problem 20: Longest Common Prefix
# ---------------------------------------------------------
# Problem:
# Given a list of strings, find the longest common
# prefix shared by all strings.
#
# Example:
# Input:
# ["flower", "flow", "flight"]
#
# Output:
# "fl"
#
# Time Complexity: O(n * m)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to find the longest common prefix
def longest_common_prefix(words):

    # If the list is empty, there is no common prefix
    if not words:
        return ""

    # Assume the first word is the common prefix
    prefix = words[0]

    # Compare the prefix with every other word
    for word in words[1:]:

        # Continue reducing the prefix until the current
        # word starts with the same prefix
        while not word.startswith(prefix):

            # Remove the last character from the prefix
            prefix = prefix[:-1]

            # If the prefix becomes empty,
            # there is no common prefix
            if not prefix:
                return ""

    # Return the longest common prefix
    return prefix


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

words = ["flower", "flow", "flight"]

result = longest_common_prefix(words)

print("Words:", words)
print("Longest common prefix:", result)