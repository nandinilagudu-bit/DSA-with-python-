# ---------------------------------------------------------
# DSA Problem 03: Reverse an Array
# ---------------------------------------------------------
# Problem:
# Given an array, reverse the elements of the array
# without using Python's built-in reverse() or slicing.
#
# Example:
# Input:  [10, 20, 30, 40, 50]
# Output: [50, 40, 30, 20, 10]
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to reverse the array
def reverse_array(arr):

    # Step 1:
    # 'left' points to the first element of the array.
    left = 0

    # Step 2:
    # 'right' points to the last element of the array.
    right = len(arr) - 1

    # Step 3:
    # Continue swapping elements while the left pointer
    # is before the right pointer.
    while left < right:

        # Step 4:
        # Swap the elements at the left and right positions.
        #
        # Example:
        # [10, 20, 30, 40, 50]
        #  ↑              ↑
        # left           right
        #
        # After swapping:
        # [50, 20, 30, 40, 10]
        arr[left], arr[right] = arr[right], arr[left]

        # Step 5:
        # Move the left pointer one position to the right.
        left += 1

        # Step 6:
        # Move the right pointer one position to the left.
        right -= 1

    # Step 7:
    # Return the reversed array.
    return arr


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array
numbers = [10, 20, 30, 40, 50]

# Display the original array
print("Original array:", numbers)

# Call the function
result = reverse_array(numbers)

# Display the reversed array
print("Reversed array:", result)