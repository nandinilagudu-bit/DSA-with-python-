# ---------------------------------------------------------
# DSA Problem 19: Valid Parentheses
# ---------------------------------------------------------
# Problem:
# Given a string containing (), {}, and [],
# determine whether the brackets are correctly matched.
#
# Example:
# Input:  "{[()]}"
# Output: True
#
# Input:  "{[(]}"
# Output: False
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to check valid parentheses
def is_valid_parentheses(text):

    # Create an empty list to use as a stack
    stack = []

    # Create a dictionary that maps closing brackets
    # to their corresponding opening brackets
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    # Traverse every character in the string
    for char in text:

        # Check if the character is an opening bracket
        if char in "([{":

            # Add the opening bracket to the stack
            stack.append(char)

        # Otherwise, the character is a closing bracket
        else:

            # If the stack is empty, there is no opening
            # bracket available to match this closing bracket
            if not stack:
                return False

            # Remove the most recently added opening bracket
            top = stack.pop()

            # Check whether the opening and closing brackets match
            if top != matching[char]:
                return False

    # If the stack is empty, every bracket was matched
    return len(stack) == 0


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

text = "{[()]}"

result = is_valid_parentheses(text)

print("Expression:", text)
print("Are parentheses valid:", result)