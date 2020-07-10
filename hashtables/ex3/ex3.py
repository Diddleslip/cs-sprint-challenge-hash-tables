def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for index in arrays:
        for i in index:
            if i not in cache:
                cache[i] = 1
            else:
                cache[i] += 1

    for key, value in cache.items():
        # print(key, value)
        if value == len(arrays):
            result.append(key)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
