# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []

    for i in files:
        splitted = i.split("/")[-1]
        if splitted not in cache:
            cache[splitted] = [i]
        else:
            cache[splitted].append(i)


    for query in queries:
        if query in cache:
            result.append(cache[query])

    print("This is result: ",result)
    ## Since result has nested arrays, we need double for loop to put them in last_result.
    last_result = []
    for i in result:
        for e in i:
            last_result.append(e)

    return last_result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
