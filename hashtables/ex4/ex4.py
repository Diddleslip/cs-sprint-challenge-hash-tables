def has_negatives(a):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    # Add positives to key in dict
    for i in a:
        if i > 0:
            if i not in cache:
                cache[i] = False

    # If negative, switch False to True in cache
    for i in a:
        if i < 0:
            if abs(i) in cache:
                cache[abs(i)] = True
            
    # Append pairs to result 
    for key, value in cache.items():
        if value is True:
            result.append(key)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
