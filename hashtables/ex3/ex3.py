def intersection(arrays):
    """
    YOUR CODE HERE
    """
    nums = {}
    result = []

    # iterate through array
    for i in range(len(arrays)):
        # create key for each value (index)
        for num in arrays[i]:
            # if num already exists in dict, increment count
            if num in nums:
                nums[num] += 1
            # otherwise, that key is the count
            else:
                nums[num] = 1

    # loop through keys in dict
    for key in nums:
        # if key exists in arrays, add to result list
        if nums[key] == len(arrays):
            result.append(key)
    # returns an array with duplicate values
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
