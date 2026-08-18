# ---------------------------------------------------------
# DSA Problem 04: Remove Duplicates from an Array
# ---------------------------------------------------------
# Problem:
# Given an array, remove duplicate elements and return
# an array containing only unique elements.
#
# Example:
# Input:  [10, 20, 10, 30, 20, 40]
# Output: [10, 20, 30, 40]
#
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to remove duplicates
def remove_duplicates(arr):

    # Step 1:
    # Create an empty list to store unique elements.
    unique_elements = []

    # Step 2:
    # Traverse through every element in the array.
    for num in arr:

        # Step 3:
        # Check whether the current number is already
        # present in the unique_elements list.
        if num not in unique_elements:

            # Step 4:
            # If the number is not already present,
            # add it to the unique_elements list.
            unique_elements.append(num)

    # Step 5:
    # Return the list containing only unique elements.
    return unique_elements


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array containing duplicate elements
numbers = [10, 20, 10, 30, 20, 40, 30]

# Display the original array
print("Original array:", numbers)

# Call the function
result = remove_duplicates(numbers)

# Display the array after removing duplicates
print("Array after removing duplicates:", result)