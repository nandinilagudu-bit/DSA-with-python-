# ---------------------------------------------------------
# DSA Problem 01: Find the Largest Element in an Array
# ---------------------------------------------------------
# Problem:
# Given an array of numbers, find the largest element
# without using Python's built-in max() function.
#
# Example:
# Input:  [10, 25, 7, 42, 18]
# Output: 42
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to find the largest element
def find_largest(arr):

    # Step 1:
    # Check if the array is empty.
    # If there are no elements, return None.
    if not arr:
        return None

    # Step 2:
    # Assume that the first element is the largest.
    # We will compare this value with the remaining elements.
    largest = arr[0]

    # Step 3:
    # Loop through the array starting from the second element.
    # We don't need to compare the first element with itself.
    for num in arr[1:]:

        # Step 4:
        # Check whether the current element is greater
        # than the largest element found so far.
        if num > largest:

            # Step 5:
            # If the current element is larger,
            # update the value of 'largest'.
            largest = num

    # Step 6:
    # After checking all elements, return the largest value.
    return largest


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array of numbers
numbers = [10, 25, 7, 42, 18]

# Call the function and store the result
result = find_largest(numbers)

# Display the original array
print("Array:", numbers)

# Display the largest element
print("Largest element:", result)