def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    weight = {}

    # loop through length of list
    for i in range(length):
        # assign pointer to current index
        cur = weights[i]
        # if current weight already in dict, add it to value of key
        if cur in weight:
            weight[cur].append(i)
        # if current weight not in dict, current = current index
        else:
            weight[cur] = [i]
    
    # loop through keys in weight dict
    for key in weight:
        # subtract current key(weight) from limit to find target weight
        target = limit - key
        # if target weight in dict
        if target in weight:
            # if target weight has a duplicate
            if len(weight[target]) != 1:
                # return tuple of indices of duplicates
                return tuple(sorted(weight[target], reverse=True))
            # no duplicate, 1st time seeing this value
            else:
                # return tuple with target weight and key
                return tuple(sorted((weight[target][0], weight[key][0]), reverse=True))
    # if key does not exist, return None
    return None
