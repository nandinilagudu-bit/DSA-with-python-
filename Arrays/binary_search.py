# ---------------------------------------------------------
# DSA Problem 08: Binary Search
# ---------------------------------------------------------
# Problem:
# Given a SORTED array and a target value, find the
# index of the target using Binary Search.
#
# If the target is not present, return -1.
#
# Example:
# Input:  numbers = [10, 20, 30, 40, 50, 60, 70]
#         target = 50
#
# Output: 4
#
# Time Complexity: O(log n)
# Space Complexity: O(1)
# ---------------------------------------------------------


# Define a function for Binary Search
def binary_search(numbers, target):

    # Step 1:
    # 'left' represents the first index of the
    # current search area.
    left = 0

    # Step 2:
    # 'right' represents the last index of the
    # current search area.
    right = len(numbers) - 1

    # Step 3:
    # Continue searching while there is still
    # a valid search area.
    while left <= right:

        # Step 4:
        # Find the middle index.
        #
        # We use this formula instead of:
        # (left + right) // 2
        #
        # because this version is safer in some
        # programming languages when dealing with
        # very large numbers.
        middle = left + (right - left) // 2

        # Step 5:
        # Check whether the middle element is
        # equal to the target.
        if numbers[middle] == target:

            # Target found!
            # Return the middle index.
            return middle

        # Step 6:
        # If the middle element is smaller than
        # the target, the target must be on the
        # RIGHT side.
        elif numbers[middle] < target:

            # Ignore the left half.
            left = middle + 1

        # Step 7:
        # Otherwise, the middle element is greater
        # than the target.
        else:

            # The target must be on the LEFT side.
            # Ignore the right half.
            right = middle - 1

    # Step 8:
    # If the loop finishes, the target does not
    # exist in the array.
    return -1


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# IMPORTANT:
# The array must be sorted for Binary Search.
numbers = [10, 20, 30, 40, 50, 60, 70]

# Value we want to search for
target = 50

# Call the Binary Search function
result = binary_search(numbers, target)

# Display the array
print("Sorted array:", numbers)

# Display the target
print("Target:", target)

# Check whether the target was found
if result != -1:

    # Target was found.
    print("Target found at index:", result)

else:

    # Target was not found.
    print("Target not found")