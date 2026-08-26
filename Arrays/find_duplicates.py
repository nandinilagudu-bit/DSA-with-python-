# ---------------------------------------------------------
# DSA Problem 10: Find Duplicate Elements in an Array
# ---------------------------------------------------------
# Problem:
# Given an array of numbers, find all the elements
# that appear more than once.
#
# Example:
# Input:  [1, 2, 3, 2, 4, 5, 1]
# Output: [2, 1]
#
# Explanation:
# 2 appears more than once.
# 1 appears more than once.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to find duplicate elements
def find_duplicates(numbers):

    # Step 1:
    # Create a set to store numbers that we have
    # already encountered.
    seen = set()

    # Step 2:
    # Create an empty list to store duplicate elements.
    duplicates = []

    # Step 3:
    # Traverse through every number in the array.
    for num in numbers:

        # Step 4:
        # Check whether the current number is already
        # present in the 'seen' set.
        if num in seen:

            # Step 5:
            # The number has appeared before, so it is
            # a duplicate.
            #
            # Before adding it, check whether it is
            # already in the duplicates list.
            if num not in duplicates:

                # Add the duplicate number to the list.
                duplicates.append(num)

        else:

            # Step 6:
            # If the number has not been seen before,
            # add it to the 'seen' set.
            seen.add(num)

    # Step 7:
    # Return the list of duplicate elements.
    return duplicates


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array containing duplicate elements
numbers = [1, 2, 3, 2, 4, 5, 1]

# Call the function
result = find_duplicates(numbers)

# Display the original array
print("Array:", numbers)

# Display the duplicate elements
print("Duplicate elements:", result)