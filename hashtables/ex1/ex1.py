cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Edge case is if there is only one length, then return None.
    if length == 1:
        return None

    ## Add items to cache
    for index, numbers in enumerate(weights):
        if numbers not in cache:
            cache[numbers] = index       

    for index, item in enumerate(weights):
        if (limit - item) in cache:
            if index == cache[(limit - item)]:
                pass
            else:
                if index > cache[(limit - item)]:
                    print(index, cache[(limit - item)])
                    return (index, cache[(limit - item)])
                else:
                    print(cache[(limit - item)], index)
                    return (cache[(limit - item)], index)


# weights_1 = [4, 6, 10, 15, 16]
# get_indices_of_item_weights(weights_1, 5, 21)




# for index, number in enumerate(weights):
#     for indexTwo, numberTwo in enumerate(weights):
        # if index == indexTwo:
        #     pass
#         else:
#             if (numberTwo + number) - limit == 0:
#                 if index > indexTwo:
#                     return (index, indexTwo)
#                 else:
#                     return (indexTwo, index)