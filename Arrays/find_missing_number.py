# ---------------------------------------------------------
# DSA Problem 09: Find the Missing Number
# ---------------------------------------------------------
# Problem:
# Given an array containing n distinct numbers taken from
# the range 0 to n, find the one number that is missing.
#
# Example:
# Input:  [3, 0, 1]
# Output: 2
#
# Explanation:
# The numbers should be:
# [0, 1, 2, 3]
#
# But 2 is missing.
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to find the missing number
def find_missing_number(numbers):

    # Step 1:
    # Find the number of elements in the array.
    n = len(numbers)

    # Step 2:
    # Calculate the expected sum of numbers from
    # 0 to n.
    #
    # Formula:
    # n * (n + 1) / 2
    #
    # For n = 3:
    # 3 * 4 / 2 = 6
    expected_sum = n * (n + 1) // 2

    # Step 3:
    # Calculate the actual sum of all numbers
    # present in the array.
    actual_sum = sum(numbers)

    # Step 4:
    # The difference between the expected sum and
    # actual sum is the missing number.
    missing_number = expected_sum - actual_sum

    # Step 5:
    # Return the missing number.
    return missing_number


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array containing numbers from 0 to n
# with one number missing.
numbers = [3, 0, 1]

# Call the function
result = find_missing_number(numbers)

# Display the original array
print("Array:", numbers)

# Display the missing number
print("Missing number:", result)