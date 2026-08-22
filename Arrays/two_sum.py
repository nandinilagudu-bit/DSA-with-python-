# ---------------------------------------------------------
# DSA Problem 06: Two Sum
# ---------------------------------------------------------
# Problem:
# Given an array of integers and a target value,
# find the indices of two numbers whose sum equals
# the target.
#
# Example:
# Input:  numbers = [2, 7, 11, 15]
#         target = 9
#
# Output: [0, 1]
#
# Explanation:
# numbers[0] + numbers[1]
#     2    +     7
#     = 9
#
# Time Complexity: O(n)
# Space Complexity: O(n)
# ---------------------------------------------------------


# Define a function to solve the Two Sum problem
def two_sum(numbers, target):

    # Step 1:
    # Create an empty dictionary.
    #
    # The dictionary will store:
    #     number -> index
    #
    # Example:
    #     {2: 0, 7: 1}
    #
    # This allows us to quickly check whether
    # we have already seen a required number.
    seen = {}

    # Step 2:
    # Loop through the array using both the index
    # and the value.
    #
    # enumerate() gives us:
    #     i    = index
    #     num  = current number
    for i, num in enumerate(numbers):

        # Step 3:
        # Calculate the number we need to find.
        #
        # If:
        #     target = 9
        #     num = 2
        #
        # Then:
        #     needed = 9 - 2
        #            = 7
        #
        # So we need to find 7.
        needed = target - num

        # Step 4:
        # Check whether the required number already
        # exists in our dictionary.
        if needed in seen:

            # Step 5:
            # If it exists, return the index of the
            # required number and the current index.
            return [seen[needed], i]

        # Step 6:
        # If the required number was not found,
        # store the current number and its index.
        seen[num] = i

    # Step 7:
    # If no two numbers add up to the target,
    # return an empty list.
    return []


# ---------------------------------------------------------
# Test the function
# ---------------------------------------------------------

# Create an array of numbers
numbers = [2, 7, 11, 15]

# Define the target sum
target = 9

# Call the function
result = two_sum(numbers, target)

# Display the input array
print("Array:", numbers)

# Display the target
print("Target:", target)

# Display the result
print("Indices:", result)