# ---------------------------------------------------------
# DSA Problem 05: Move All Zeros to the End
# ---------------------------------------------------------
# Problem:
# Given an array containing zeros and non-zero numbers,
# move all zeros to the end of the array.
#
# The order of the non-zero elements must remain the same.
#
# Example:
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Time Complexity: O(n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function to move all zeros to the end
def move_zeros(arr):

    # Step 1:
    # 'position' keeps track of where the next
    # non-zero element should be placed.
    position = 0

    # Step 2:
    # Traverse through every element of the array.
    for i in range(len(arr)):

        # Step 3:
        # Check if the current element is NOT zero.
        if arr[i] != 0:

            # Step 4:
            # Swap the current non-zero element with
            # the element at the 'position' index.
            #
            # This moves the non-zero element toward
            # the beginning of the array.
            arr[position], arr[i] = arr[i], arr[position]

            # Step 5:
            # Move 'position' forward because we have
            # successfully placed one non-zero element.
            position += 1

    # Step 6:
    # Return the modified array.
    return arr


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array containing zeros and non-zero numbers
numbers = [0, 1, 0, 3, 12]

# Display the original array
print("Original array:", numbers)

# Call the function
result = move_zeros(numbers)

# Display the modified array
print("Array after moving zeros:", result)