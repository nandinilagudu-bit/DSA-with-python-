# ---------------------------------------------------------
# DSA Problem 02: Find the Second Largest Element
# ---------------------------------------------------------
# Problem:
# Given an array of numbers, find the second largest
# element without using Python's built-in sort() function.
#
# Example:
# Input:  [10, 25, 7, 42, 18]
# Output: 25
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to find the second largest element
def find_second_largest(arr):

    # Step 1:
    # We need at least two elements to find
    # the second largest element.
    if len(arr) < 2:
        return None

    # Step 2:
    # Start with the first element as the largest.
    largest = arr[0]

    # Step 3:
    # Start with None because we have not found
    # a second largest value yet.
    second_largest = None

    # Step 4:
    # Traverse every element in the array.
    for num in arr[1:]:

        # Step 5:
        # If the current number is greater than
        # the current largest number...
        if num > largest:

            # The old largest becomes the second largest.
            second_largest = largest

            # The current number becomes the new largest.
            largest = num

        # Step 6:
        # If the current number is smaller than the largest
        # but greater than the current second largest,
        # update second_largest.
        elif num != largest and (
            second_largest is None or num > second_largest
        ):
            second_largest = num

    # Step 7:
    # Return the second largest element.
    return second_largest


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array of numbers
numbers = [10, 25, 7, 42, 18]

# Call the function
result = find_second_largest(numbers)

# Display the original array
print("Array:", numbers)

# Display the second largest element
print("Second largest element:", result)