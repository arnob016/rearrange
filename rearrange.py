#Hello, here's how you rearrange an array in python if this is what you were looking for.

def rearrange_array(numbers):
    positives = [num for num in numbers if num >= 0]
    negatives = [num for num in numbers if num < 0]

    rearranged_numbers = negatives + positives

    return rearranged_numbers

# Here's an array of numbers
numbers = [3, -2, 1, -5, 4, -6, 8, 0, -3]
rearranged = rearrange_array(numbers)
print(rearranged)
