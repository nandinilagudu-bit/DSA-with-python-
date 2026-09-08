# ---------------------------------------------------------
# DSA Problem 18: Reverse Words in a String
# ---------------------------------------------------------
# Problem:
# Reverse the order of words in a sentence.
#
# Example:
# Input:
# "I love Python"
#
# Output:
# "Python love I"
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to reverse the words
def reverse_words(sentence):

    # Split the sentence into individual words
    words = sentence.split()

    # Create an empty string for the result
    result = ""

    # Traverse the words from the last word to the first
    for i in range(len(words) - 1, -1, -1):

        # Add the current word to the result
        result += words[i]

        # Add a space between words
        if i != 0:
            result += " "

    # Return the reversed sentence
    return result


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

sentence = "I love Python"

result = reverse_words(sentence)

print("Original sentence:", sentence)
print("Reversed words:", result)