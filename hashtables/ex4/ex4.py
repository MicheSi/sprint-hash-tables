def has_negatives(a):
    """
    YOUR CODE HERE
    """
    nums = {}
    result = []

    # iterate through a
    for num in a:
        # change num to absolute value and check if already in dict
        if abs(num) in nums:
            # add absolute value to result
            result.append(abs(num))
        # num doesn't exist, so it's the only one
        else:
            nums[abs(num)] = 1
    # return array with absolute values of duplicates
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
