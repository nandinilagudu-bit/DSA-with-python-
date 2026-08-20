# ---------------------------------------------------------
# DSA Problem 07: Linear Search
# ---------------------------------------------------------
# Problem:
# Given an array and a target value, find the index
# of the target value.
#
# If the target is not present, return -1.
#
# Example:
# Input:  numbers = [10, 25, 7, 42, 18]
#         target = 42
#
# Output: 3
#
# Explanation:
# 42 is present at index 3.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function for Linear Search
def linear_search(numbers, target):

    # Step 1:
    # Traverse through every element of the array.
    #
    # enumerate() gives us both:
    #     i   -> index
    #     num -> value
    for i, num in enumerate(numbers):

        # Step 2:
        # Check whether the current element is equal
        # to the target value.
        if num == target:

            # Step 3:
            # If the target is found, return its index.
            return i

    # Step 4:
    # If the loop finishes and the target was not found,
    # return -1.
    return -1


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array of numbers
numbers = [10, 25, 7, 42, 18]

# Define the value we want to search for
target = 42

# Call the Linear Search function
result = linear_search(numbers, target)

# Display the array
print("Array:", numbers)

# Display the target value
print("Target:", target)

# Check whether the target was found
if result != -1:

    # If result is not -1, the target was found.
    print("Target found at index:", result)

else:

    # If result is -1, the target was not found.
    print("Target not found")